"""Self-documenting ``owui`` command-line interface."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Any, NoReturn

import typer

from openwebui_cli.client import OpenWebUIClient
from openwebui_cli.config import (
    ConfigStore,
    Profile,
    resolve_connection,
    store_profile_api_key,
)
from openwebui_cli.exceptions import OpenWebUIError, ValidationError
from openwebui_cli.output import emit, write_json_file
from openwebui_cli.values import changes_between, parse_cli_value
from openwebui_cli.version import __version__

app = typer.Typer(
    name="owui",
    no_args_is_help=True,
    help=(
        "Administer Open WebUI from a terminal or automation. Credentials are read from "
        "OPENWEBUI_API_KEY or an OS keyring and are never accepted as command arguments."
    ),
)
profile_app = typer.Typer(no_args_is_help=True, help="Manage non-secret instance profiles.")
auth_app = typer.Typer(no_args_is_help=True, help="Configure and verify API authentication.")
system_app = typer.Typer(no_args_is_help=True, help="Manage administrator-level system settings.")
system_config_app = typer.Typer(
    no_args_is_help=True,
    help="Read, export, compare, and patch the complete Open WebUI administrator configuration.",
)
app.add_typer(profile_app, name="profile")
app.add_typer(auth_app, name="auth")
app.add_typer(system_app, name="system")
system_app.add_typer(system_config_app, name="config")


@dataclass(slots=True)
class State:
    profile: str | None
    base_url: str | None
    config_file: Path | None
    compact: bool

    def store(self) -> ConfigStore:
        return ConfigStore(self.config_file)

    def client(self) -> OpenWebUIClient:
        connection = resolve_connection(
            self.store(), profile_name=self.profile, base_url=self.base_url
        )
        return OpenWebUIClient(connection)


@app.callback()
def root(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p", help="Named profile; overrides the active profile."),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help="Open WebUI URL; overrides profile and environment URL."),
    ] = None,
    config_file: Annotated[
        Path | None,
        typer.Option("--config", help="Alternative non-secret TOML profile file."),
    ] = None,
    compact: Annotated[
        bool, typer.Option("--compact", help="Emit compact JSON instead of indented JSON.")
    ] = False,
    version: Annotated[
        bool,
        typer.Option("--version", is_eager=True, help="Show the CLI version and exit."),
    ] = False,
) -> None:
    """Select a profile globally, then invoke a command group shown below."""

    if version:
        typer.echo(__version__)
        raise typer.Exit()
    ctx.obj = State(profile=profile, base_url=base_url, config_file=config_file, compact=compact)


@profile_app.command("list")
def profile_list(ctx: typer.Context) -> None:
    """List profiles and identify the active profile; no credential is displayed."""

    state = _state(ctx)
    config = state.store().load()
    emit(
        {
            "active_profile": config.active_profile,
            "profiles": [
                {
                    "name": item.name,
                    "base_url": item.normalized_url(),
                    "keyring_configured": bool(item.keyring_service and item.keyring_username),
                    "verify_ssl": item.verify_ssl,
                    "timeout": item.timeout,
                }
                for item in config.profiles.values()
            ],
        },
        compact=state.compact,
    )


@profile_app.command("show")
def profile_show(
    ctx: typer.Context,
    name: Annotated[
        str | None, typer.Argument(help="Profile name; defaults to the active profile.")
    ] = None,
) -> None:
    """Show one profile's non-secret connection metadata."""

    state = _state(ctx)
    config = state.store().load()
    selected = name or config.active_profile
    if not selected or selected not in config.profiles:
        _abort("No matching profile is configured.")
    item = config.profiles[selected]
    emit(
        {
            "name": item.name,
            "base_url": item.normalized_url(),
            "keyring_service": item.keyring_service,
            "keyring_username": item.keyring_username,
            "verify_ssl": item.verify_ssl,
            "timeout": item.timeout,
            "active": selected == config.active_profile,
        },
        compact=state.compact,
    )


@profile_app.command("set")
def profile_set(
    ctx: typer.Context,
    name: Annotated[str, typer.Argument(help="Profile name, for example 'production'.")],
    url: Annotated[str, typer.Option("--url", help="Open WebUI base URL.")],
    keyring_service: Annotated[
        str | None,
        typer.Option(help="OS keyring service name containing the API key."),
    ] = None,
    keyring_username: Annotated[
        str | None,
        typer.Option(help="OS keyring account name containing the API key."),
    ] = None,
    verify_ssl: Annotated[
        bool, typer.Option("--verify-ssl/--no-verify-ssl", help="Verify the HTTPS certificate.")
    ] = True,
    timeout: Annotated[float, typer.Option(min=0.1, help="Request timeout in seconds.")] = 30.0,
    activate: Annotated[
        bool, typer.Option("--activate", help="Make this the active profile.")
    ] = False,
) -> None:
    """Create or update a profile. This command never stores an API key."""

    state = _state(ctx)
    profile = Profile(
        name=name,
        base_url=url,
        keyring_service=keyring_service,
        keyring_username=keyring_username,
        verify_ssl=verify_ssl,
        timeout=timeout,
    )
    profile.normalized_url()
    config = state.store().upsert_profile(profile, activate=activate)
    emit(
        {"profile": name, "active_profile": config.active_profile, "saved": True},
        compact=state.compact,
    )


