#!/usr/bin/env python3
"""Normalize upstream Open WebUI OpenAPI output for deterministic code generation.

The raw specification is retained unchanged. This script only repairs structural
issues rejected by OpenAPI Generator: duplicate operation IDs and undeclared path
parameters.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
PATH_PARAMETER = re.compile(r"\{([^{}]+)\}")


def normalize(document: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    changes: list[str] = []
    seen_operation_ids: dict[str, tuple[str, str]] = {}

    for path in sorted(document.get("paths", {})):
        path_item = document["paths"][path]
        shared_parameters = path_item.setdefault("parameters", [])
        declared_shared = {
            parameter.get("name")
            for parameter in shared_parameters
            if parameter.get("in") == "path"
        }
        required_by_template = set(PATH_PARAMETER.findall(path))
        declared_by_any_operation = set(declared_shared)
        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if isinstance(operation, dict):
                declared_by_any_operation.update(
                    parameter.get("name")
                    for parameter in operation.get("parameters", [])
                    if parameter.get("in") == "path"
                )

        for name in sorted(required_by_template - declared_by_any_operation):
            shared_parameters.append(
                {
                    "name": name,
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                }
            )
            changes.append(f"declared missing path parameter {name!r} on {path}")

        if not shared_parameters:
            path_item.pop("parameters", None)

        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not operation_id:
                digest = hashlib.sha256(f"{method}:{path}".encode()).hexdigest()[:10]
                operation_id = f"operation_{method}_{digest}"
                operation["operationId"] = operation_id
                changes.append(f"created operationId {operation_id!r} for {method.upper()} {path}")

            if operation_id in seen_operation_ids:
                digest = hashlib.sha256(f"{method}:{path}".encode()).hexdigest()[:10]
                replacement = f"{operation_id}_{method}_{digest}"
                operation["operationId"] = replacement
                first_method, first_path = seen_operation_ids[operation_id]
                changes.append(
                    f"renamed duplicate operationId {operation_id!r} on "
                    f"{method.upper()} {path} to {replacement!r}; first used by "
                    f"{first_method.upper()} {first_path}"
                )
                seen_operation_ids[replacement] = (method, path)
            else:
                seen_operation_ids[operation_id] = (method, path)

    return document, changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Raw OpenAPI JSON document")
    parser.add_argument("output", type=Path, help="Normalized OpenAPI JSON document")
    parser.add_argument("--report", type=Path, help="Optional normalization report")
    args = parser.parse_args()

    document = json.loads(args.input.read_text())
    normalized, changes = normalize(document)
    args.output.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n")

    if args.report:
        lines = ["# OpenAPI normalization report", ""]
        lines.extend(f"- {change}" for change in changes)
        args.report.write_text("\n".join(lines) + "\n")

    print(f"Normalized OpenAPI document with {len(changes)} deterministic repair(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
