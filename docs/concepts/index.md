# Concepts

These pages explain the cross-cutting ideas behind Neops — how a workflow turns into work, how the platform stays safe under failure, and how testing fits in.
Component-specific concepts (definitions, lifecycle, scheduling, etc.) live inside each component's own section.

<div class="grid cards" markdown>

-   :material-numeric-1-box:{ .lg .middle } __System overview__

    ---

    A single diagram showing how a workflow definition, the engine, the CMS, the blackboard, and zone-aware workers fit together.

    [:octicons-arrow-right-24: Read more](10-overview.md)

-   :material-numeric-2-box:{ .lg .middle } __How Neops operates__

    ---

    Read-path, write-path, and full execution-flow sequence diagrams across User, CMS, engine, blackboard, and worker.

    [:octicons-arrow-right-24: Read more](20-how-neops-operates.md)

-   :material-numeric-3-box:{ .lg .middle } __Workflows as transactions__

    ---

    Why every workflow run is a transaction: locking, atomic updates, and FAILED_SAFE vs FAILED_UNSAFE failure classification.

    [:octicons-arrow-right-24: Read more](../neops-workflow-engine/docs/10-concepts/40-workflow-as-a-transaction.md)

-   :material-numeric-4-box:{ .lg .middle } __Function blocks__

    ---

    Versioned, typed Python units that the engine schedules and workers execute.
    See also: [purity & idempotency](../neops-worker-sdk-py/docs/function-blocks/40-pure-and-idempotent.md).

    [:octicons-arrow-right-24: Read more](../neops-workflow-engine/docs/10-concepts/20-function-blocks.md)

-   :material-numeric-5-box:{ .lg .middle } __Blackboard & execution model__

    ---

    How jobs flow from engine to workers and back.
    Pairs with the [execution model](../neops-workflow-engine/docs/10-concepts/50-execution.md) page.

    [:octicons-arrow-right-24: Read more](../neops-workflow-engine/docs/10-concepts/60-blackboard.md)

-   :material-numeric-6-box:{ .lg .middle } __Remote lab testing__

    ---

    Session queue, lab lifecycle, and the one-lab-per-host invariant that makes shared testing safe.

    [:octicons-arrow-right-24: Read more](../neops-remote-lab/docs/10-concepts/10-architecture.md)

</div>
