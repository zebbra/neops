# How Neops operates

Neops separates data management from workflow execution. The CMS is the source of truth
for entity data, while the workflow engine orchestrates changes as workflows and
persists execution state. Workers run the actual function blocks and communicate
through the blackboard, which is the engine's job queue.

The blackboard is implemented inside the workflow engine (database tables + REST
endpoints). Workers poll it for jobs and push results back.

## Core components

- User: Reads entity data and triggers workflows.
- neops-cms: Stores entities and exposes them via APIs.
- neops-workflow-engine: Orchestrates workflows and manages execution state.
- neops-blackboard: The job queue used by the engine and workers.
- neops-worker: Executes function blocks and reports results.
- database: Persists workflow executions, jobs, and results.

## Overview: Read path (User ↔ CMS)

```mermaid
sequenceDiagram
    actor User
    participant CMS as neops-cms

    User->>CMS: Read entities & facts
    CMS-->>User: Entity data
```

## Overview: Write path (Workflow execution)

```mermaid
sequenceDiagram
    actor User
    participant CMS as neops-cms
    participant Engine as neops-workflow-engine

    User->>Engine: Execute workflow
    Engine->>CMS: Acquire entities & lock
    CMS-->>Engine: Locked entity data
    Engine->>CMS: Apply entity updates
```

## Execution flow (Engine, Blackboard, Worker)

```mermaid
sequenceDiagram
    actor User
    participant CMS as neops-cms
    participant Engine as neops-workflow-engine
    participant BB as neops-blackboard
    participant Worker as neops-worker

    User->>CMS: Read entities & facts
    CMS-->>User: Entity data

    User->>Engine: Create/update workflows<br/>Execute workflow
    Engine->>CMS: Acquire entities & lock
    CMS-->>Engine: Locked entity data
    Engine->>BB: Create jobs for steps

    Worker->>BB: Poll for jobs
    BB-->>Worker: Assign job
    Worker->>BB: Push results

    BB-->>Engine: Job results
    Engine->>CMS: Apply entity updates
```

## See also

- [System overview](10-overview.md) — the same architecture as a single dataflow diagram.
- [Workflows as transactions](../neops-workflow-engine/docs/10-concepts/40-workflow-as-a-transaction.md) — what locking, atomic updates, and failure classification actually guarantee.
