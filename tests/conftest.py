from __future__ import annotations

import os

import pytest


@pytest.fixture(autouse=True)
def isolate_openwebui_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Prevent developer-machine profiles or credentials from affecting tests."""

    for name in (
        "OPENWEBUI_PROFILE",
        "OPENWEBUI_BASE_URL",
        "OPENWEBUI_API_KEY",
        "OPENWEBUI_CONFIG",
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("PYTHONUTF8", os.environ.get("PYTHONUTF8", "1"))
