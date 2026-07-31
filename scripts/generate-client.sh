#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXPECTED_VERSION="$(tr -d '[:space:]' < "$ROOT/.openapi-generator-version")"

if ! command -v openapi-generator >/dev/null 2>&1; then
  printf '%s\n' "openapi-generator is required. Install version $EXPECTED_VERSION." >&2
  exit 1
fi

ACTUAL_VERSION="$(openapi-generator version 2>/dev/null | tail -1 | tr -d '[:space:]')"
if [[ "$ACTUAL_VERSION" != "$EXPECTED_VERSION" ]]; then
  printf '%s\n' "Expected openapi-generator $EXPECTED_VERSION, found $ACTUAL_VERSION." >&2
  exit 1
fi

cd "$ROOT"
python3 scripts/normalize-openapi.py \
  openapi/openapi.json \
  openapi/openapi.normalized.json \
  --report openapi/NORMALIZATION.md

openapi-generator validate -i openapi/openapi.normalized.json >/dev/null
openapi-generator generate \
  --config openapi-generator.yaml \
  --ignore-file-override openapi-generator-ignore \
  --global-property apiTests=false,modelTests=false

printf '%s\n' "Generated client and reference documentation in $ROOT/generated"
