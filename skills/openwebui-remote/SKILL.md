---
name: openwebui-remote
description: Remotely inspect and administer Open WebUI through the public owui Python CLI. Use for system configuration, user accounts, default permissions, current-user settings, API authentication checks, and headless Open WebUI administration. Enforces read-before-write, dry runs, explicit confirmation, least privilege, and strict credential hygiene.
allowed-tools: Bash(owui:*)
---

# Open WebUI Remote Control

Use the `owui` CLI as the supported administration layer. Prefer its stable commands over hand-written HTTP calls or generated operation names.

## Safety rules

1. Never print, log, request in chat, or pass an API key, JWT, password, cookie, or secret as a command argument.
2. Use a named profile backed by the operating-system keyring. `OPENWEBUI_API_KEY` is allowed only when injected securely into the process environment.
3. Treat reads as the default. Before every mutation, inspect current state and run the corresponding `--dry-run` command when available.
4. Show the user the non-secret proposed changes and obtain explicit confirmation immediately before applying them with `--yes`.
5. After a mutation, read the affected resource again and verify the expected result.
6. Never use a shared administrator key in browser or mobile code. Use one least-privilege service account per application.
7. Do not invoke undocumented destructive generated-client operations without a reviewed plan and explicit user consent.
8. Minimize personal data in chat output. Summarize user-list results instead of reproducing unnecessary names or email addresses.

## Prerequisite check

```bash
command -v owui >/dev/null && owui --version
owui profile list
```

If `owui` is unavailable, follow the installation section in the project README. Do not silently install or reconfigure software unless the user requested it.

## Select and verify a profile

```bash
owui --profile <profile> auth status
```

This displays account identity but never the key. If no profile exists, create only non-secret metadata and let the user store the key through hidden input:

```bash
owui profile set <profile> \
  --url https://openwebui.example.org \
  --keyring-service <service> \
  --keyring-username <account> \
  --activate
owui auth keyring-store --for-profile <profile>
```

Never invent keyring identifiers when an existing organizational convention may apply; ask first.

## Read system settings

```bash
owui --profile <profile> system config get
owui --profile <profile> system config get ENABLE_API_KEYS
```

For a change, always dry-run first:

```bash
owui --profile <profile> system config set ENABLE_SIGNUP false --dry-run
```

After explicit confirmation:

```bash
owui --profile <profile> system config set ENABLE_SIGNUP false --yes
owui --profile <profile> system config get ENABLE_SIGNUP
```

## Manage users

Read operations:

```bash
owui --profile <profile> users list
owui --profile <profile> users get <user-id-or-email>
```

Account creation and password reset use hidden input by default. Ask the user to complete that protected prompt. For non-interactive automation, `--password-stdin` may receive input directly from an approved secret manager; never use `echo`, a literal value, or a temporary plaintext file.

Privilege changes and password resets require explicit confirmation. The CLI discards session tokens returned by account creation.

## Manage default permissions

```bash
owui --profile <profile> permissions get
owui --profile <profile> permissions set features.api_keys false --dry-run
```

Open WebUI permissions are additive. Review the whole permission document and relevant groups before granting access. Apply only after confirmation, then verify:

```bash
owui --profile <profile> permissions set features.api_keys false --yes
owui --profile <profile> permissions get
```

## Manage current-user settings

These settings belong only to the account owning the selected API key:

```bash
owui --profile <profile> user-settings get
owui --profile <profile> user-settings set ui.language nl --dry-run
```

Apply only after confirmation and verify the affected path.

## Discover commands

Use embedded help instead of guessing flags or payloads:

```bash
owui --help
owui <group> --help
owui <group> <command> --help
```

See `references/COMMANDS.md` for the supported command map and escalation guidance.
