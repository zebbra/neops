#!/usr/bin/env python3
"""Collect deterministic git and dependency context for a client release."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


STABLE_TAG = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
FALLBACK_SDK_PACKAGES = {
    "@zebbra/ngx-jsonforms-carbon",
    "@zebbra/ngx-neops-app-components",
    "@zebbra/ngx-neops-app-services",
    "@zebbra/ngx-neops-client",
    "@zebbra/ngx-neops-icons",
    "@zebbra/ngx-neops-sdk-artifacts",
    "@zebbra/ngx-neops-storage-client",
}


class ContextError(RuntimeError):
    pass


def run_git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise ContextError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def semver_key(tag: str) -> tuple[int, int, int]:
    match = STABLE_TAG.fullmatch(tag)
    if not match:
        raise ContextError(f"Not a stable release tag: {tag}")
    return tuple(int(part) for part in match.groups())


def stable_tags(repo: Path, merged_ref: str) -> list[str]:
    tags = run_git(repo, "tag", "--merged", merged_ref, "--list").splitlines()
    return sorted((tag for tag in tags if STABLE_TAG.fullmatch(tag)), key=semver_key)


def file_at_ref(repo: Path, ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{ref}:{path}"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout if result.returncode == 0 else None


def dependencies_at_ref(repo: Path, ref: str) -> dict[str, str]:
    raw = file_at_ref(repo, ref, "package.json")
    if raw is None:
        return {}
    package = json.loads(raw)
    dependencies: dict[str, str] = {}
    for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        dependencies.update(package.get(section, {}))
    return dependencies


def discover_sdk_packages(sdk_repo: Path | None) -> tuple[set[str], str | None]:
    if sdk_repo is None or not (sdk_repo / ".git").exists():
        return FALLBACK_SDK_PACKAGES, None

    package = json.loads((sdk_repo / "package.json").read_text())
    dependencies = package.get("dependencies", {})
    names = {
        name
        for name, value in dependencies.items()
        if name.startswith("@zebbra/") and isinstance(value, str) and value.startswith("file:projects/")
    }
    return names or FALLBACK_SDK_PACKAGES, str(sdk_repo.resolve())


def changed_dependencies(before: dict[str, str], after: dict[str, str]) -> list[dict[str, str | None]]:
    changes: list[dict[str, str | None]] = []
    for name in sorted(set(before) | set(after)):
        old = before.get(name)
        new = after.get(name)
        if old != new:
            changes.append({"name": name, "from": old, "to": new})
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path to neops-web-client")
    parser.add_argument("--tag", help="Stable client tag to document")
    parser.add_argument("--sdk-repo", help="Path to neops-web-sdk")
    parser.add_argument("--docs-dir", default="docs/releases", help="Release entry directory")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists():
        raise ContextError(f"Not a git checkout: {repo}")

    run_git(repo, "rev-parse", "--verify", "HEAD")
    tags = stable_tags(repo, "HEAD")
    if not tags:
        raise ContextError("No stable release tags are reachable from HEAD")

    docs_dir = repo / args.docs_dir
    if args.tag:
        target = args.tag
        semver_key(target)
        run_git(repo, "rev-parse", "--verify", f"refs/tags/{target}")
    else:
        target = tags[-1]
        if (docs_dir / f"{target}.md").exists():
            raise ContextError(f"The newest stable tag {target} already has a release entry")

    target_key = semver_key(target)
    ancestors = []
    for tag in tags:
        if tag == target or semver_key(tag) >= target_key:
            continue
        result = subprocess.run(
            ["git", "-C", str(repo), "merge-base", "--is-ancestor", tag, target],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            ancestors.append(tag)
    previous = ancestors[-1] if ancestors else None
    range_spec = f"{previous}..{target}" if previous else target

    before = dependencies_at_ref(repo, previous) if previous else {}
    after = dependencies_at_ref(repo, target)
    dependency_changes = changed_dependencies(before, after)

    if args.sdk_repo:
        sdk_repo = Path(args.sdk_repo).resolve()
    else:
        candidate = repo.parent / "neops-web-sdk"
        sdk_repo = candidate if candidate.exists() else None
    sdk_packages, resolved_sdk_repo = discover_sdk_packages(sdk_repo)

    sdk_changes = [change for change in dependency_changes if change["name"] in sdk_packages]
    zebbra_changes = [change for change in dependency_changes if change["name"].startswith("@zebbra/")]
    sdk_from_versions = sorted({change["from"] for change in sdk_changes if change["from"]})
    sdk_to_versions = sorted({change["to"] for change in sdk_changes if change["to"]})

    commits = []
    for line in run_git(repo, "log", "--format=%H%x09%s", range_spec).splitlines():
        if not line:
            continue
        commit, _, subject = line.partition("\t")
        commits.append({"commit": commit, "subject": subject})

    if previous:
        changed_files = run_git(repo, "diff", "--name-only", range_spec).splitlines()
    else:
        changed_files = run_git(repo, "ls-tree", "-r", "--name-only", target).splitlines()
    target_commit = run_git(repo, "rev-list", "-n", "1", target)
    release_date = run_git(
        repo,
        "for-each-ref",
        "--format=%(taggerdate:short)",
        f"refs/tags/{target}",
    ) or run_git(repo, "log", "-1", "--format=%cs", target)

    output: dict[str, Any] = {
        "repository": str(repo),
        "target_tag": target,
        "target_commit": target_commit,
        "release_date": release_date,
        "previous_tag": previous,
        "range": range_spec,
        "docs_entry": str(docs_dir / f"{target}.md"),
        "docs_entry_exists": (docs_dir / f"{target}.md").exists(),
        "commits": commits,
        "changed_files": changed_files,
        "dependency_changes": dependency_changes,
        "zebbra_dependency_changes": zebbra_changes,
        "sdk_dependency_changes": sdk_changes,
        "sdk_version_range": {"from": sdk_from_versions, "to": sdk_to_versions},
        "sdk_package_source": resolved_sdk_repo or "built-in fallback list",
    }
    print(json.dumps(output, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ContextError, json.JSONDecodeError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
