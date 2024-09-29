# Facts

Facts in neops.io are flexible data structures stored as JSON in the database. Every fact/data structure is stored under a given key. Facts are collected by fact tasks.

They are representing a state at a given time. And facts are not only facts, they can represent states as well.

Examples of facts:

- Software release running on a network device
- A configuration parameter eg. the log server
- State of a routing protocol neighbor ship
- Information from peripheral systems, like CMDB and others
  - Information about service SLA
  - Information about physical device access

Facts can be stored on every entity known in neops.io
(see [Entities](35-architecture#entities))

Data structures of facts are **searchable**.

They are collected by [FACTS Tasks/Providers](/30-provider_overview) and they need a key to be stored.

!> Choose the facts key wisely, because if the key contains ip (pattern `*.ip.*`) an ip address (yes ipv6 as well) or an empty string is expected. otherwise the content is skipped for searching.

Example

```JSON
  "napalm_facts": {
    "fqdn": "dsw01.neops.io",
    "model": "IOSv",
    "uptime": 2547840,
    "vendor": "Cisco",
    "hostname": "sw01",
    "os_version": "vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(CML_NIGHTLY_20180619)FLO_DSGS7, EARLY DEPLOYMENT DEVELOPMENT BUILD, synced to  V152_6_0_81_E",
    "serial_number": "93F8UGICVB2",
    "interface_list": [
      "GigabitEthernet0/0",
      "GigabitEthernet0/1",
      "GigabitEthernet0/2",
      "GigabitEthernet0/3",
      "GigabitEthernet1/0",
      "GigabitEthernet1/1",
      "GigabitEthernet1/2",
      "GigabitEthernet1/3",
      "GigabitEthernet2/0",
      "GigabitEthernet2/1",
      "GigabitEthernet2/2",
      "GigabitEthernet2/3",
      "GigabitEthernet3/0",
      "GigabitEthernet3/1",
      "GigabitEthernet3/2",
      "GigabitEthernet3/3",
      "Vlan10"
    ]
  },
  "vlans": [
    {
      "name": "default",
      "status": "active",
      "vlan_id": "1",
      "interfaces": [
        "Gi0/1",
        "Gi0/2",
        "Gi0/3",
        "Gi1/2",
        "Gi1/3",
        "Gi2/0",
        "Gi2/1",
        "Gi2/2",
        "Gi2/3",
        "Gi3/0",
        "Gi3/1",
        "Gi3/2",
        "Gi3/3"
      ]
    },
    {
      "name": "MGMT",
      "status": "active",
      "vlan_id": "10",
      "interfaces": []
    },
    {
      "name": "CLIENT-A",
      "status": "active",
      "vlan_id": "100",
      "interfaces": []
    },
    {
      "name": "CLIENT-B",
      "status": "active",
      "vlan_id": "101",
      "interfaces": []
    },
    {
      "name": "CLIENT-C",
      "status": "active",
      "vlan_id": "102",
      "interfaces": []
    },
    {
      "name": "fddi-default",
      "status": "act/unsup",
      "vlan_id": "1002",
      "interfaces": []
    },
    {
      "name": "token-ring-default",
      "status": "act/unsup",
      "vlan_id": "1003",
      "interfaces": []
    },
    {
      "name": "fddinet-default",
      "status": "act/unsup",
      "vlan_id": "1004",
      "interfaces": []
    },
    {
      "name": "trnet-default",
      "status": "act/unsup",
      "vlan_id": "1005",
      "interfaces": []
    }
  ],
```
