# neops.core.provider.interface_rollback
## InterfaceRollbackProvider
The neops base provider contains all methods and required data processing for a concrete provider.
To create a new provider, either extend this NeopsBaseProvider or a concrete provider

the neops base provider is inherited from the [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)

----------
### JSON Schema
#### Configure Base Provider


##### Properties


- **`apply`** *(string)*: Method how to apply the configuration, over cli or copy with scp and merge. Must be one of: `['scp', 'cli']`. Default: `cli`.
