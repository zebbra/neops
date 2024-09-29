# neops.core.provider.device_snmp_facts
## DeviceSNMPFactsProvider
Provider to get facts from SNMP

----------
### JSON Schema
#### Add Structured Command to Facts


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`oidKeyPairs`** *(array)*: Specify which OIDs you would like to store as a fact. The fact key can help you to identify the value later.

  - **Items** *(object)*

    - **`oid`** *(string)*

    - **`key`** *(string)*

### Methods
```python
oid_str_to_tuple(self,oid: str) -> 
```