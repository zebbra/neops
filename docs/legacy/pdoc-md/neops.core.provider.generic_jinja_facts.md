# neops.core.provider.generic_jinja_facts
## GenericJinjaFactsProvider
This Provider is used to restructure new facts from existing facts.

----------
### JSON Schema
#### Generic Jinja Check


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`add_facts_to`** *(string)*: Select on which entity you want save the Facts. Must be one of: `['GLOBAL', 'GROUP', 'DEVICE', 'INTERFACE', 'CLIENT ON GROUP', 'CLIENT ON INTERFACE']`.

- **`mapping_template`** *(string)*: Default: `{% do neops.set_facts({}) %}`.


----------
### Mapping Template

The Jinja template which is processed to map the values to the new facts.


The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- entity objects based on add_facts_to
    - `none` _on `GLOBAL`_
    - `device_group`: _on `GROUP`, the current device group object serialized as dictionary_
    - `device`: _on `DEVICE`, the current device object serialized as dictionary_
    - `interface`: _on `INTERFACE`, the current interface object serialized as dictionary_
    - `client`: _on `CLIENT ON GROUP` or `CLIENT ON INTERFACE`, the current client object serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)
and to save the facts objects_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_
    - `neops.set_facts(dictionary)`: _sets the facts to be saved_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

### Methods
```python
run_global(self,task_kwargs: Dict[Any, Any],**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to GLOBAL

----------
```python
run_on_client_of_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,client_id: int,client_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to CLIENT ON INTERFACE

----------
```python
run_on_client_of_location(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],location_id: int,client_id: int,client_result,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to CLIENT ON GROUP

----------
```python
run_on_device(self,task_input_kwargs: Dict[Any, Any],task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,device_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to DEVICE

----------
```python
run_on_device_group(self,device_group_id: int,task_kwargs: Dict[Any, Any],device_group_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to GROUP

----------
```python
run_on_interface(self,task_input_kwargs: Dict[Any, Any],task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,interface_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the mapping template if the "add facts to" is set to INTERFACE

----------