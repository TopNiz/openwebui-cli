from __future__ import annotations

import json
from pathlib import Path

import respx
from httpx import Response
from typer.testing import CliRunner

from openwebui_cli.cli import app

runner = CliRunner()
BASE_URL = "https://example.test"
ENV = {
    "OPENWEBUI_BASE_URL": BASE_URL,
    "OPENWEBUI_API_KEY": "not-a-real-credential",
}
SYSTEM_CONFIG = {
    "ENABLE_SIGNUP": False,
    "ENABLE_API_KEYS": True,
    "WEBUI_URL": BASE_URL,
}


def test_version_option_without_command() -> None:
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0, result.output
    assert result.output.strip() == "0.1.0a3"


def test_root_and_nested_help() -> None:
    for arguments in (
        ["--help"],
        ["profile", "--help"],
        ["profile", "list", "--help"],
        ["profile", "show", "--help"],
        ["profile", "set", "--help"],
        ["profile", "use", "--help"],
        ["auth", "--help"],
        ["auth", "keyring-store", "--help"],
        ["auth", "status", "--help"],
        ["system", "--help"],
        ["system", "config", "--help"],
        ["system", "config", "get", "--help"],
        ["system", "config", "export", "--help"],
        ["system", "config", "set", "--help"],
        ["system", "config", "apply", "--help"],
        ["users", "--help"],
        ["users", "list", "--help"],
        ["users", "get", "--help"],
        ["users", "create", "--help"],
        ["users", "update", "--help"],
        ["users", "reset-password", "--help"],
        ["permissions", "--help"],
        ["permissions", "get", "--help"],
        ["permissions", "export", "--help"],
        ["permissions", "set", "--help"],
        ["permissions", "apply", "--help"],
        ["user-settings", "--help"],
        ["user-settings", "get", "--help"],
        ["user-settings", "export", "--help"],
        ["user-settings", "set", "--help"],
        ["user-settings", "apply", "--help"],
    ):
        result = runner.invoke(app, arguments)
        assert result.exit_code == 0, result.output
        assert "help" in result.output.lower()


@respx.mock
def test_system_config_get() -> None:
    respx.get(f"{BASE_URL}/api/v1/auths/admin/config").mock(
        return_value=Response(200, json=SYSTEM_CONFIG)
    )

    result = runner.invoke(app, ["system", "config", "get", "ENABLE_SIGNUP"], env=ENV)

    assert result.exit_code == 0, result.output
    assert json.loads(result.output) == {"ENABLE_SIGNUP": False}


@respx.mock
def test_system_config_set_dry_run_does_not_post() -> None:
    respx.get(f"{BASE_URL}/api/v1/auths/admin/config").mock(
        return_value=Response(200, json=SYSTEM_CONFIG)
    )
    post = respx.post(f"{BASE_URL}/api/v1/auths/admin/config")

    result = runner.invoke(
        app,
        ["system", "config", "set", "ENABLE_SIGNUP", "true", "--dry-run"],
        env=ENV,
    )

    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["dry_run"] is True
    assert payload["changes"]["ENABLE_SIGNUP"]["after"] is True
    assert not post.called


@respx.mock
def test_system_config_apply_posts_complete_configuration(tmp_path: Path) -> None:
    patch = tmp_path / "patch.json"
    patch.write_text('{"ENABLE_SIGNUP": true}')
    respx.get(f"{BASE_URL}/api/v1/auths/admin/config").mock(
        return_value=Response(200, json=SYSTEM_CONFIG)
    )
    post = respx.post(f"{BASE_URL}/api/v1/auths/admin/config").mock(
        return_value=Response(200, json={**SYSTEM_CONFIG, "ENABLE_SIGNUP": True})
    )

    result = runner.invoke(
        app,
        ["system", "config", "apply", str(patch), "--yes"],
        env=ENV,
    )

    assert result.exit_code == 0, result.output
    assert post.called
    assert json.loads(post.calls[0].request.content) == {
        **SYSTEM_CONFIG,
        "ENABLE_SIGNUP": True,
    }


@respx.mock
def test_create_user_does_not_output_password_or_returned_token() -> None:
    route = respx.post(f"{BASE_URL}/api/v1/auths/add").mock(
        return_value=Response(
            200,
            json={
                "id": "user-1",
                "name": "Example User",
                "email": "user@example.test",
                "role": "user",
                "profile_image_url": "/user.png",
                "token": "not-a-real-session-token",
                "token_type": "Bearer",
            },
        )
    )

    result = runner.invoke(
        app,
        [
            "users",
            "create",
            "Example User",
            "user@example.test",
            "--password-stdin",
            "--yes",
        ],
        input="not-a-real-password\n",
        env=ENV,
    )

    assert result.exit_code == 0, result.output
    assert route.called
    assert "not-a-real-password" not in result.output
    assert "not-a-real-session-token" not in result.output
    assert json.loads(result.output)["user"]["id"] == "user-1"


@respx.mock
def test_default_permission_set_dry_run() -> None:
    respx.get(f"{BASE_URL}/api/v1/users/default/permissions").mock(
        return_value=Response(200, json={"features": {"api_keys": False}})
    )
    post = respx.post(f"{BASE_URL}/api/v1/users/default/permissions")

    result = runner.invoke(
        app,
        ["permissions", "set", "features.api_keys", "true", "--dry-run"],
        env=ENV,
    )

    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["changes"]["features.api_keys"]["after"] is True
    assert not post.called


@respx.mock
def test_user_settings_nested_set_posts_complete_document() -> None:
    respx.get(f"{BASE_URL}/api/v1/users/user/settings").mock(
        return_value=Response(200, json={"ui": {"theme": "dark", "language": "fr"}})
    )
    post = respx.post(f"{BASE_URL}/api/v1/users/user/settings/update").mock(
        return_value=Response(200, json={"ui": {"theme": "light", "language": "fr"}})
    )

    result = runner.invoke(
        app,
        ["user-settings", "set", "ui.theme", "light", "--yes"],
        env=ENV,
    )

    assert result.exit_code == 0, result.output
    assert post.called
    assert json.loads(post.calls[0].request.content) == {"ui": {"theme": "light", "language": "fr"}}


def test_profile_set_never_writes_api_key(tmp_path: Path) -> None:
    config = tmp_path / "config.toml"

    result = runner.invoke(
        app,
        [
            "--config",
            str(config),
            "profile",
            "set",
            "demo",
            "--url",
            BASE_URL,
            "--keyring-service",
            "owui-demo",
            "--keyring-username",
            "service-account",
            "--activate",
        ],
    )

    assert result.exit_code == 0, result.output
    assert "api_key" not in config.read_text().lower()
