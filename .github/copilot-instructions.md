# Neops Documentation Mono-Repo Context

- MkDocs with Material for MkDocs theme, monorepo plugin
- Component repos are git submodules under `docs/`
- NEVER edit `mkdocs.yml` — it's auto-generated. Edit `mkdocs_custom.yml` instead.
- See AGENTS.md at repo root for full project context
- Shared ecosystem knowledge: `.agent/knowledge/_shared/`
- After changes: `make doc-serve` to verify docs build and render
