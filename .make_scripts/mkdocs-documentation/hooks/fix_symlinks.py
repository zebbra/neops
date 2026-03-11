import os
from pathlib import Path
from mkdocs.structure.files import Files

def on_files(files: Files, config):
    """
    Ensures Snippets can find files by adding the REAL repository root
    to the search paths, while fixing file-level symlinks.
    """
    # config['config_file_path'] is the path to your real mkdocs.yml
    project_root = Path(config['config_file_path']).parent.resolve()
    original_docs_dir = project_root / "docs"

    if os.environ.get('DEBUG') == 'true':
        print(f"[Symlink Hook] Project Root: {project_root}")
        print(f"[Symlink Hook] Original Docs Dir: {original_docs_dir}")

    # 2. Inject search paths for the Snippets extension
    _add_to_snippets_config(config, str(project_root))
    _add_to_snippets_config(config, str(original_docs_dir))

    # 3. Add each included submodule's root and docs dir so that snippets
    #    using repo-relative paths (e.g. "examples/hello.yaml") resolve
    #    correctly when the submodule is composed into the mono-repo.
    for child in sorted(original_docs_dir.iterdir()):
        if child.is_dir() and (child / "mkdocs_custom.yml").exists():
            _add_to_snippets_config(config, str(child.resolve()))
            child_docs = child / "docs"
            if child_docs.is_dir():
                _add_to_snippets_config(config, str(child_docs.resolve()))
            if os.environ.get('DEBUG') == 'true':
                print(f"[Symlink Hook] Added submodule snippet paths: {child.name}")

    for file in files:
        # Reconstruct path in real repo
        original_path = original_docs_dir / file.src_path

        if original_path.is_symlink():
            resolved_target = original_path.resolve().absolute()

            if not resolved_target.exists():
                print(f"[Symlink Hook] WARNING: Broken link ignored: {file.src_path}")
                continue

            if resolved_target.is_file():
                # Fix individual file symlinks
                file.abs_src_path = str(resolved_target)
                if os.environ.get('DEBUG') == 'true':
                    print(f"[Symlink Hook] Resolved File: {file.src_path} -> {file.abs_src_path}")

            elif resolved_target.is_dir():
                # For directory symlinks (like doc_assets), we keep them in
                # the list so the path remains valid for Snippets, but we
                # neuter the copy command to prevent IsADirectoryError.
                file.abs_src_path = str(resolved_target)
                file.copy_file = lambda dirty=False: None

                # Add the specific resolved target as well
                _add_to_snippets_config(config, str(resolved_target))
                if os.environ.get('DEBUG') == 'true':
                    print(f"[Symlink Hook] Mapped Directory Prefix: {file.src_path} -> {resolved_target}")

    return files

def _add_to_snippets_config(config, path):
    """Injects a search path into the pymdownx.snippets configuration"""
    mdx_configs = config.setdefault('mdx_configs', {})
    snippets_conf = mdx_configs.setdefault('pymdownx.snippets', {})
    base_paths = snippets_conf.get('base_path', [])

    if isinstance(base_paths, str):
        base_paths = [base_paths]

    if path not in base_paths:
        base_paths.append(path)

    snippets_conf['base_path'] = base_paths