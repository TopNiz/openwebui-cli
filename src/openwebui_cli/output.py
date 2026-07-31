"""Machine-readable command output."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer

from openwebui_cli.exceptions import ValidationError


def emit(value: Any, *, compact: bool = False) -> None:
    """Write deterministic JSON to stdout."""

    typer.echo(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=None if compact else 2))


def write_json_file(path: Path, value: Any, *, force: bool = False) -> None:
    """Write JSON without silently overwriting an existing file."""

    if path.exists() and not force:
        raise ValidationError(
            f"Refusing to overwrite existing file {path}; pass --force to replace it."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
