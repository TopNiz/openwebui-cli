from __future__ import annotations

import pytest

from openwebui_cli.exceptions import ValidationError
from openwebui_cli.values import changes_between, merge_nested, set_nested_value


def test_set_nested_value_preserves_unrelated_values() -> None:
    source = {"ui": {"theme": "dark", "language": "fr"}}

    updated = set_nested_value(source, "ui.theme", "light")

    assert updated == {"ui": {"theme": "light", "language": "fr"}}
    assert source["ui"]["theme"] == "dark"
    assert changes_between(source, updated) == {"ui.theme": {"before": "dark", "after": "light"}}


def test_strict_nested_patch_rejects_unknown_path() -> None:
    with pytest.raises(ValidationError, match="Unknown setting path"):
        set_nested_value({"features": {"api_keys": False}}, "features.unknown", True, strict=True)


def test_recursive_merge_can_add_user_setting() -> None:
    updated = merge_nested({"ui": {"theme": "dark"}}, {"ui": {"language": "nl"}})

    assert updated == {"ui": {"theme": "dark", "language": "nl"}}
