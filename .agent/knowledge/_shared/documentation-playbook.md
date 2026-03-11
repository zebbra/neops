# Documentation Playbook

Guide for writing and maintaining documentation for any neops component. Applies to all repos.

## Personas

Four personas drive documentation decisions — see `documentation-personas.md` for full definitions (Sam, Priya, Marcus, Diana). Every doc page should serve at least two personas. Junior-friendly means layered, not dumbed-down.

## Documentation Stack

- **MkDocs** with **Material for MkDocs** theme
- Extensions: `pymdownx.superfences`, `pymdownx.snippets`, `pymdownx.tabbed`, `pymdownx.details`
- Diagrams: Mermaid (fenced code blocks)
- Multi-repo build: `neops/` mono-repo includes component repos as submodules via `mkdocs-monorepo-plugin`

## Writing Phases

### 1. Discovery
- Map existing docs: search for `*.md` files in `docs/` and review nav in `mkdocs_custom.yml`
- Read `.agent/knowledge/` files for context and gaps
- Check implementation status in source code before documenting features

### 2. Planning
- Decide audience (which personas). Outline sections — single responsibility per page.
- Identify code examples needed; find or create matching source files.

### 3. Example-First Writing
- Write or locate real code examples first (in `examples/` or source directories)
- Add snippet markers: `# --8<-- [start:name]` / `# --8<-- [end:name]`
- Run tests to verify examples work before writing prose

### 4. Writing Rules
- **Code >5 lines**: must use `--8<--` includes from real source files. Never inline large blocks.
- **Snippet paths**: relative to the markdown file, using symlinks in `docs/` (never `../../`)
- **Admonitions**: `!!!` (always open), `???` (collapsible). Use `!!! warning "Implementation Status"` for unimplemented features.
- **Tabs**: `=== "Tab Title"` for language/variant switches
- **Active voice, present tense, concise**: every sentence must earn its place
- **Layer difficulty**: basics in main text, advanced in collapsible admonitions

### 5. Implementation Status
Always add a warning for features not yet implemented:
```markdown
!!! warning "Implementation Status"
    This feature is planned but not yet implemented in the current release.
```
Never describe a feature without indicating its implementation status.

### 6. Cross-Project Integration
- Engine → SDK links: `/neops-worker-sdk-py/docs/...` (absolute paths)
- SDK → Engine links: `/neops-workflow-engine/docs/...` (absolute paths)
- These resolve in the unified MkDocs multi-repo build
- All getting-started examples use `fb.examples.neops.io` package
- Terminology must match across both projects' glossaries

### 7. QA
- `make validate-examples` — CI-validate workflow YAML
- `mkdocs serve` — verify all pages render, no broken includes
- Verify cross-project links resolve
- **Persona reviews**: launch parallel subagents (one per persona from `documentation-personas.md`). Each reads ALL docs pages and rates on 8 dimensions (0–10): Clarity, Completeness, Accuracy, Navigation, Progressive Disclosure, Cross-References, Implementation Status Honesty, Actionability. Compile into review findings.

### 8. Knowledge Capture
- Update `.agent/knowledge/` files with new findings
- Record gaps in project-specific audit files
- Update `missing-external-links.md` for unresolved cross-references

## Structure Template (Per Component)

```
docs/
  index.md                    # Overview, navigation cards, architecture diagram
  getting-started/
    10-setup.md               # Prerequisites, installation, hello world
    20-first-<concept>.md     # First hands-on tutorial
  10-concepts/                # Core concepts, increasing depth
  20-<primary-topic>/         # Main topic area
  30-<secondary-topic>/       # Secondary topic area
  50-deployment/              # Configuration, Docker, operations
  60-development/             # Internal/contributor docs (separate from user docs)
  99-appendix/                # Glossary, FAQ, schema reference
```

## Lessons Learned

- **Persona-driven design works**: reviews catch different issues per persona
- **Snippet includes prevent rot**: code in docs stays current with source
- **Implementation status honesty builds trust**: users appreciate knowing what's real vs. planned
- **Cross-project onboarding loop is critical**: engine getting-started links to SDK and vice versa
- **Avoid "Coming Soon" markers**: they rot. Use `!!! warning "Implementation Status"` instead.
- **Keep examples aligned**: FB package names, parameter names, and workflow references must match across repos
