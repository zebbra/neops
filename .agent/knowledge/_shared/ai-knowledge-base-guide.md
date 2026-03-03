# AI Knowledge Base Architecture Guide

How to set up, maintain, and extend the neops AI knowledge base for effective AI-assisted development.

## Architecture Overview

The knowledge base follows Anthropic's context engineering principles: token efficiency, progressive disclosure, and graceful degradation. Every file must justify its existence by providing high-signal context that agents cannot infer from code alone.

### File Structure (Per Repository)

```
AGENTS.md                          # Universal AI context (~100 lines, always loaded)
CLAUDE.md                          # Claude Code pointer to AGENTS.md
.cursor/rules/                     # Cursor-specific rules with glob matching
  project-context.mdc              # Always-on project context
  documentation-writing.mdc        # Triggered when editing docs/**
.agent/knowledge/
  _shared/                         # Shared across all neops repos (future: neops-ai-context submodule)
    neops-ecosystem-overview.md    # Platform overview, components, data flow
    component-architectures.md     # All component architectures in one file
    documentation-playbook.md      # How to write docs for any neops component
    documentation-personas.md      # Review persona definitions
    cross-project-patterns.md      # Cross-repo conventions, testing patterns
    ai-knowledge-base-guide.md    # This file
  <project-specific files>         # Unique to each repo (audits, link tracking, etc.)
```

### Design Principles

1. **Progressive disclosure**: AGENTS.md gives enough context for any agent to start working. Deeper knowledge is discovered on-demand when agents explore `.agent/knowledge/`.
2. **Token efficiency**: ~570 lines across 6 shared files (down from 1400+ across 12+ duplicated files). No filler, no redundancy with linter/CI enforcement.
3. **Single source of truth**: `_shared/` files are identical across all repos. Future plan: extract to `neops-ai-context` repo as git submodule at `.agent/shared/`.
4. **Graceful degradation**: If an agent only reads AGENTS.md, it can still function. If `_shared/` isn't available, project-specific files and AGENTS.md provide sufficient context.
5. **Agent-agnostic**: Works with Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, and any tool that reads markdown files from the repo.

### Root File Strategy

| File | Purpose | Loaded by |
|---|---|---|
| `AGENTS.md` | Primary AI context (vendor-neutral, AGENTS.md open standard) | Cursor, Copilot, Codex, Gemini CLI, Claude Code |
| `CLAUDE.md` | Pointer to AGENTS.md + Claude-specific notes | Claude Code |
| `.cursor/rules/*.mdc` | Glob-matched rules (e.g., docs/** triggers writing conventions) | Cursor only |

## Maintenance Guidelines

### When to Update

- **After implementing a new feature**: update component-architectures.md and AGENTS.md
- **After writing documentation**: update project-specific audit files
- **After discovering implementation gaps**: update ecosystem overview's status section
- **After establishing new conventions**: update documentation-playbook.md or cross-project-patterns.md
- **After a persona review round**: update documentation-personas.md if review process changed

### How to Keep Shared Files in Sync

Until the `neops-ai-context` repo exists, shared files must be manually kept identical:

1. Edit the file in one repo
2. Copy to the other two repos: `cp neops-workflow-engine/.agent/knowledge/_shared/file.md neops-worker-sdk-py/.agent/knowledge/_shared/file.md`
3. Commit in all repos referencing the same change

Future: `neops-ai-context` repo as submodule at `.agent/shared/` eliminates manual sync.

### What Goes Where

| Content Type | Location |
|---|---|
| Ecosystem-wide knowledge | `_shared/` |
| Component architecture details | `_shared/component-architectures.md` |
| Project-specific doc audit | Project root `.agent/knowledge/` |
| Project-specific link tracking | Project root `.agent/knowledge/` |
| Review findings | Project root `.agent/knowledge/` |

## Bootstrapping a New Neops Component

### Prompt Template

Use this prompt with any AI coding agent to bootstrap knowledge files for a new neops component repository:

---

**Prompt for AI agents:**

> You are setting up AI knowledge files for the `{REPO_NAME}` repository, a component of the neops network automation platform.
>
> **Step 1: Copy shared knowledge**
> Copy all files from an existing neops repo's `.agent/knowledge/_shared/` directory to this repo's `.agent/knowledge/_shared/`. These files contain ecosystem-wide context that must be identical across all repos.
>
> **Step 2: Create AGENTS.md**
> Create an `AGENTS.md` at the repo root following this structure (~100-120 lines):
> - Overview (3-4 sentences about this specific component)
> - Tech Stack (bullet list)
> - Architecture (key concepts and data flow, brief)
> - Development (build, test, lint commands — copy from README or Makefile)
> - Project Structure (key directories with one-line descriptions)
> - Conventions (coding style, naming patterns, import rules)
> - Neops Ecosystem (brief context, ~20 lines, pointer to `.agent/knowledge/_shared/`)
> - AI Agent Guidance (how agents should approach work in this repo)
>
> **Step 3: Create CLAUDE.md**
> Create a `CLAUDE.md` with: "See AGENTS.md for full project context. For deeper knowledge, explore .agent/knowledge/."
>
> **Step 4: Create .cursor/rules/**
> Create `.cursor/rules/project-context.mdc` (alwaysApply: true) with project-specific context.
> If the repo has documentation, create `.cursor/rules/documentation-writing.mdc` (globs: docs/**) with writing conventions.
>
> **Step 5: Create project-specific knowledge**
> Explore the codebase and create project-specific knowledge files in `.agent/knowledge/`:
> - `{repo-name}-docs-audit.md` (if docs exist: structure, quality, gaps)
> - `missing-external-links.md` (cross-project links that need resolution)
>
> **Step 6: Verify**
> - Ensure `_shared/` files are byte-identical to other repos (use `diff` to confirm)
> - Verify commands in AGENTS.md Development section actually run successfully
> - Verify Project Structure section matches the filesystem (`ls -la`)
> - Verify configuration table matches actual environment variables in source code
> - Ensure .cursor/rules/ glob patterns match actual directory names (e.g., `docs/**` not `documentation/**`)
> - Ensure .cursor/rules/ don't duplicate content already in AGENTS.md
>
> **Fallback for Step 1**: If no other neops repo is available locally, clone any neops component repo
> and copy its `_shared/` directory. The canonical files are kept in sync across all repos.

---

### Checklist for New Component

- [ ] `.agent/knowledge/_shared/` contains all 6 shared files (identical to other repos)
- [ ] `AGENTS.md` exists at repo root with accurate project context
- [ ] `CLAUDE.md` exists at repo root pointing to AGENTS.md
- [ ] `.cursor/rules/project-context.mdc` exists with project-specific context
- [ ] `.cursor/rules/documentation-writing.mdc` exists if repo has docs
- [ ] Project-specific knowledge files created in `.agent/knowledge/`
- [ ] `.gitignore` does NOT exclude `.cursor/` (rules should be committed)

## Future: neops-ai-context Repository

Planned: extract `_shared/` to a dedicated `neops-ai-context` git submodule at `.agent/shared/` in each repo, eliminating manual sync. The current structure is designed for trivial extraction.
