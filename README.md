# Open WebUI CLI

An unofficial, open-source Python client and command-line interface for administering and automating [Open WebUI](https://github.com/open-webui/open-webui).

> **Status:** alpha proof of concept. Release `0.1.0a3` targets Open WebUI `0.11.0` and focuses on system configuration, user administration, permissions, and per-user settings.

## Goals

- provide an installable Python library for programmatic access;
- provide an `owui` CLI with complete embedded help;
- generate a comprehensive low-level client from Open WebUI's OpenAPI specification;
- add a stable, ergonomic high-level administration API;
- keep credentials out of source files, shell history, logs, and command output;
- support reusable profiles for multiple Open WebUI instances.

## Installation

Install the CLI and module from the tagged GitHub release/source:

```bash
uv tool install 'git+https://github.com/TopNiz/openwebui-cli.git@v0.1.0a3'
# or
python -m pip install 'git+https://github.com/TopNiz/openwebui-cli.git@v0.1.0a3'
```

Wheel and source artifacts are also attached to the GitHub pre-release. PyPI publication is intentionally deferred until trusted publishing is configured.

For development:

```bash
git clone https://github.com/TopNiz/openwebui-cli.git
cd openwebui-cli
uv sync --extra dev
uv run owui --help
```

## Secure configuration

Create a named profile containing only non-secret connection metadata:

```bash
owui profile set demo \
  --url https://openwebui.example.org \
  --keyring-service openwebui-cli-demo \
  --keyring-username "$USER" \
  --activate
owui auth keyring-store
owui auth status
```

`auth keyring-store` reads the key through hidden input. Alternatively, provide `OPENWEBUI_BASE_URL` and `OPENWEBUI_API_KEY` to the process environment. Never put a key in a command argument or committed file.

## Initial command scope

```text
owui profile ...
owui auth ...
owui system config ...
owui users ...
owui permissions ...
owui user-settings ...
```

Examples:

```bash
owui system config get
owui system config get ENABLE_SIGNUP
owui system config set ENABLE_SIGNUP false --dry-run
owui system config set ENABLE_SIGNUP false --yes
owui system config export system-config.json

owui users list
owui users get user@example.org
owui users create "Example User" user@example.org
owui users update user@example.org --role user
owui users reset-password user@example.org

owui permissions get
owui permissions set features.api_keys false --dry-run
owui user-settings set ui.language nl --dry-run
```

Creation and password-reset commands read passwords through a hidden prompt by default. For automation, use `--password-stdin` and pipe directly from a protected secret source; never place a password in a command argument.

Run `owui --help` and `<command> --help` for authoritative embedded documentation. See the complete [`CLI reference`](docs/CLI.md).

## Python library

```python
from openwebui_cli import ConfigStore, OpenWebUIClient, resolve_connection

connection = resolve_connection(ConfigStore())
with OpenWebUIClient(connection) as client:
    config = client.get_system_config()
```

The stable `OpenWebUIClient` facade covers supported workflows. The complete asynchronous `openwebui_client` package is generated from the pinned OpenAPI description for advanced endpoints; see [`generated/docs`](generated/docs) and [`docs/API-GENERATION.md`](docs/API-GENERATION.md).

Chat uses Open WebUI's OpenAI-compatible endpoint and standard SDK conventions. This administration CLI covers Open WebUI-specific APIs that are not part of the OpenAI protocol.

## Global Pi skill

The repository includes `skills/openwebui-remote`, a safety-focused global skill for remote Open WebUI administration. Install it once with:

```bash
./scripts/install-global-skill.sh
```

The installer refuses to overwrite an existing global skill. Restart or reload the agent harness after installation so it rediscovers the skill.

## Project plan and compatibility

See [`docs/ROADMAP.md`](docs/ROADMAP.md), [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md), and [`CHANGELOG.md`](CHANGELOG.md). Work is tracked through GitHub issues and delivered through reviewed sprint pull requests.

## Security

Never place an API key in a command argument, committed configuration, issue, pull request, or log. See [`SECURITY.md`](SECURITY.md).

## Independence

This project is not affiliated with or endorsed by Open WebUI Inc. “Open WebUI” is used only to identify compatibility with the upstream software.

## License

Original project code is licensed under Apache-2.0. The captured OpenAPI description and generated artifacts derive from Open WebUI and retain the upstream notices described in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
