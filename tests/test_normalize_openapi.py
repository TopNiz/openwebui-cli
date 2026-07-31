from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).parents[1] / "scripts" / "normalize-openapi.py"
spec = importlib.util.spec_from_file_location("normalize_openapi", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
normalize = module.normalize


def test_normalization_repairs_duplicate_ids_and_missing_parameters() -> None:
    document: dict[str, Any] = {
        "openapi": "3.1.0",
        "paths": {
            "/one/{id}": {"get": {"operationId": "duplicate"}},
            "/two/{name}": {"post": {"operationId": "duplicate"}},
        },
    }

    normalized, changes = normalize(document)

    second = normalized["paths"]["/two/{name}"]
    assert second["post"]["operationId"].startswith("duplicate_post_")
    assert second["parameters"][0]["name"] == "name"
    assert len(changes) == 3
