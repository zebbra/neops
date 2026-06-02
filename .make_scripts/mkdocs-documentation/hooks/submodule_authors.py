"""Backfill submodule git authorship and dates into mkdocs-document-dates.

Why this exists
---------------

The `mkdocs-document-dates` plugin gathers authors and timestamps by running
`git log` once from the parent docs_dir. It does not recurse into git
submodules, so for any documentation page that lives under a submodule
working tree (a separate git repo) the lookup returns nothing. The plugin
then falls back to the file's mtime + the local user's home-directory name —
i.e. a generic "leandro" / "ubuntu" / "ci" instead of the real authors.

This hook closes that gap.

How it works
------------

It is registered in `mkdocs_base.yml` and runs at `on_files` priority -50,
which is after `mkdocs-document-dates`'s own `on_files` (priority +50)
populates its `data_cached`. Then:

  1. Reads `.gitmodules` at the project root to find each submodule's
     working-tree path.
  2. Per submodule, runs one `git log` for `*.md` using the same flags as
     the plugin (`--use-mailmap`, `--reverse`, `--no-merges`,
     `%aN|%aE|%at`).
  3. If the project root has a `.mailmap`, also passes
     `-c mailmap.file=<root>/.mailmap` so the parent repo's identity rules
     apply inside each submodule (each submodule has its own git history
     but typically no mailmap of its own).
  4. For every file under a submodule path, writes the resulting
     `created` / `updated` / `authors` into the plugin's
     `data_cached[src_uri]`.

The plugin's `on_page_markdown` then reads the cache as usual and renders
real authorship and dates for submodule pages.

Limitations
-----------

The single `git log -- '*.md'` query does not follow renames. Authors of a
file's pre-rename path won't surface under its current path. If that
matters, replace the batch query with a per-file `git log --follow`.

No-op when the project has no submodules.
"""

from __future__ import annotations

import configparser
import logging
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from mkdocs.plugins import event_priority

logger = logging.getLogger("mkdocs.hooks.submodule_authors")


def _read_submodule_paths(repo_root: Path) -> list[Path]:
    gitmodules = repo_root / ".gitmodules"
    if not gitmodules.exists():
        return []
    cp = configparser.ConfigParser()
    try:
        cp.read(gitmodules)
    except configparser.Error as e:
        logger.warning("Cannot parse .gitmodules: %s", e)
        return []
    paths: list[Path] = []
    for section in cp.sections():
        path = cp.get(section, "path", fallback=None)
        if path:
            abs_path = (repo_root / path).resolve()
            if abs_path.is_dir():
                paths.append(abs_path)
    return paths


def _load_submodule_metadata(
    submodule_root: Path, mailmap_file: Path | None = None
) -> dict[str, dict]:
    """Return {rel_path_in_submodule: {created, updated, authors}}."""
    cmd: list[str] = ["git"]
    if mailmap_file is not None and mailmap_file.exists():
        cmd += ["-c", f"mailmap.file={mailmap_file}"]
    cmd += [
        "-c", "core.quotepath=false",
        "log", "--reverse", "--no-merges", "--use-mailmap",
        "--name-only", "--format=%aN|%aE|%at",
        "--", "*.md",
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=submodule_root,
            capture_output=True,
            encoding="utf-8",
        )
    except OSError as e:
        logger.warning("git log failed in %s: %s", submodule_root, e)
        return {}
    if proc.returncode != 0:
        return {}

    authors_dict: dict[str, dict[tuple[str, str], None]] = defaultdict(dict)
    first_commit: dict[str, int] = {}
    last_commit: dict[str, int] = {}
    current_commit: tuple[str, str, str] | None = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if "|" in line:
            parts = line.split("|", 2)
            if len(parts) == 3:
                current_commit = (parts[0], parts[1], parts[2])
        elif line.endswith(".md") and current_commit is not None:
            name, email, ts_str = current_commit
            ts = int(ts_str)
            authors_dict[line].setdefault((name, email), None)
            first_commit.setdefault(line, ts)
            last_commit[line] = ts  # --reverse is ascending; last seen is latest

    out: dict[str, dict] = {}
    for path, created_ts in first_commit.items():
        out[path] = {
            "created": datetime.fromtimestamp(created_ts, tz=timezone.utc),
            "updated": datetime.fromtimestamp(last_commit[path], tz=timezone.utc),
            "authors": [
                {"name": name, "email": email}
                for (name, email) in authors_dict[path].keys()
            ],
        }
    return out


def _is_inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


@event_priority(-50)
def on_files(files, config):
    plugin = config.plugins.get("document-dates")
    if plugin is None or not hasattr(plugin, "data_cached"):
        return files

    config_path = Path(config["config_file_path"]).resolve()
    repo_root = config_path.parent
    submodule_paths = _read_submodule_paths(repo_root)
    if not submodule_paths:
        return files

    parent_mailmap = repo_root / ".mailmap"

    sub_meta_cache: dict[Path, dict[str, dict]] = {}
    backfilled = 0

    for f in files:
        if not f.src_path.endswith(".md"):
            continue
        if not f.abs_src_path:
            continue
        abs_src = Path(f.abs_src_path).resolve()

        owner = next(
            (sp for sp in submodule_paths if _is_inside(abs_src, sp)),
            None,
        )
        if owner is None:
            continue

        if owner not in sub_meta_cache:
            sub_meta_cache[owner] = _load_submodule_metadata(owner, parent_mailmap)

        rel_to_sub = abs_src.relative_to(owner).as_posix()
        info = sub_meta_cache[owner].get(rel_to_sub)
        if not info:
            continue

        entry = plugin.data_cached.setdefault(f.src_uri, {})
        entry["created"] = info["created"]
        entry["updated"] = info["updated"]
        entry["authors"] = info["authors"]
        backfilled += 1

    if backfilled:
        logger.info(
            "submodule_authors: backfilled git authorship for %d submodule pages",
            backfilled,
        )
    return files
