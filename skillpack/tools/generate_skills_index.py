#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.S)
KV_RE = re.compile(r"^(?P<k>[A-Za-z0-9_-]+)\s*:\s*(?P<v>.*)\s*$")


@dataclass(frozen=True)
class SkillInfo:
    name: str
    description: str
    skill_md: Path

    @property
    def folder(self) -> str:
        return self.skill_md.parent.name


def _read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def _parse_frontmatter(md: str) -> dict[str, str]:
    match = FRONTMATTER_RE.search(md)
    if not match:
        return {}

    out: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        km = KV_RE.match(line)
        if not km:
            continue
        key = km.group("k").strip()
        value = km.group("v").strip()
        if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
            value = value[1:-1]
        out[key] = value
    return out


def discover_skills(root: Path) -> list[SkillInfo]:
    skills: list[SkillInfo] = []
    for skill_md in sorted(root.rglob("SKILL.md")):
        md = _read_text(skill_md)
        fm = _parse_frontmatter(md)
        name = fm.get("name", "").strip()
        description = fm.get("description", "").strip()
        if not name or not description:
            continue
        skills.append(SkillInfo(name=name, description=description, skill_md=skill_md))
    return skills


def render_index(root: Path, skills: list[SkillInfo]) -> str:
    skills_sorted = sorted(skills, key=lambda s: s.name)
    mismatches = [s for s in skills_sorted if s.folder != s.name]

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines: list[str] = []
    lines.append("# Codex Skill Index (name → location)")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append("")
    lines.append(
        "This folder keeps **nested** skill sources, but Codex primarily keys on the `name:` in `SKILL.md` frontmatter. "
        "This index is the canonical mapping you maintain."
    )
    lines.append("")
    lines.append("## Inventory")
    lines.append(f"- Skills found: **{len(skills_sorted)}**")
    lines.append(f"- Folder/name mismatches: **{len(mismatches)}** (not necessarily broken, but harder to maintain)")
    lines.append("")
    lines.append("## Skills")
    lines.append("| name | description | location |")
    lines.append("|---|---|---|")
    for s in skills_sorted:
        desc = s.description.replace("\n", " ").replace("|", "\\|")
        rel = s.skill_md.relative_to(root).as_posix()
        lines.append(f"| `{s.name}` | {desc} | `{rel}` |")

    lines.append("")
    lines.append("## Folder/name mismatches")
    if not mismatches:
        lines.append("None.")
    else:
        lines.append("| folder | name | location |")
        lines.append("|---|---|---|")
        for s in mismatches:
            rel = s.skill_md.relative_to(root).as_posix()
            lines.append(f"| `{s.folder}` | `{s.name}` | `{rel}` |")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Codex-friendly skill name→path index for a skillpack.")
    parser.add_argument("--root", default=".", help="Root folder containing skills (default: current directory).")
    parser.add_argument("--out", default="skills-index.md", help="Output markdown file path (relative to root).")
    parser.add_argument("--fail-on-mismatch", action="store_true", help="Exit non-zero if folder != name for any skill.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = (root / args.out).resolve()

    skills = discover_skills(root)
    content = render_index(root, skills)
    # Write with UTF-8 BOM for Windows-friendly display
    out.write_bytes(b"\xef\xbb\xbf" + content.encode("utf-8"))

    mismatches = [s for s in skills if s.folder != s.name]
    print(f"Wrote: {out} ({len(skills)} skills, {len(mismatches)} mismatches)")

    if args.fail_on_mismatch and mismatches:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

