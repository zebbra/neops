# Cross-Project Patterns

Conventions for documentation, examples, and testing that span multiple neops repositories.

## Cross-Project URL Convention

Links between project docs use absolute paths rooted at the project directory:
- Engine → SDK: `/neops-worker-sdk-py/docs/...`
- SDK → Engine: `/neops-workflow-engine/docs/...`

These resolve in the unified MkDocs multi-repo build (the `neops/` mono-repo includes all component repos as submodules under `docs/`).

## Terminology Alignment

Canonical definitions for shared terms live in `neops-ecosystem-overview.md` (Key Concepts table). When adding a new term to one project's glossary, add it to all relevant projects. Terms MUST match across all glossaries.

## Example Alignment

- All getting-started examples use **`fb.examples.neops.io`** package
- Workflow YAML `name`, `package`, and `version` fields must match between engine and SDK examples
- Engine CI: `make validate-examples` validates YAML against JSON schema
- SDK CI: pytest validates FB signatures and test cases
- When updating an example in one repo, check the other repo and update accordingly

### Runnable vs. Illustrative Examples

- **Runnable**: `echo`, `show_version`, `ping`, `configBackup` have real SDK implementations
- **Illustrative**: intermediate/advanced workflow examples use hypothetical FB names to demonstrate patterns
- Always label clearly which examples are runnable and which are illustrative

## Implementation Status Sync

Both projects must agree on implementation status for shared features:
- If the engine marks a feature as unimplemented, SDK docs must not describe it as available
- Use identical admonition style: `!!! warning "Implementation Status"`
- Periodically audit cross-project status to catch drift

## Cross-Project Onboarding

Each project's Getting Started links to the other:
- Engine "Your First Workflow" → SDK "Write Your First Function Block"
- SDK "Your First Function Block" → Engine "Run Your First Workflow"

This creates a complete onboarding loop regardless of entry point.

## Testing Patterns

### Worker SDK Testing

Two test decorators:
- `@fb_test_case(description, params, context, succeeds, assertions)` — local tests with mocked context
- `@fb_test_case_with_lab(description, params, remote_lab_fixture, assertions)` — remote lab with real devices

Context factory: `create_workflow_context(run_on, entity_id, devices, device_groups, interfaces)`.

Available lab topologies: `simple_iol` (2 Cisco IOL), `simple_frr` (2 FRRouting).

### Workflow Engine Testing

- Unit tests: Jest (`npm run test`)
- E2E tests: Supertest + PostgreSQL (`npm run test:e2e`)
- Example validation: `make validate-examples` (JSON schema validation of all YAML examples)
- CI in Docker: multi-stage Dockerfile with `--target run-ci`

### Common Pitfalls

- Hyphenated directories (`examples/getting-started/`) can't be imported as Python packages — use `sys.path` manipulation
- `DeviceTypeDto.platform` must be a `PlatformTypeDto`, not a string
- Plugin imports register via decorators at import time — order matters
- Default pytest config excludes `function_block` marker; use `-m "function_block"` explicitly
