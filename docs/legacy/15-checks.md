# Checks

Checks in neops.io are fixed data structures with a state (ok, nok, check execution failed), a reason and flexible metric values. Every check result is stored under a given key.

They are representing a defined state at a given time

Examples of checks:

- Verify if a fact meets the requirement:
  - Is the correct software version installed?
  - Is the BGP Session up
- Directly check a state of an element:
  - Is this destination reachable over ICMP
  - Are there any software advisories for this device
- Aggregation of other check results:
  - Has every device at a location the correct software version
  - Has a device the correct software version and are there no critical bugs in this software release

Checks can be stored on every entity known in neops.io
(see [Entities](35-architecture#entities))

Data structures of checks are **searchable**.

They are collected by [Check Tasks/Providers](/30-provider_overview) and they need a key to be stored.

Example of a check data structure

```JSON
{
  "mgmt_vlan_check": {
    "id": 67,
    "date": "2020-09-11T07:07:47.190Z",
    "reason": "MGMT VLAN does exist",
    "result": "ok",
    "metrics": {}
  }
}
```

Checks can store relations to facts or other checks where they are based on, to drill down the reason on a check result.

## Pre and Post Run Checks

You can use check task as pre or post run of other tasks. If a check fails as a pre or post run task (in a [task graph](20-tasks?id=pre-and-post-running-tasks-task-graph)) it prevents the execution of other task steps for the failed element.
