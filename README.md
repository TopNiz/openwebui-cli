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

## Initial command scope

```text
owui system config ...
owui users ...
owui user-settings ...
owui auth ...
```

Chat will use Open WebUI's OpenAI-compatible endpoint and standard SDK conventions. The administration CLI covers Open WebUI-specific APIs that are not part of the OpenAI protocol.

## Project plan

See [`docs/ROADMAP.md`](docs/ROADMAP.md). Work is tracked through GitHub issues and delivered through reviewed sprint pull requests.

## Security

Never place an API key in a command argument, committed configuration, issue, pull request, or log. See [`SECURITY.md`](SECURITY.md).

## Independence

This project is not affiliated with or endorsed by Open WebUI Inc. “Open WebUI” is used only to identify compatibility with the upstream software.

## License

Original project code is licensed under Apache-2.0. The captured OpenAPI description and generated artifacts derive from Open WebUI and retain the upstream notices described in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
