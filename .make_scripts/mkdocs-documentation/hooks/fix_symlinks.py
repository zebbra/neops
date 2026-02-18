import os
from pathlib import Path
from mkdocs.structure.files import Files

def on_files(files: Files, config):
    """
    Final Monorepo Fix:
    1. Reconstructs docs_dir dynamically from config.
    2. Resolves symlinks at any depth.
    3. Injects the REAL repo paths into Snippets so they work in /tmp.
    """
    # config['config_file_path'] is the absolute path to your real mkdocs.yml
    conf_path = Path(config['config_file_path']).resolve()
    project_root = conf_path.parent

    # Dynamically get docs_dir (e.g., 'docs') and anchor it to the real project root
    raw_docs_dir = config.get('docs_dir', 'docs')
    original_docs_dir = (project_root / raw_docs_dir).resolve()

    # 1. Inject the Master Search Paths into Snippets
    # This allows Snippets to find files even when building in /tmp
    _add_to_snippets_config(config, str(project_root))
    _add_to_snippets_config(config, str(original_docs_dir))

    for file in files:
        # Reconstruct where the file lives in the ACTUAL repository
        # This works for submodules because file.src_path is relative to the docs root
        original_path = original_docs_dir / file.src_path

        if original_path.is_symlink():
            resolved_target = original_path.resolve().absolute()

            if not resolved_target.exists():
                continue

            if resolved_target.is_file():
                file.abs_src_path = str(resolved_target)

            elif resolved_target.is_dir():
                # For directory symlinks (like doc_assets)
                file.abs_src_path = str(resolved_target)

                # NEUTER the copy command to prevent IsADirectoryError
                file.copy_file = lambda dirty=False: None

                # Add this specific resolved folder to Snippets search paths
                _add_to_snippets_config(config, str(resolved_target))

                print(f"[Symlink Hook] Fixed Dir: {file.src_path} -> {resolved_target}")

    return files

def _add_to_snippets_config(config, path):
    """Safely injects search paths into pymdownx.snippets"""
    mdx_configs = config.setdefault('mdx_configs', {})
    snippets_conf = mdx_configs.setdefault('pymdownx.snippets', {})
    base_paths = snippets_conf.get('base_path', [])

    if isinstance(base_paths, str):
        base_paths = [base_paths]

    if path not in base_paths:
        base_paths.append(path)

    snippets_conf['base_path'] = base_paths