"""High-level Python interface for Open WebUI administration."""

from openwebui_cli.client import OpenWebUIClient
from openwebui_cli.config import ConfigStore, Profile, ResolvedConnection, resolve_connection
from openwebui_cli.version import __version__

__all__ = [
    "ConfigStore",
    "OpenWebUIClient",
    "Profile",
    "ResolvedConnection",
    "resolve_connection",
    "__version__",
]
