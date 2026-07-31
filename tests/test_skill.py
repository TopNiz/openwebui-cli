from __future__ import annotations

import re
from pathlib import Path

SKILL = Path(__file__).parents[1] / "skills" / "openwebui-remote" / "SKILL.md"


def test_global_skill_has_valid_frontmatter_and_safety_guidance() -> None:
    text = SKILL.read_text()
    assert text.startswith("---\n")
    frontmatter = text.split("---\n", 2)[1]
    name = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

    assert name and name.group(1) == "openwebui-remote"
    assert description and len(description.group(1)) <= 1024
    assert "explicit confirmation" in text
    assert "--dry-run" in text
    assert "Never print" in text
    assert "--api-key" not in text
