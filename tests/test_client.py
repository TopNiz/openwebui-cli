from __future__ import annotations

import json

import httpx
import pytest

from openwebui_cli.client import OpenWebUIClient
from openwebui_cli.config import ResolvedConnection
from openwebui_cli.exceptions import APIError, ValidationError


def connection() -> ResolvedConnection:
    return ResolvedConnection(
        base_url="https://example.test",
        api_key="not-a-real-credential",
    )


def test_get_and_patch_system_configuration() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert request.headers["authorization"].startswith("Bearer ")
        if request.method == "GET":
            return httpx.Response(
                200, json={"ENABLE_SIGNUP": False, "WEBUI_URL": "https://ui.test"}
            )
        payload = json.loads(request.content)
        assert payload == {"ENABLE_SIGNUP": True, "WEBUI_URL": "https://ui.test"}
        return httpx.Response(200, json=payload)

    with OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client:
        updated = client.patch_system_config({"ENABLE_SIGNUP": True})

    assert updated["ENABLE_SIGNUP"] is True
    assert [request.method for request in requests] == ["GET", "POST"]


def test_unknown_system_configuration_key_is_rejected_before_post() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"ENABLE_SIGNUP": False})

    with (
        OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client,
        pytest.raises(ValidationError, match="UNKNOWN"),
    ):
        client.patch_system_config({"UNKNOWN": True})


def test_server_error_redacts_active_credential() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"detail": "not-a-real-credential was rejected"})

    with (
        OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client,
        pytest.raises(APIError) as captured,
    ):
        client.get_system_config()

    assert "not-a-real-credential" not in str(captured.value)
    assert "[REDACTED]" in str(captured.value)


def test_create_user_discards_returned_session_token() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        payload = json.loads(request.content)
        assert payload["password"] == "not-a-real-password"
        return httpx.Response(
            200,
            json={
                "id": "user-1",
                "name": payload["name"],
                "email": payload["email"],
                "role": payload["role"],
                "profile_image_url": "/user.png",
                "token": "not-a-real-session-token",
                "token_type": "Bearer",
            },
        )

    with OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client:
        user = client.create_user(
            name="Example User",
            email="user@example.test",
            password="not-a-real-password",
        )

    assert user["id"] == "user-1"
    assert "token" not in user
    assert "password" not in user


def test_list_users_removes_private_embedded_fields() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "users": [
                    {
                        "id": "user-1",
                        "name": "Example User",
                        "email": "user@example.test",
                        "role": "user",
                        "settings": {"ui": {"theme": "dark"}},
                        "oauth": {"provider": "example"},
                    }
                ],
                "total": 1,
            },
        )

    with OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client:
        result = client.list_users()

    assert result["total"] == 1
    assert "settings" not in result["users"][0]
    assert "oauth" not in result["users"][0]


def test_user_settings_and_default_permissions_round_trip() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET" and request.url.path.endswith("/permissions"):
            return httpx.Response(200, json={"features": {"api_keys": False}})
        if request.method == "GET":
            return httpx.Response(200, json={"ui": {"theme": "dark"}})
        return httpx.Response(200, json=json.loads(request.content))

    with OpenWebUIClient(connection(), transport=httpx.MockTransport(handler)) as client:
        permissions = client.get_default_permissions()
        settings = client.replace_user_settings({"ui": {"theme": "light"}})

    assert permissions["features"]["api_keys"] is False
    assert settings["ui"]["theme"] == "light"
