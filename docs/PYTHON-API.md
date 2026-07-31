# High-level Python API

The `openwebui_cli` package provides stable synchronous workflows. The generated `openwebui_client` package provides version-specific asynchronous access to every endpoint.

## Resolve a configured connection

```python
from openwebui_cli import ConfigStore, OpenWebUIClient, resolve_connection

connection = resolve_connection(ConfigStore())
with OpenWebUIClient(connection) as client:
    identity = client.who_am_i()
```

`ResolvedConnection` excludes its credential from `repr`. Do not serialize the object.

## System settings

```python
with OpenWebUIClient(connection) as client:
    current = client.get_system_config()
    updated = client.patch_system_config({"ENABLE_SIGNUP": False})
```

`patch_system_config` validates keys, preserves unrelated fields, and submits the complete schema required by Open WebUI.

## User administration

```python
with OpenWebUIClient(connection) as client:
    page = client.list_users(query="example.org")
    user = client.create_user(
        name="Example User",
        email="user@example.org",
        password=password_from_a_secret_manager,
        role="user",
    )
    user = client.update_user(user["id"], {"role": "pending"})
```

The caller owns password collection and disposal. `create_user` discards the session token returned by Open WebUI and returns only sanitized account metadata.

## Permissions and current-user settings

```python
with OpenWebUIClient(connection) as client:
    permissions = client.get_default_permissions()
    settings = client.get_user_settings()
    settings["ui"] = {**settings.get("ui", {}), "language": "nl"}
    client.replace_user_settings(settings)
```

Replacement methods expect complete documents. CLI patch commands provide safe nested-merge convenience.

## Errors

- `ConfigurationError`: URL, profile, or keyring resolution problem;
- `ValidationError`: invalid local request rejected before network activity;
- `APIError`: timeout, connectivity failure, malformed response, or HTTP error.

API errors redact the active credential and do not include authorization headers.
