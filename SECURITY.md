# Security policy

## Reporting a vulnerability

Do not open a public issue containing exploit details, credentials, personal data, or sensitive deployment information. Use GitHub's private vulnerability reporting feature for this repository.

## Credential handling

- Prefer an operating-system keyring or the `OPENWEBUI_API_KEY` process environment variable.
- Never pass an API key as a CLI argument: arguments can be retained in shell history and process listings.
- Never store API keys in repository files or ordinary profile configuration.
- The CLI must never print, log, partially reveal, or serialize an API key.
- Use separate Open WebUI service accounts and keys for separate applications.
- Do not embed an administrator key in browser or mobile application code.

## Deployment guidance

Open WebUI's Swagger and OpenAPI routes require `ENV=dev`. Development mode is suitable for a proof of concept, but it exposes additional documentation routes. Restore production mode and review endpoint restrictions before production use.

## Supported versions

Until the first stable release, security and compatibility fixes target the Open WebUI version pinned in `openapi/source.json`.
