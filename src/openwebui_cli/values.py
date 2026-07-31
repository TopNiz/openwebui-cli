"""JSON values, patches, and human-readable change descriptions."""

from __future__ import annotations

import json
from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from openwebui_cli.exceptions import ValidationError


def parse_cli_value(raw: str) -> Any:
    """Parse JSON scalars/objects/arrays, falling back to an ordinary string."""

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def changes_between(current: Mapping[str, Any], updated: Mapping[str, Any]) -> dict[str, Any]:
    """Return changed leaf paths with before/after values."""

    changes: dict[str, Any] = {}
    _collect_changes(current, updated, "", changes)
    return changes


def set_nested_value(
    document: Mapping[str, Any], path: str, value: Any, *, strict: bool = False
) -> dict[str, Any]:
    """Return a deep copy with one dot-delimited path replaced."""

    parts = path.split(".")
    if not path or any(not part for part in parts):
        raise ValidationError("A setting path must contain non-empty dot-delimited names.")
    result = deepcopy(dict(document))
    cursor: dict[str, Any] = result
    for part in parts[:-1]:
        if part not in cursor:
            if strict:
                raise ValidationError(f"Unknown setting path {path!r}.")
            cursor[part] = {}
        if not isinstance(cursor[part], dict):
            raise ValidationError(f"Setting path {path!r} crosses a non-object value.")
        cursor = cursor[part]
    if strict and parts[-1] not in cursor:
        raise ValidationError(f"Unknown setting path {path!r}.")
    cursor[parts[-1]] = value
    return result


def merge_nested(
    document: Mapping[str, Any], patch: Mapping[str, Any], *, strict: bool = False
) -> dict[str, Any]:
    """Recursively merge a partial object into a deep copy of a document."""

    result = deepcopy(dict(document))

    def merge(target: dict[str, Any], incoming: Mapping[str, Any], prefix: str) -> None:
        for key, value in incoming.items():
            path = f"{prefix}.{key}" if prefix else key
            if strict and key not in target:
                raise ValidationError(f"Unknown setting path {path!r}.")
            if isinstance(value, Mapping) and isinstance(target.get(key), dict):
                merge(target[key], value, path)
            elif isinstance(value, Mapping) and strict and key in target:
                raise ValidationError(f"Setting path {path!r} is not an object.")
            else:
                target[key] = deepcopy(value)

    merge(result, patch, "")
    return result


def _collect_changes(
    current: Mapping[str, Any], updated: Mapping[str, Any], prefix: str, output: dict[str, Any]
) -> None:
    for key in sorted(set(current) | set(updated)):
        path = f"{prefix}.{key}" if prefix else key
        before = current.get(key)
        after = updated.get(key)
        if isinstance(before, Mapping) and isinstance(after, Mapping):
            _collect_changes(before, after, path, output)
        elif before != after:
            output[path] = {"before": before, "after": after}
