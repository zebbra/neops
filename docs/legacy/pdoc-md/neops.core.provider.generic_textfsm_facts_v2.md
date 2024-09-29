# neops.core.provider.generic_textfsm_facts_v2
## GenericTextFSMFactsV2
This Provider is used to get structured data from show commands from a device.
The show command is executed on the device and the output is parsed by [TextFSM](/appendix_sub/appendix_textfsm).

----------
### JSON Schema
#### Add Structured Command to Facts


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`add_facts_to`** *(string)*: Add Facts to Group, Device, Interface or Clients. Must be one of: `['GLOBAL', 'GROUP', 'DEVICE', 'INTERFACE', 'CLIENT']`.

- **`command_template`** *(string)*: Show command to convert to structured data(String is parsed by Jinja to create the command). Default: `show version`.

- **`textfsm_template`** *(string)*: TextFSM Template to parse the show output.

- **`mapping_template`** *(string)*: parse excel content (given as excel var to jinja) and provide the data structure for the task. Default: `{#### element props group, device, interface or client #}
{#### command results are under the variable command_results #}
{% do neops.set_facts(textfsm) %}`.

- **`slow_device`** *(integer)*: Add a factor for longer wait times for heavy loaded devices. Default: `0`.


----------
### Command and Mapping Templates
##### Command Template

A Jinja Template which is processed before applying the show command.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `elements`: _ids of the affected elements based on add facts to selection_

##### Mapping Template

A Jinja Template which is processed before apply the result of the TextFSM output to the facts.

**If the mapping template is empty (or only contains a space, because of the default value)
the template is not proccessed and the output of the TextFSM output is directly saved to the facts.**

The following parameters are passed to the template processing:

- `command_results`: _output from the TextFSM processing,
if the facts are added to groups it is a list with the device id and result in a dictionary _
- `device`: _the current device object serialized as dictionary_
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
pre_run_on_nornir_device(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,**kwargs) -> Any
```
Processes the command Jinja template and executes the show command on the device

----------
```python
run_global(self,task_kwargs: Dict[Any, Any],**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the output and the mapping template if the "add facts to" is set to GLOBAL

----------
```python
run_on_client_of_interface(self,task_input_kwargs: Dict[Any, Any],task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,client_id: int,client_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Any
```
Processes the output and the mapping template if the "add facts to" is set to CLIENT

----------
```python
run_on_device(self,task_input_kwargs: Dict[Any, Any],task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,device_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult,**kwargs) -> Any
```
Processes the output and the mapping template if the "add facts to" is set to DEVICE

----------
```python
run_on_device_group(self,device_group_id: int,task_kwargs: Dict[Any, Any],device_group_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult,**kwargs) -> Union[Dict[Any, Any], NoneType]
```
Processes the output and the mapping template if the "add facts to" is set to GROUP

----------
```python
run_on_interface(self,task_input_kwargs: Dict[Any, Any],task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,interface_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult,**kwargs) -> Any
```
Processes the output and the mapping template if the "add facts to" is set to INTERFACE

----------