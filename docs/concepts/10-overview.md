# System overview

A workflow run has two sides: **what you author and trigger** (a workflow definition plus an execution payload) and **what happens at runtime** (the engine, CMS, blackboard, and a pool of workers).
The two diagrams below cover each side in turn — start with the first to see what the platform asks you to write, then read the second to see what it does with it.

## 1. Authoring and triggering

A workflow definition is an ordered list of versioned function-block references — no Python, no host configuration, no scheduling logic.
To run one, a caller posts an execution payload that names the workflow and the entities to operate on; the engine takes it from there.

```mermaid
flowchart LR
    classDef blueBox fill:#4a9af8,stroke:#333,stroke-width:1px,color:#fff

    subgraph Definition["<b>Workflow Definition</b><br/>SwiNOG/pos-migration:1"]
        direction TB
        a["fb.neops.io/fetch_config:1"] --> b["fb.neops.io/pre_check:1"]
        b --> c["fb.neops.io/migrate:1"]
        c --> d["fb.neops.io/post_check:1"]
    end

    Payload["<b>Execution Payload</b><br/>workflow: SwiNOG/pos-migration:1<br/>parameters: { … }<br/>executeOn: groupIds=[42]"]

    Engine["Neops Workflow Engine"]:::blueBox

    Definition -- "register" --> Engine
    Payload -- "execute" --> Engine
```

## 2. Runtime architecture

When the engine receives an execution payload it acquires entity locks from the CMS, posts jobs to the blackboard, and waits for workers to pick them up.
Each worker advertises the function-block versions it implements, so several versions can coexist during a rolling upgrade without taking the engine down.

```mermaid
flowchart LR
    classDef blueBox fill:#4a9af8,stroke:#333,stroke-width:1px,color:#fff
    classDef db fill:#4a9af8,stroke:#333,stroke-width:1px

    CMS["Neops CMS<br/>(entities & facts)"]:::blueBox
    CMSDB[( )]:::db
    CMS --- CMSDB

    Engine["Neops Workflow Engine"]:::blueBox
    EngineDB[( )]:::db
    Engine --- EngineDB

    BB["Blackboard<br/>(Jobs: D1, D2, …)"]:::blueBox

    subgraph Workers["Workers"]
        direction TB
        W1A["Worker 1 · Zone A<br/>fetch_config:1.0.0<br/>pre_check:1.0.0"]:::blueBox
        W1B["Worker 1 · Zone B<br/>fetch_config:1.0.0<br/>pre_check:1.0.0"]:::blueBox
        W2B["Worker 2 · Zone B<br/>migrate:1.0.0<br/>post_check:1.0.0"]:::blueBox
        W3B["Worker 3 · Zone B<br/>migrate:2.0.0<br/>post_check:2.0.0"]:::blueBox
    end

    CMS <-->|"1. lock & context"| Engine
    Engine <-->|"2. jobs · results"| BB
    BB <-->|"poll · run · return"| W1A
    BB <--> W1B
    BB <--> W2B
    BB <--> W3B
```

## What to notice

- **The engine acquires entities before any worker runs.**
  Locking is centralized at the CMS, not distributed across workers, so a single workflow run sees a consistent snapshot.
- **The blackboard decouples the engine from worker placement.**
  Workers poll for jobs they can handle; the engine never knows or cares which physical worker runs a given step.
- **Workers can advertise different function-block versions.**
  Worker 2 runs `migrate:1.0.0` alongside Worker 3 on `migrate:2.0.0` — this is how rolling upgrades work without engine downtime.

## See also

- [How Neops operates](20-how-neops-operates.md) — sequence diagrams for the read path, write path, and full execution flow.
- [Workflow Engine concepts](../neops-workflow-engine/docs/10-concepts/index.md) — definitions, transactions, blackboard, execution model.
