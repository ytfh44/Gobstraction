#!/usr/bin/env python3
"""Minimal structural validator for the Gobstraction Agent Skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[A-Za-z0-9-]+$")
EXPECTED = {
    "gobstraction",
    "gobstraction-audit",
    "gobstraction-delete",
    "gobstraction-merge",
    "gobstraction-split",
    "gobstraction-contain",
    "gobstraction-zero",
    "gobstraction-ground",
    "gobstraction-compose",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing YAML frontmatter closer")
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"unsupported frontmatter line: {raw!r}")
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data


def main() -> int:
    errors: list[str] = []
    found = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    if found != EXPECTED:
        errors.append(f"skill set mismatch: expected {sorted(EXPECTED)}, found {sorted(found)}")

    for name in sorted(found):
        path = SKILLS / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            fm = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
            continue

        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name must equal directory name")
        if not NAME_RE.fullmatch(fm.get("name", "")):
            errors.append(f"{name}: invalid skill name")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{name}: missing description")
        if not desc.startswith("Use when"):
            errors.append(f"{name}: description should start with 'Use when'")
        if len(desc) > 500:
            errors.append(f"{name}: description exceeds 500 characters")
        if len(text.split("\n---\n", 1)[0]) > 1024:
            errors.append(f"{name}: frontmatter exceeds 1024 characters")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(found)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
