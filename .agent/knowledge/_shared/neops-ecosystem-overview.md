# Neops Ecosystem Overview

Neops is a network automation platform that abstracts imperative scripts into declarative YAML workflows composed of reusable, typed function blocks. It provides vendor-agnostic, transaction-safe, typed, and testable network automation.

## Value Proposition

- **Vendor-agnostic**: function blocks abstract device communication; workflows never reference vendor specifics
- **Transaction-safe**: workflows track pure/idempotent execution for safe retry/rollback classification
- **Typed**: FB inputs/outputs carry JSON schemas enforced at registration; the engine validates before execution
- **Testable**: FBs are pure Python functions testable in isolation; workflow YAML is schema-validated in CI

## Platform Components

| Component | Tech Stack | Purpose |
|---|---|---|
| **Workflow Engine** | NestJS, TypeScript, PostgreSQL (MikroORM), port 3030 | Orchestrates workflow execution, scheduling, blackboard job queue, REST API |
| **Worker SDK** | Python 3.12+, Pydantic, async/thread-pool hybrid | Write and run function blocks; auto-registers with engine |
| **CMS (neops-core)** | Django, GraphQL (graphene-django), PostgreSQL, Elasticsearch | Device inventory, facts, checks, configs, locking, permissions |
| **Remote Lab** | FastAPI, Netlab (Containerlab/libvirt) | On-demand network topologies for integration testing |
| **Monitor App** | SvelteKit (static build), bundled with engine repo | Lightweight dashboard for workflow management |
| **Web Client** | React/Next.js | Full user-facing UI (future) |
| **Gateways** | GraphQL gateway, REST gateway, secure gateway | Protocol adapters and auth |
| **Helm Charts** | Kubernetes | Production deployment manifests |

## Data Flow

```
User → API / Monitor App
  → Workflow Engine (validate, schedule, orchestrate)
    → Blackboard (job queue per execution)
      → Worker SDK (poll, execute function block)
        → Device (via connection proxy/plugin)
      → CMS (persist entity updates on unlock)
```

## Key Concepts

| Concept | Definition |
|---|---|
| **Workflow** | YAML document declaring ordered steps, each referencing a function block |
| **Function Block (FB)** | Named, versioned, typed Python unit registered with engine via Worker SDK |
| **Blackboard** | Job queue managed by the engine; workers poll for jobs, push results |
| **Context** | Runtime entity data (devices, interfaces, groups) injected into each FB call |
| **Seed Entity** | Starting entity type a workflow operates on: `device`, `interface`, `group`, `global` |
| **Acquire** | Pre-execution phase that locks entities and gathers data from CMS |
| **Pure** | FB with no side effects — failure always yields `FAILED_SAFE` |
| **Idempotent** | FB safe to re-execute — same inputs produce same outputs |

## Entity Model (CMS)

- **Device**: hostname, IP, credentials, platform, connection_state, facts (JSON), checks (JSON), configs
- **Interface**: name, device (FK), state (UP/DOWN/etc.), neighbor (self-ref), facts, checks
- **DeviceGroup**: name, devices (M2M), facts, checks
- **Facts/Checks**: Versioned key-value records, auto-aggregated into parent entity JSON fields

## Repository Locations

| Repo | Directory |
|---|---|
| Documentation mono-repo | `neops/` |
| Workflow Engine | `neops-workflow-engine/` |
| Worker SDK (Python) | `neops-worker-sdk-py/` |
| CMS | `neops-core/` |
| Remote Lab | `neops-remote-lab/` |
| Web Client | `neops-web-client/` |
| Helm Charts | `neops-helm/` |

## Implementation Status

For current implementation status of each component, see the respective project's `AGENTS.md` file. Key note: several workflow features are schema-defined but not yet implemented (workflowReference, continueOnError, retryConfig, auto-retry, rollback).
