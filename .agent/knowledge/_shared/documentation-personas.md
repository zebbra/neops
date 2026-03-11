# Documentation Personas

Reusable persona definitions for reviewing and writing neops documentation.

## Sam — Junior Network Engineer

- **Experience**: 2 years in network operations
- **Skills**: Python basics, YAML from Ansible playbooks, CLI comfort. No typed Python (Pydantic, dataclasses) or TypeScript.
- **Mindset**: Eager to learn, needs hand-holding, appreciates fun and approachable tools
- **Reading pattern**: Getting Started → Concepts → Workflows. Skips architecture docs initially.
- **Success criteria**: Can run a hello-world workflow end-to-end within 30 minutes following only the docs

## Priya — Senior Network Engineer

- **Experience**: 15+ years across multi-vendor environments
- **Skills**: Expert in Ansible, Nornir, custom Python tooling, NETCONF/YANG. Familiar with CI/CD.
- **Mindset**: Critical, pragmatic, demands clear ROI before adopting a new tool
- **Reading pattern**: Architecture and Concepts first, then advanced features (acquire, retry, rollback). Compares with existing tools.
- **Success criteria**: Understands why neops is better than Ansible/Nornir for transaction-safe multi-device automation

## Marcus — Implementation Wizard

- **Experience**: Staff-level engineer, modern Python and TypeScript fluency
- **Skills**: Pydantic, NestJS, gRPC, MikroORM. Reads source when docs fall short.
- **Mindset**: Demands precision, completeness, and internal consistency. Notices mismatched types, missing edge cases.
- **Reading pattern**: Source-level docs, extension points, schema references first. Tutorials only if they show non-obvious patterns.
- **Success criteria**: Can extend neops with a custom handler, gateway, or FB type without asking questions

## Diana — Technical Writer (Meta-Reviewer)

- **Experience**: Multi-product technical documentation across developer platforms
- **Skills**: Evaluates structure, maintainability, audience awareness, cross-project consistency
- **Mindset**: Documentation as product. Cares about navigation, progressive disclosure, long-term maintainability.
- **Reading pattern**: Full nav structure review, then spot-checks for consistency, voice, completeness.
- **Success criteria**: Docs are navigable, internally consistent, each page serves a clear audience

For the persona review process, see `documentation-playbook.md` (QA phase).
