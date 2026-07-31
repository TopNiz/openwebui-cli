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


def test_root_and_nested_help() -> None:
    for arguments in (
        ["--help"],
        ["system", "--help"],
        ["system", "config", "--help"],
        ["system", "config", "set", "--help"],
        ["profile", "set", "--help"],
        ["auth", "status", "--help"],
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
