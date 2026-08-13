# Lab

Neops ships two independent lab environments. They share nothing — no code, no API, no dependency — and serve different purposes: one runs the whole platform on your own machine, the other provides shared real-topology access for automated tests.

## Lab Environments

<div class="grid cards" markdown>

-   :material-laptop:{ .lg .middle } __Local Lab__

    ---

    A turn-key local containerlab environment: 10 FRRouting routers and 5 Nokia SR Linux switches with real point-to-point wiring, plus the full Neops control plane on docker compose — everything on one machine.

    [:octicons-arrow-right-24: Read more](../neops-lab/docs/index.md)

-   :material-cloud-outline:{ .lg .middle } __Remote Lab__

    ---

    Run pytest suites against shared Netlab topologies with real network operating systems, coordinated through a FIFO session queue for exclusive access.

    [:octicons-arrow-right-24: Read more](../neops-remote-lab/docs/index.md)

</div>
