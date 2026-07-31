# Open WebUI CLI

An unofficial, open-source Python client and command-line interface for administering and automating [Open WebUI](https://github.com/open-webui/open-webui).

> **Status:** pre-alpha proof of concept. The first milestone targets Open WebUI `0.11.0` and focuses on system configuration, user administration, and per-user settings.

## Goals

- provide an installable Python library for programmatic access;
- provide an `owui` CLI with complete embedded help;
- generate a comprehensive low-level client from Open WebUI's OpenAPI specification;
- add a stable, ergonomic high-level administration API;
- keep credentials out of source files, shell history, logs, and command output;
- support reusable profiles for multiple Open WebUI instances.

## Installation

Until the first package release, install directly from GitHub:

```bash
uv tool install git+https://github.com/TopNiz/openwebui-cli.git
# or
python -m pip install git+https://github.com/TopNiz/openwebui-cli.git
```

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
owui users ...             # Sprint 2
owui user-settings ...     # Sprint 2
```

Examples:

```bash
owui system config get
owui system config get ENABLE_SIGNUP
owui system config set ENABLE_SIGNUP false --dry-run
owui system config set ENABLE_SIGNUP false --yes
owui system config export system-config.json
```

Run `owui --help` and `<command> --help` for authoritative embedded documentation.

## Python library

```python
from openwebui_cli import ConfigStore, OpenWebUIClient, resolve_connection

connection = resolve_connection(ConfigStore())
with OpenWebUIClient(connection) as client:
    config = client.get_system_config()
```

The stable `OpenWebUIClient` facade covers supported workflows. The complete asynchronous `openwebui_client` package is generated from the pinned OpenAPI description for advanced endpoints; see [`generated/docs`](generated/docs) and [`docs/API-GENERATION.md`](docs/API-GENERATION.md).

Chat uses Open WebUI's OpenAI-compatible endpoint and standard SDK conventions. This administration CLI covers Open WebUI-specific APIs that are not part of the OpenAI protocol.

## Project plan

See [`docs/ROADMAP.md`](docs/ROADMAP.md). Work is tracked through GitHub issues and delivered through reviewed sprint pull requests.

## Security

Never place an API key in a command argument, committed configuration, issue, pull request, or log. See [`SECURITY.md`](SECURITY.md).

## Independence

This project is not affiliated with or endorsed by Open WebUI Inc. “Open WebUI” is used only to identify compatibility with the upstream software.

## License

Original project code is licensed under Apache-2.0. The captured OpenAPI description and generated artifacts derive from Open WebUI and retain the upstream notices described in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
