# Installation & Deployment

Neops is composed of multiple deployable services.
Each component owns its own deployment guide; this page is the index.
Start with the workflow engine, then bring up workers, then add the remote lab and secure gateway as needed.

<div class="grid cards" markdown>

-   :material-numeric-1-box:{ .lg .middle } __Workflow Engine__

    ---

    Deploy the orchestration core: configuration, Docker images, worker management, and operations.

    [:octicons-arrow-right-24: Read more](../neops-workflow-engine/docs/50-deployment/index.md)

-   :material-numeric-2-box:{ .lg .middle } __Worker SDK (Python workers)__

    ---

    Package, configure, and run worker processes that execute your function blocks.

    [:octicons-arrow-right-24: Read more](../neops-worker-sdk-py/docs/deployment/index.md)

-   :material-numeric-3-box:{ .lg .middle } __Remote Lab__

    ---

    Set up the Netlab host and Headscale VPN so developers and CI can share lab topologies safely.

    [:octicons-arrow-right-24: Read more](../neops-remote-lab/docs/40-deployment/index.md)

-   :material-numeric-4-box:{ .lg .middle } __Secure Gateway__

    ---

    Front the Neops API with a GraphQL gateway that filters operations and data for external consumers.

    [:octicons-arrow-right-24: Read more](/neops-secure-gateway/docs/)

-   :material-numeric-5-box:{ .lg .middle } __Configuration reference__

    ---

    All environment variables and runtime knobs for the workflow engine in one place.

    [:octicons-arrow-right-24: Read more](../neops-workflow-engine/docs/50-deployment/10-configuration.md)

</div>
