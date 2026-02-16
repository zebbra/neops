# Neops public facing Repository

This is the public facing repository for Neops.
This repository contains resources and documentation for Neops.

Neops represents a groundbreaking approach to network power that transcends traditional task automation.
It’s designed to enhance productivity, enabling you to focus on what you do best—your core competencies.
With Neops, you’ll experience a seamless integration of intelligent solutions that streamline operations
and free up your time for strategic initiatives.

## Writing documentation

- The main task in this repository is to write and manage documentation.
- Documentation is always in the 'docs' folder.

### Framework

- We use [mkdocs](https://www.mkdocs.org/) to write documentation.
- The documentation is written in markdown and styled with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
- We use the monorepo plugin to include the documentation in the main repository.
- Therefore, you are newer allowed to reference a file outside of the docs folder (i.e., do never use the dot-dot syntax like `../some-file.md` to reference a file in the main repository). 
- Always create, locate or symlink the file or ideally its containing folder in the docs folder and reference it from there.
- Most symlinks should be available automatically in the docs folder, so be sure to verify before you create something new.

### Documenting with code examples

- Code snippets longer than 5 lines should always be referenced from real code, ideally placed in an 'examples', 'snippets', 'use-cases' or 'getting-started' folder outside the docs .
- Do never write code examples inlined in the documentation.
- Always reference code examples using the superfences plugin

```yaml
markdown_extensions:
  - pymdownx.superfences
```

- if you want to include parts of a file in the markdown documentation, you can define a snippet like this (here, the snippet is called 'plugins':

```yaml
# --8<-- [start:plugins]
plugins:
  # Enables search
  - search
  # Allows to add a whole directory in the navigation instead of just files
  # Sub-nav items are automatically created if the provided dir contains subdirectories
  - include_dir_to_nav
# --8<-- [end:plugins]
```

- Then, you can reference it in markdown like this:

```markdown
### Include the entire content of the file

--8<-- "mkdocs_custom.yml"
```

```markdown
### Include only the snippet named 'plugins'

--8<-- "mkdocs_custom.yml:plugins"
```

### Documenting with diagrams

- Use [mermaid](https://mermaid-js.github.io/mermaid/#/) to create diagrams


### Handling tasks

- When prompted with a task, first determine if it belongs to this repository or a submodule of this repository.
- Then, read CONVENTIONS.md, AGENTS.md and existing documentation to get familiar with the context.
- Then, document according to the conventions of the submodule and the rules in this file.
- You can validate your documentation by running `make doc-build`, in the root repository (test overall documentation) and submodules (test specific documentation)
- Always validate your documentations after every change!!