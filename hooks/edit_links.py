"""Point the "edit this page" button of submodule pages somewhere that works.

`edit_uri` resolves every page against this repository, but submodule pages
exist here only as a gitlink, so their edit links 404. Pages from a public
submodule edit the file in that repository instead. Pages from a private one
open an issue on this public repository, since readers cannot see the source.
Pages of this repository keep the default link.

Submodules come from `.gitmodules`; only visibility is listed here, because it
is not recorded anywhere in the checkout. Anything not listed counts as private.
"""

from __future__ import annotations

import configparser
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import urlencode

PUBLIC_SUBMODULE_REPOS = {
    "https://github.com/zebbra/neops-remote-lab",
    "https://github.com/zebbra/neops-lab",
}
DEFAULT_SUBMODULE_BRANCH = "develop"


@dataclass(frozen=True)
class Submodule:
    docs_prefix: PurePosixPath
    root: Path
    repo_url: str
    branch: str

    @property
    def is_public(self) -> bool:
        return self.repo_url in PUBLIC_SUBMODULE_REPOS


_submodules: list[Submodule] = []


def on_config(config):
    repo_root = Path(config["config_file_path"]).resolve().parent
    docs_dir = Path(config["docs_dir"]).resolve()
    _submodules[:] = _read_submodules(repo_root, docs_dir)
    return config


def on_page_context(context, page, config, nav):
    submodule = _owning_submodule(page.file.src_uri)
    if submodule is None:
        return context
    if submodule.is_public:
        page.edit_url = _submodule_edit_url(submodule, page.file)
    else:
        page.edit_url = _issue_url(config["repo_url"], page)
    return context


def _read_submodules(repo_root: Path, docs_dir: Path) -> list[Submodule]:
    gitmodules = configparser.ConfigParser()
    gitmodules.read(repo_root / ".gitmodules")
    submodules = []
    for section in gitmodules.sections():
        root = (repo_root / gitmodules.get(section, "path")).resolve()
        if not root.is_relative_to(docs_dir):
            continue
        submodules.append(
            Submodule(
                docs_prefix=PurePosixPath(root.relative_to(docs_dir).as_posix()),
                root=root,
                repo_url=gitmodules.get(section, "url").removesuffix(".git"),
                branch=gitmodules.get(section, "branch", fallback=DEFAULT_SUBMODULE_BRANCH),
            )
        )
    return submodules


def _owning_submodule(src_uri: str) -> Submodule | None:
    path = PurePosixPath(src_uri)
    return next((s for s in _submodules if path.is_relative_to(s.docs_prefix)), None)


def _submodule_edit_url(submodule: Submodule, file) -> str:
    return f"{submodule.repo_url}/edit/{submodule.branch}/{_path_in_submodule(submodule, file)}"


def _path_in_submodule(submodule: Submodule, file) -> str:
    source = Path(file.abs_src_path).resolve()
    if source.is_relative_to(submodule.root):
        return source.relative_to(submodule.root).as_posix()
    return PurePosixPath(file.src_uri).relative_to(submodule.docs_prefix).as_posix()


def _issue_url(repo_url: str, page) -> str:
    query = urlencode(
        {
            "title": f"Docs: {page.title}",
            "body": f"Page: /{page.url}\nSource: {page.file.src_uri}\n\nWhat should change?\n",
        }
    )
    return f"{repo_url.rstrip('/')}/issues/new?{query}"
