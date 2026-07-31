#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

./scripts/generate-client.sh

if ! git diff --quiet -- generated openapi/openapi.normalized.json openapi/NORMALIZATION.md; then
  printf '%s\n' 'Generated client drift detected. Run scripts/generate-client.sh and commit the result.' >&2
  git diff --stat -- generated openapi/openapi.normalized.json openapi/NORMALIZATION.md >&2
  exit 1
fi

printf '%s\n' 'Generated client is up to date.'