@profile_app.command("use")
def profile_use(
    ctx: typer.Context, name: Annotated[str, typer.Argument(help="Profile name.")]
) -> None:
    """Select the default profile used when --profile is omitted."""

    state = _state(ctx)
    config = state.store().activate(name)
    emit({"active_profile": config.active_profile}, compact=state.compact)


@auth_app.command("keyring-store")
def auth_keyring_store(
    ctx: typer.Context,
    profile_name: Annotated[
        str | None,
        typer.Option("--for-profile", help="Profile receiving the key; defaults to active."),
    ] = None,
) -> None:
    """Read an API key through hidden input and store it in the configured OS keyring."""

    state = _state(ctx)
    config = state.store().load()
    selected = profile_name or state.profile or config.active_profile
    if not selected or selected not in config.profiles:
        _abort("No matching profile is configured.")
    secret = typer.prompt("API key", hide_input=True, confirmation_prompt=True)
    try:
        store_profile_api_key(config.profiles[selected], secret)
    finally:
        secret = ""
    emit({"profile": selected, "stored": True}, compact=state.compact)


@auth_app.command("status")
def auth_status(ctx: typer.Context) -> None:
    """Verify authentication and display the associated account without showing its key."""

    state = _state(ctx)
    try:
        with state.client() as client:
            user = client.who_am_i()
    except OpenWebUIError as exc:
        _abort(str(exc))
    emit(
        {
            "authenticated": True,
            "user": {key: user.get(key) for key in ("id", "name", "email", "role")},
        },
        compact=state.compact,
    )


@system_config_app.command("get")
def system_config_get(
    ctx: typer.Context,
    key: Annotated[
        str | None,
        typer.Argument(help="Optional exact setting key, for example ENABLE_SIGNUP."),
    ] = None,
) -> None:
    """Read all system settings or one exact key. Requires an administrator API key."""

    state = _state(ctx)
    config = _get_system_config(state)
    if key is not None:
        if key not in config:
            _abort(f"Unknown system configuration key {key!r}.")
        config = {key: config[key]}
    emit(config, compact=state.compact)


@system_config_app.command("export")
def system_config_export(
    ctx: typer.Context,
    path: Annotated[Path, typer.Argument(help="Destination JSON file.")],
    force: Annotated[
        bool, typer.Option("--force", help="Replace an existing destination file.")
    ] = False,
) -> None:
    """Export the current complete system configuration to a JSON file."""

    state = _state(ctx)
    try:
        write_json_file(path, _get_system_config(state), force=force)
    except OpenWebUIError as exc:
        _abort(str(exc))
    emit({"exported": str(path)}, compact=state.compact)


@system_config_app.command("set")
def system_config_set(
    ctx: typer.Context,
    key: Annotated[str, typer.Argument(help="Exact setting key, for example ENABLE_SIGNUP.")],
    value: Annotated[
        str,
        typer.Argument(help="JSON value (true, 10, null, object) or an ordinary string."),
    ],
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Show the proposed change without applying it.")
    ] = False,
    yes: Annotated[
        bool, typer.Option("--yes", "-y", help="Apply without an interactive confirmation.")
    ] = False,
) -> None:
    """Patch one setting while preserving every other required system setting."""

    state = _state(ctx)
    _apply_system_patch(state, {key: parse_cli_value(value)}, dry_run=dry_run, yes=yes)


@system_config_app.command("apply")
def system_config_apply(
    ctx: typer.Context,
    path: Annotated[Path, typer.Argument(help="JSON object containing only keys to patch.")],
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Show proposed changes without applying them.")
    ] = False,
    yes: Annotated[
        bool, typer.Option("--yes", "-y", help="Apply without interactive confirmation.")
    ] = False,
) -> None:
    """Apply a partial JSON configuration patch after validating every key."""

    try:
        patch = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        _abort(f"Cannot read configuration patch {path}: {exc}")
    if not isinstance(patch, dict):
        _abort("The configuration patch must be a JSON object.")
    _apply_system_patch(_state(ctx), patch, dry_run=dry_run, yes=yes)


def _apply_system_patch(state: State, patch: dict[str, Any], *, dry_run: bool, yes: bool) -> None:
    try:
        with state.client() as client:
            current = client.get_system_config()
            unknown = sorted(set(patch) - set(current))
            if unknown:
                raise ValidationError(f"Unknown system configuration key(s): {', '.join(unknown)}")
            updated = {**current, **patch}
            changes = changes_between(current, updated)
            if not changes:
                emit({"applied": False, "changes": {}}, compact=state.compact)
                return
            if dry_run:
                emit({"applied": False, "dry_run": True, "changes": changes}, compact=state.compact)
                return
            if not yes and not typer.confirm("Apply these system configuration changes?"):
                raise typer.Abort()
            result = client.replace_system_config(updated)
    except OpenWebUIError as exc:
        _abort(str(exc))
    emit({"applied": True, "changes": changes, "configuration": result}, compact=state.compact)


def _get_system_config(state: State) -> dict[str, Any]:
    try:
        with state.client() as client:
            return client.get_system_config()
    except OpenWebUIError as exc:
        _abort(str(exc))


def _state(ctx: typer.Context) -> State:
    state = ctx.find_root().obj
    if not isinstance(state, State):
        raise RuntimeError("CLI state was not initialized")
    return state


def _abort(message: str) -> NoReturn:
    typer.echo(f"Error: {message}", err=True)
    raise typer.Exit(2)


if __name__ == "__main__":
    app()
