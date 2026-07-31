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
