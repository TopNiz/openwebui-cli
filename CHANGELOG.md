# Changelog

All notable changes are documented here. The project follows semantic versioning after the initial proof-of-concept releases.

## 0.1.0a3 — 2026-08-04

### Changed

- Document GitHub-tagged `uv tool install` setup directly in the global Open WebUI remote-administration skill.

## 0.1.0a2 — 2026-07-31

### Fixed

- Include the upstream Open WebUI license and third-party notices inside wheel and source artifacts.

## 0.1.0a1 — 2026-07-31

### Added

- OpenAPI 3.1 description pinned from Open WebUI 0.11.0.
- Deterministic normalization and OpenAPI Generator 7.21.0 client generation.
- Complete asynchronous low-level `openwebui_client` package and generated API reference.
- Stable synchronous `OpenWebUIClient` administration facade.
- Named profiles with environment and operating-system keyring credential resolution.
- System configuration read, export, dry-run, and patch commands.
- User listing, lookup, creation, account update, and protected password-reset commands.
- Default-permission read, export, strict nested patch, and dry-run commands.
- Current-user settings read, export, nested patch, and dry-run commands.
- Comprehensive embedded help, README, CLI and Python API documentation.
- Global `openwebui-remote` Pi skill with read-before-write safety rules.
- Python 3.11–3.14 CI, linting, strict typing, tests, and package builds.

### Security

- Credentials are never accepted as ordinary CLI arguments.
- Profile files do not contain API keys.
- API errors redact the active credential.
- Account creation discards the JWT returned by Open WebUI.
- User output excludes embedded settings and OAuth data.

### Compatibility

- Validated against Open WebUI 0.11.0.
- Open WebUI's administrative API remains experimental; compatibility with other versions is not yet guaranteed.
