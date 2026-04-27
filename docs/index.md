# Neops product documentation

[![Neops Documentation](https://github.com/zebbra/neops/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/zebbra/neops/actions/workflows/gh-pages.yml)

Neops is a transactional network automation platform.
Operators describe network changes as workflows — ordered sequences of versioned function blocks — which the workflow engine orchestrates by acquiring entity locks from the CMS, distributing jobs to workers through the blackboard job queue, and applying changes atomically with explicit failure semantics (FAILED_SAFE vs FAILED_UNSAFE).
Function blocks are written in Python with the worker SDK and tested against real topologies via the Remote Lab, while the web client exposes workflows to operators and the Secure Gateway lets external consumers reach a filtered subset of the API.


## Documentation Overview

<div class="grid cards" markdown>

-   :material-numeric-1-box:{ .lg .middle } __Getting Started__

    ---

    Recommended entry points for operators, workflow authors, and function-block developers.

    [:octicons-arrow-right-24: Read more](getting-started/00-index.md)

-   :material-numeric-2-box:{ .lg .middle } __Concepts__

    ---

    The cross-cutting ideas — transactional model, function blocks, blackboard, remote lab — that explain how the pieces fit together.

    [:octicons-arrow-right-24: Read more](concepts/)

-   :material-numeric-3-box:{ .lg .middle } __User Guide__

    ---

    Use the web client to browse entity data, trigger workflows, and watch executions live.

    [:octicons-arrow-right-24: Read more](coming-soon.md)

-   :material-numeric-4-box:{ .lg .middle } __Workflows__

    ---

    Author, schedule, and operate workflows with the workflow engine: definitions, lifecycle, retries, and rollbacks.

    [:octicons-arrow-right-24: Read more](neops-workflow-engine/docs/)

-   :material-numeric-5-box:{ .lg .middle } __Function Blocks__

    ---

    Build reusable Python execution units with the worker SDK — anatomy, device connections, testing, deployment.

    [:octicons-arrow-right-24: Read more](neops-worker-sdk-py/docs/)

-   :material-numeric-6-box:{ .lg .middle } __Remote Lab__

    ---

    Run pytest suites against shared Netlab topologies via a FIFO session queue.

    [:octicons-arrow-right-24: Read more](neops-remote-lab/docs/)

-   :material-numeric-7-box:{ .lg .middle } __Installation & Deployment__

    ---

    Per-component deployment guides for the engine, workers, remote lab, and secure gateway.

    [:octicons-arrow-right-24: Read more](installation/)

-   :material-numeric-8-box:{ .lg .middle } __Modules__

    ---

    Optional add-on services such as the Secure Gateway.

    [:octicons-arrow-right-24: Read more](modules/)

</div>
