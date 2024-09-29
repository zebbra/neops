# neops.core.provider.base.base_facts
## NeopsFactsBaseProvider
This Provider is inherited from the `NeopsBaseProvider`, it brings additional functionality to handle facts (flexible data structures per entity).

Every task based on this provider needs a facts key where the facts result is stored in the database per element.

For providers inherits from this provider the facts results are written automatically based on the result set of the pre- and run methods per element.
It supports data structures of any kind as long as they are compatible to JSON.

This provider should be the base for fact providers. So if you create a new fact provider with, either extend this `NeopsFactsBaseProvider` or a concrete fact provider

----------
### JSON Schema
#### Facts Base Provider


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

### Class variables
```python
facts_for
```
The entity where the facts are for, can be different from the `run_on`, so specify if required otherwise we will use the `run_on` value.

This provider supports that facts are written for different entities, so use facts for as a list.

----------
### Methods
```python
process_client_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult]) -> NoneType
```
`process_client_results` is called at the end of the run cycle.
It stores the client results data structures as facts to the database if the `facts_for` variable is set to `CLIENT`

----------
```python
process_device_group_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult]) -> NoneType
```
`process_device_group_results` is called at the end of the run cycle.
It stores the device group results data structures as facts to the database if the `facts_for` variable is set to `GROUP`

----------
```python
process_device_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult]) -> NoneType
```
`process_device_results` is called at the end of the run cycle.
It stores the device results data structures as facts to the database if the `facts_for` variable is set to `DEVICE`

----------
```python
process_global_result(self,result: neops.core.provider.base.result.provider_result.ProviderResult) -> NoneType
```
`process_global_result` is called at the end of the run cycle.
It stores the global results data structures as facts to the database if the `facts_for` variable is set to `GLOBAL`

----------
```python
process_interface_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult]) -> NoneType
```
`process_interface_results` is called at the end of the run cycle.
It stores the interface results data structures as facts to the database if the `facts_for` variable is set to `INTERFACE`

----------