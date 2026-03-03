# Neops Documentation Mono-Repo

Central documentation repository for the neops network automation platform. Aggregates documentation from all component repos via git submodules and builds a unified MkDocs site.

## Tech Stack

- **Docs**: MkDocs with Material for MkDocs theme
- **Build**: Makefile-driven, monorepo plugin for multi-repo nav
- **Submodules**: Component repos included under `docs/` for unified build
- **Deployment**: Static site generation

## Architecture

This repo does not contain application code. It serves as the documentation hub:
1. Component repos (workflow-engine, worker-sdk, etc.) are git submodules under `docs/`
2. Each component's `mkdocs_custom.yml` defines its own nav structure
3. The root `mkdocs.yml` (auto-generated) includes all component navs via `!include`
4. Hooks in `.make_scripts/` handle symlink fixing and nav inclusion

## Development

```bash
git submodule update --init --recursive    # Initialize submodules
make doc-serve                              # Build and serve docs locally
make scan_docs                              # Check docs compliance (no ../ links, no inline code)
```

## Project Structure

```
docs/
  neops-workflow-engine/     Git submodule → workflow engine repo
  neops-worker-sdk-py/       Git submodule → worker SDK repo
  neops-remote-lab/          Git submodule → remote lab repo
  neops-web-client/          Git submodule → web client repo
  neops-secure-gateway/      Git submodule → secure gateway repo
  override/                  MkDocs theme overrides
mkdocs.yml                   Auto-generated (DO NOT EDIT)
mkdocs_custom.yml            Custom MkDocs configuration
.make_scripts/               Build scripts and hooks
```

## Conventions

- Never edit `mkdocs.yml` directly — edit `mkdocs_custom.yml` instead
- Cross-project links use absolute paths: `/neops-workflow-engine/docs/...`, `/neops-worker-sdk-py/docs/...`
- Component docs are written in their own repos, not here
- This repo holds only shared configuration, theme overrides, and build tooling

## Neops Ecosystem

This is the top-level repo that ties all documentation together. For the full platform overview, see `.agent/knowledge/_shared/neops-ecosystem-overview.md`.

## AI Agent Guidance

- The main task in this repo is managing the documentation build and cross-project integration
- Do NOT write component documentation here — write it in the component repos
- Shared knowledge: `.agent/knowledge/_shared/` (identical across all neops repos)
- Project-specific knowledge: `.agent/knowledge/` root (review findings)
- Submodules may not be initialized — run `git submodule update --init --recursive` first
- `mkdocs.yml` is auto-generated — NEVER edit it directly; use `mkdocs_custom.yml` instead

### Knowledge File Index

| Task | Read |
|---|---|
| How neops components interact | `_shared/neops-ecosystem-overview.md` |
| Architecture details for any component | `_shared/component-architectures.md` |
| Writing documentation for any component | `_shared/documentation-playbook.md` |
| Cross-project conventions and testing | `_shared/cross-project-patterns.md` |
| Setting up AI knowledge in a new repo | `_shared/ai-knowledge-base-guide.md` |
| Review scores and improvement ideas | `documentation-review-findings.md` |
