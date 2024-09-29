# neops.core.provider.generic_report
## GenericReportProvider
Provider to generate a custom output to copy pase to an other application

----------
### JSON Schema
#### Excel to Process Tasks


##### Properties


- **`report_for`** *(string)*: Select on which entity you want to report. Must be one of: `['GROUP', 'DEVICE', 'INTERFACE', 'CLIENT']`.

- **`template`** *(string)*: Jinja template for the report.


----------
### Report Templates

A Jinja Template to generate the report.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- entity objects based on add_facts_to
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

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

### Methods
```python
run_on_client_of_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,client_id: int,report_for: str,**kwargs) -> Any
```
Process report on CLIENT

----------
```python
run_on_device(self,task: nornir.core.task.Task,device_id: int,report_for: str,template: str,**kwargs) -> Any
```
Process report on DEVICE

----------
```python
run_on_device_group(self,device_group_id: int,report_for: str,template: str,**kwargs) -> Any
```
Process report on GROUP

----------
```python
run_on_interface(self,task: nornir.core.task.Task,device_id: int,interface_id: int,report_for: str,template: str,**kwargs) -> Any
```
Process report on INTERFACE

----------