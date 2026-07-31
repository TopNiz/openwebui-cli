from __future__ import annotations

from importlib.resources import files


def test_upstream_license_and_notices_are_packaged() -> None:
    licenses = files("openwebui_cli") / "licenses"
    upstream = (licenses / "OPEN_WEBUI_LICENSE").read_text()
    notices = (licenses / "THIRD_PARTY_NOTICES.md").read_text()

    assert "Open WebUI License" in upstream
    assert "Copyright (c) 2023- Open WebUI Inc." in upstream
    assert "OpenAPI description" in notices
    assert "not affiliated with or endorsed" in notices
