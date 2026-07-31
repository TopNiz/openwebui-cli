# CLI reference

`owui` emits JSON so its output can be read by humans, shell tools, and automation. Use `--compact` for one-line JSON. Global options must precede the command group.

```text
owui [--profile NAME] [--base-url URL] [--config FILE] [--compact] COMMAND
```

No command accepts an API key or password as a command-line value.

## Profiles

```text
owui profile list
owui profile show [NAME]
owui profile set NAME --url URL [OPTIONS]
owui profile use NAME
```

Profiles store only URL, TLS, timeout, and keyring lookup metadata. They never store the API key.

## Authentication

```text
owui auth keyring-store [--for-profile NAME]
owui auth status
```

`keyring-store` uses hidden, confirmed input. `status` verifies the credential and returns only account identity fields.

## System configuration

```text
owui system config get [KEY]
owui system config export FILE [--force]
owui system config set KEY VALUE [--dry-run] [--yes]
owui system config apply FILE [--dry-run] [--yes]
```

Open WebUI requires the complete administrator configuration when updating it. The CLI therefore fetches the current object, validates patch keys, merges changes, and sends the complete object. `apply` accepts a partial top-level JSON object.

## Users

```text
owui users list [--query TEXT] [--page N] [--order-by FIELD] [--direction asc|desc]
owui users get USER_ID_OR_EMAIL
owui users create NAME EMAIL [--role pending|user|admin] [--password-stdin] [--yes]
owui users update USER_ID_OR_EMAIL [--name NAME] [--email EMAIL] [--role ROLE] [--profile-image-url URL] [--yes]
owui users reset-password USER_ID_OR_EMAIL [--password-stdin] [--yes]
```

User output is sanitized: passwords, returned session tokens, embedded settings, and OAuth data are omitted. Open WebUI returns a JWT when an administrator creates a user; the high-level client discards it before returning.

By default, password operations use a hidden prompt with confirmation. `--password-stdin` reads exactly one line for integration with a secret manager. Do not use `echo` or a literal password in a shell pipeline.

## Default permissions

```text
owui permissions get
owui permissions export FILE [--force]
owui permissions set DOT.PATH VALUE [--dry-run] [--yes]
owui permissions apply FILE [--dry-run] [--yes]
```

Permission changes use strict paths: misspelled or unknown paths are rejected. Open WebUI permissions are additive, so review the complete effective permission model before granting access.

## Current-user settings

```text
owui user-settings get
owui user-settings export FILE [--force]
owui user-settings set DOT.PATH VALUE [--dry-run] [--yes]
owui user-settings apply FILE [--dry-run] [--yes]
```

These commands affect only the account owning the active API key. Nested paths preserve unrelated settings. Arbitrary user-setting keys are allowed because Open WebUI's user-settings schema is extensible.

## Values

Values are parsed as JSON when valid:

- `true`, `false`, `null` become JSON scalars;
- `10` becomes a number;
- `{"key":"value"}` and `[1,2]` become objects/arrays;
- unquoted text such as `nl` remains a string.

## Automation safety

- Use `--dry-run` to inspect a change.
- Mutations prompt unless `--yes` is supplied.
- Use a separate least-privilege Open WebUI service account per application.
- Never put an administrator key in browser or mobile application code.
- Capture structured output, but do not enable HTTP debug logging around credentials.

Every command and subcommand has embedded help:

```bash
owui --help
owui users create --help
owui permissions set --help
```
