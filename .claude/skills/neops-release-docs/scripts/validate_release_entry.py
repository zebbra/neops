#!/usr/bin/env python3
"""Validate a neops-web-client release documentation entry."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path to neops-web-client")
    parser.add_argument("--tag", required=True, help="Stable client tag, such as v4.1.0")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    entry = repo / "docs" / "releases" / f"{args.tag}.md"
    index = repo / "docs" / "releases" / "index.md"
    navigation = repo / "mkdocs_release_notes.yml"
    errors: list[str] = []

    for path in (entry, index, navigation):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(repo)}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    entry_text = entry.read_text()
    index_text = index.read_text()
    nav_text = navigation.read_text()

    version = args.tag.removeprefix("v")
    if not re.search(rf"^# .+{re.escape(version)}\s*$", entry_text, re.MULTILINE):
        errors.append(f"entry heading does not identify release {args.tag}")
    if args.tag not in index_text:
        errors.append(f"release index does not mention {args.tag}")
    if f"releases/{args.tag}.md" not in nav_text:
        errors.append(f"release navigation does not include releases/{args.tag}.md")
    if PLACEHOLDER.search(entry_text):
        errors.append("entry contains TODO, TBD, or FIXME placeholder text")
    if "\N{EM DASH}" in entry_text:
        errors.append("entry contains a Unicode em dash")

    for alt, raw_target in IMAGE.findall(entry_text):
        target = raw_target.split("#", 1)[0].split("?", 1)[0].strip()
        if target.startswith(("http://", "https://", "data:")):
            continue
        if not alt.strip():
            errors.append(f"image has empty alt text: {raw_target}")
        image_path = (entry.parent / target).resolve()
        try:
            image_path.relative_to(repo)
        except ValueError:
            errors.append(f"image resolves outside the repository: {raw_target}")
            continue
        if not image_path.is_file():
            errors.append(f"missing image: {image_path.relative_to(repo)}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Release documentation validation passed for {args.tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
