"""Profiles and credential resolution.

Profile files contain connection metadata only. API keys are resolved from the
process environment or an operating-system keyring and are never serialized.
"""

from __future__ import annotations

import os
import stat
import tempfile
import tomllib
from contextlib import suppress
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import tomli_w
from platformdirs import user_config_path

from openwebui_cli.exceptions import ConfigurationError

ENV_PROFILE = "OPENWEBUI_PROFILE"
ENV_BASE_URL = "OPENWEBUI_BASE_URL"
ENV_API_KEY = "OPENWEBUI_API_KEY"
ENV_CONFIG = "OPENWEBUI_CONFIG"


@dataclass(frozen=True, slots=True)
class Profile:
    """Non-secret connection metadata for one Open WebUI instance."""

    name: str
    base_url: str
    keyring_service: str | None = None
    keyring_username: str | None = None
    verify_ssl: bool = True
    timeout: float = 30.0

    def normalized_url(self) -> str:
        url = self.base_url.strip().rstrip("/")
        if not url.startswith(("https://", "http://")):
            raise ConfigurationError("The Open WebUI base URL must start with https:// or http://.")
        return url


@dataclass(frozen=True, slots=True)
class ResolvedConnection:
    """Runtime connection details; the credential is excluded from repr."""

    base_url: str
    api_key: str = field(repr=False)
    verify_ssl: bool = True
    timeout: float = 30.0
    profile_name: str | None = None


@dataclass(slots=True)
class AppConfig:
    """Parsed profile configuration."""

    active_profile: str | None = None
    profiles: dict[str, Profile] = field(default_factory=dict)


class ConfigStore:
    """Read and atomically write the non-secret TOML profile file."""

    def __init__(self, path: Path | str | None = None) -> None:
        configured = path or os.environ.get(ENV_CONFIG)
        self.path = Path(configured).expanduser() if configured else default_config_path()

    def load(self) -> AppConfig:
        if not self.path.exists():
            return AppConfig()
        try:
            raw = tomllib.loads(self.path.read_text())
        except (OSError, tomllib.TOMLDecodeError) as exc:
            raise ConfigurationError(f"Cannot read configuration file {self.path}: {exc}") from exc

        profiles: dict[str, Profile] = {}
        for name, values in raw.get("profiles", {}).items():
            if not isinstance(values, dict) or not values.get("base_url"):
                raise ConfigurationError(f"Profile {name!r} does not define base_url.")
            profiles[name] = Profile(
                name=name,
                base_url=str(values["base_url"]),
                keyring_service=_optional_string(values.get("keyring_service")),
                keyring_username=_optional_string(values.get("keyring_username")),
                verify_ssl=bool(values.get("verify_ssl", True)),
                timeout=float(values.get("timeout", 30.0)),
            )
        active = _optional_string(raw.get("active_profile"))
        return AppConfig(active_profile=active, profiles=profiles)

    def save(self, config: AppConfig) -> None:
        payload: dict[str, Any] = {}
        if config.active_profile:
            payload["active_profile"] = config.active_profile
        payload["profiles"] = {
            name: {
                key: value
                for key, value in asdict(profile).items()
                if key != "name" and value is not None
            }
            for name, profile in sorted(config.profiles.items())
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        mode = stat.S_IRUSR | stat.S_IWUSR
        fd, temporary_name = tempfile.mkstemp(
            prefix="config.", suffix=".toml", dir=self.path.parent
        )
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(tomli_w.dumps(payload).encode())
            os.chmod(temporary_name, mode)
            os.replace(temporary_name, self.path)
        except Exception:
            with suppress(FileNotFoundError):
                os.unlink(temporary_name)
            raise

    def upsert_profile(self, profile: Profile, *, activate: bool = False) -> AppConfig:
        config = self.load()
        config.profiles[profile.name] = profile
        if activate or not config.active_profile:
            config.active_profile = profile.name
        self.save(config)
        return config

    def activate(self, name: str) -> AppConfig:
        config = self.load()
        if name not in config.profiles:
            raise ConfigurationError(f"Unknown profile {name!r}.")
        config.active_profile = name
        self.save(config)
        return config


def default_config_path() -> Path:
    """Return the platform-appropriate profile path."""

    return user_config_path("openwebui-cli", ensure_exists=False) / "config.toml"


def resolve_connection(
    store: ConfigStore,
    *,
    profile_name: str | None = None,
    base_url: str | None = None,
) -> ResolvedConnection:
    """Resolve profile, environment overrides, and API key without exposing it."""

    config = store.load()
    selected_name = profile_name or os.environ.get(ENV_PROFILE) or config.active_profile
    profile = config.profiles.get(selected_name) if selected_name else None
    if selected_name and profile is None:
        raise ConfigurationError(f"Unknown profile {selected_name!r}.")

    resolved_url = (
        base_url or os.environ.get(ENV_BASE_URL) or (profile.base_url if profile else None)
    )
    if not resolved_url:
        raise ConfigurationError(
            "No Open WebUI URL is configured. Set OPENWEBUI_BASE_URL or create a profile."
        )

    api_key = os.environ.get(ENV_API_KEY)
    if not api_key and profile:
        api_key = _read_keyring(profile)
    if not api_key:
        raise ConfigurationError(
            "No API key is available. Set OPENWEBUI_API_KEY or store one in the profile keyring."
        )

    normalized_url = Profile(name="runtime", base_url=resolved_url).normalized_url()
    return ResolvedConnection(
        base_url=normalized_url,
        api_key=api_key,
        verify_ssl=profile.verify_ssl if profile else True,
        timeout=profile.timeout if profile else 30.0,
        profile_name=selected_name,
    )


def store_profile_api_key(profile: Profile, api_key: str) -> None:
    """Store a key in the OS keyring; callers must collect it through protected input."""

    if not profile.keyring_service or not profile.keyring_username:
        raise ConfigurationError(
            "The profile must define keyring_service and keyring_username before storing a key."
        )
    if not api_key:
        raise ConfigurationError("An empty API key cannot be stored.")
    try:
        import keyring

        keyring.set_password(profile.keyring_service, profile.keyring_username, api_key)
    except Exception as exc:
        raise ConfigurationError(
            "The operating-system keyring could not store the API key."
        ) from exc


def _read_keyring(profile: Profile) -> str | None:
    if not profile.keyring_service or not profile.keyring_username:
        return None
    try:
        import keyring

        return keyring.get_password(profile.keyring_service, profile.keyring_username)
    except Exception as exc:
        raise ConfigurationError(
            "The operating-system keyring could not read the API key."
        ) from exc


def _optional_string(value: object) -> str | None:
    return str(value) if value is not None and str(value) else None
