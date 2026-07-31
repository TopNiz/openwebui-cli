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


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise APIError(f"Open WebUI returned an invalid {label}.")
    return value


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
