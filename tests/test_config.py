from __future__ import annotations

from pathlib import Path

import keyring
import pytest

from openwebui_cli.config import (
    ENV_API_KEY,
    ENV_BASE_URL,
    AppConfig,
    ConfigStore,
    Profile,
    resolve_connection,
)
from openwebui_cli.exceptions import ConfigurationError


def test_profile_round_trip_omits_secrets(tmp_path: Path) -> None:
    store = ConfigStore(tmp_path / "config.toml")
    profile = Profile(
        name="demo",
        base_url="https://example.test/",
        keyring_service="owui-demo",
        keyring_username="service-account",
    )

    store.upsert_profile(profile, activate=True)
    loaded = store.load()

    assert loaded.active_profile == "demo"
    assert loaded.profiles["demo"].normalized_url() == "https://example.test"
    text = store.path.read_text()
    assert "api_key" not in text.lower()
    assert store.path.stat().st_mode & 0o777 == 0o600


def test_environment_takes_precedence_over_profile(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    store = ConfigStore(tmp_path / "config.toml")
    store.save(
        AppConfig(
            active_profile="demo",
            profiles={"demo": Profile(name="demo", base_url="https://profile.test")},
        )
    )
    monkeypatch.setenv(ENV_BASE_URL, "https://environment.test/")
    monkeypatch.setenv(ENV_API_KEY, "not-a-real-credential")

    connection = resolve_connection(store)

    assert connection.base_url == "https://environment.test"
    assert connection.api_key == "not-a-real-credential"
    assert "not-a-real-credential" not in repr(connection)


def test_keyring_resolution(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    store = ConfigStore(tmp_path / "config.toml")
    store.upsert_profile(
        Profile(
            name="demo",
            base_url="https://example.test",
            keyring_service="owui-demo",
            keyring_username="service-account",
        ),
        activate=True,
    )
    monkeypatch.delenv(ENV_API_KEY, raising=False)
    monkeypatch.setattr(keyring, "get_password", lambda service, username: "keyring-value")

    connection = resolve_connection(store)

    assert connection.api_key == "keyring-value"


def test_missing_credential_is_actionable(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(ENV_API_KEY, raising=False)
    monkeypatch.delenv(ENV_BASE_URL, raising=False)

    with pytest.raises(ConfigurationError, match="No Open WebUI URL"):
        resolve_connection(ConfigStore(tmp_path / "missing.toml"))
