"""JSON values, patches, and human-readable change descriptions."""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any


def parse_cli_value(raw: str) -> Any:
    """Parse JSON scalars/objects/arrays, falling back to an ordinary string."""

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def changes_between(current: Mapping[str, Any], updated: Mapping[str, Any]) -> dict[str, Any]:
    """Return only changed keys with before/after values."""

    return {
        key: {"before": current.get(key), "after": updated.get(key)}
        for key in sorted(set(current) | set(updated))
        if current.get(key) != updated.get(key)
    }
