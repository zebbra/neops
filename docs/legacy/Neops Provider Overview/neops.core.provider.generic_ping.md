# neops.core.provider.generic_ping
## GenericPing
Ping Targets and save results as facts

----------
### JSON Schema
#### Add Structured Command to Facts


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`add_facts_to`** *(string)*: Add Facts to Group, Device, Interface or Clients. Must be one of: `['GLOBAL', 'GROUP', 'CLIENT OF LOCATIONS', 'DEVICE', 'INTERFACE', 'CLIENT OF INTERFACE']`.

- **`destination_template`** *(string)*: List of Targets (1 per line). Default: `8.8.8.8`.
