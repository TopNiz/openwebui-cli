"""Stable high-level Open WebUI API client."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

from openwebui_cli.config import ResolvedConnection
from openwebui_cli.exceptions import APIError, ValidationError
from openwebui_cli.version import __version__


class OpenWebUIClient:
    """Synchronous high-level client for stable administration workflows.

    The generated ``openwebui_client`` package exposes every operation from the
    pinned OpenAPI document. This facade intentionally provides short, stable
    method names for workflows supported by the CLI.
    """

    def __init__(
        self,
        connection: ResolvedConnection,
        *,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self._connection = connection
        self._api_key = connection.api_key
        self._http = httpx.Client(
            base_url=connection.base_url,
            headers={
                "Authorization": f"Bearer {connection.api_key}",
                "Accept": "application/json",
                "User-Agent": f"openwebui-cli/{__version__}",
            },
            timeout=connection.timeout,
            verify=connection.verify_ssl,
            transport=transport,
        )

    def __enter__(self) -> OpenWebUIClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def close(self) -> None:
        """Release network resources."""

        self._http.close()

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        """Perform an authenticated request and return decoded JSON when available."""

        try:
            response = self._http.request(method, path, **kwargs)
        except httpx.TimeoutException as exc:
            raise APIError("The Open WebUI request timed out.") from exc
        except httpx.HTTPError as exc:
            raise APIError("Open WebUI could not be reached.") from exc

        if response.is_error:
            detail = _safe_error_detail(response, self._api_key)
            message = f"Open WebUI returned HTTP {response.status_code}"
            if detail:
                message += f": {detail}"
            raise APIError(message, status_code=response.status_code)
        if response.status_code == 204 or not response.content:
            return None
        content_type = response.headers.get("content-type", "")
        if "json" in content_type:
            return response.json()
        return response.text

    def who_am_i(self) -> dict[str, Any]:
        """Return the authenticated account summary."""

        return _require_mapping(self.request("GET", "/api/v1/auths/"), "account response")

    def get_system_config(self) -> dict[str, Any]:
        """Read administrator-level system configuration."""

        return _require_mapping(
            self.request("GET", "/api/v1/auths/admin/config"), "system configuration"
        )

    def replace_system_config(self, config: Mapping[str, Any]) -> dict[str, Any]:
        """Submit the complete administrator configuration object."""

        return _require_mapping(
            self.request("POST", "/api/v1/auths/admin/config", json=dict(config)),
            "updated system configuration",
        )

    def patch_system_config(self, patch: Mapping[str, Any]) -> dict[str, Any]:
        """Fetch, validate, merge, and replace system configuration safely."""

        current = self.get_system_config()
        unknown = sorted(set(patch) - set(current))
        if unknown:
            raise ValidationError(f"Unknown system configuration key(s): {', '.join(unknown)}")
        updated = {**current, **dict(patch)}
        return self.replace_system_config(updated)

    def list_users(
        self,
        *,
        query: str | None = None,
        order_by: str | None = None,
        direction: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Return one page of users visible to the authenticated administrator."""

        params = {
            key: value
            for key, value in {
                "query": query,
                "order_by": order_by,
                "direction": direction,
                "page": page,
            }.items()
            if value is not None
        }
        result = _require_mapping(self.request("GET", "/api/v1/users/", params=params), "user list")
        users = result.get("users")
        if not isinstance(users, list) or not all(isinstance(user, dict) for user in users):
            raise APIError("Open WebUI returned an invalid user list.")
        return {
            "users": [_public_user(user) for user in users],
            "total": result.get("total", len(users)),
        }

    def create_user(
        self,
        *,
        name: str,
        email: str,
        password: str,
        role: str = "user",
        profile_image_url: str = "/user.png",
    ) -> dict[str, Any]:
        """Create a user and discard the session token returned by Open WebUI."""

        _validate_role(role)
        response = _require_mapping(
            self.request(
                "POST",
                "/api/v1/auths/add",
                json={
                    "name": name,
                    "email": email,
                    "password": password,
                    "role": role,
                    "profile_image_url": profile_image_url,
                },
            ),
            "created user",
        )
        return _public_user(response)

    def update_user(self, user_id: str, patch: Mapping[str, Any]) -> dict[str, Any]:
        """Update supported account fields; passwords are accepted only in memory."""

        allowed = {"role", "name", "email", "profile_image_url", "password"}
        unknown = sorted(set(patch) - allowed)
        if unknown:
            raise ValidationError(f"Unsupported user field(s): {', '.join(unknown)}")
        if "role" in patch and patch["role"] is not None:
            _validate_role(str(patch["role"]))
        response = _require_mapping(
            self.request("POST", f"/api/v1/users/{user_id}/update", json=dict(patch)),
            "updated user",
        )
        return _public_user(response)

    def get_default_permissions(self) -> dict[str, Any]:
        """Read permissions inherited by ordinary users."""

        return _require_mapping(
            self.request("GET", "/api/v1/users/default/permissions"),
            "default user permissions",
        )

    def replace_default_permissions(self, permissions: Mapping[str, Any]) -> dict[str, Any]:
        """Replace the complete default-permissions document."""

        result = self.request("POST", "/api/v1/users/default/permissions", json=dict(permissions))
        if result is None:
            return dict(permissions)
        return _require_mapping(result, "updated default user permissions")

    def get_user_settings(self) -> dict[str, Any]:
        """Read settings for the account owning the active API key."""

        result = self.request("GET", "/api/v1/users/user/settings")
        if result is None:
            return {}
        return _require_mapping(result, "user settings")

    def replace_user_settings(self, settings: Mapping[str, Any]) -> dict[str, Any]:
        """Replace settings for the account owning the active API key."""

        return _require_mapping(
            self.request("POST", "/api/v1/users/user/settings/update", json=dict(settings)),
            "updated user settings",
        )


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise APIError(f"Open WebUI returned an invalid {label}.")
    return value


def _public_user(user: Mapping[str, Any]) -> dict[str, Any]:
    """Return account metadata while excluding tokens, passwords, settings, and OAuth data."""

    safe_fields = (
        "id",
        "name",
        "email",
        "role",
        "profile_image_url",
        "is_active",
        "group_ids",
        "last_active_at",
        "created_at",
        "updated_at",
    )
    return {field: user.get(field) for field in safe_fields if field in user}


def _validate_role(role: str) -> None:
    if role not in {"pending", "user", "admin"}:
        raise ValidationError("User role must be pending, user, or admin.")


def _safe_error_detail(response: httpx.Response, api_key: str) -> str:
    """Extract a bounded server detail while redacting the active credential."""

    detail = ""
    try:
        payload = response.json()
        if isinstance(payload, dict):
            candidate = payload.get("detail") or payload.get("message")
            if isinstance(candidate, (str, int, float, bool)):
                detail = str(candidate)
    except ValueError:
        detail = ""
    return detail.replace(api_key, "[REDACTED]")[:500]
