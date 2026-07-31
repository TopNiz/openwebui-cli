#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/skills/openwebui-remote"
TARGET="${OPENWEBUI_SKILL_DIR:-$HOME/.agents/skills/openwebui-remote}"

if [[ -e "$TARGET" ]]; then
  printf '%s\n' "Refusing to overwrite existing skill path: $TARGET" >&2
  exit 1
fi

mkdir -p "$TARGET/references"
cp "$SOURCE/SKILL.md" "$TARGET/SKILL.md"
cp "$SOURCE/references/COMMANDS.md" "$TARGET/references/COMMANDS.md"

printf '%s\n' "Installed global skill at $TARGET"
