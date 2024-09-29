# neops.core.provider.generic_rest_facts
## GenericRestFactsProvider
Provider to get facts from a GET on a REST API

----------
### JSON Schema
#### Add Return Value from REST call to Facts


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`url`** *(string)*: Jinja Template can be used to get parameters, element of run on is passed to Jinja Template.

- **`request_on`** *(string)*: Run Global or on Group, Device or Interface. Must be one of: `['GLOBAL', 'GROUP', 'DEVICE', 'INTERFACE']`.

- **`auth`** *(object)*

- **`mapping`** *(object)*

  - **`add_facts_to`** *(string)*: Add Facts to Group, Device or Interface. Must be one of: `['GROUP', 'DEVICE', 'INTERFACE']`.

  - **`mapping_template`** *(string)*: Return string from Jinja Template is evaluated and mapped to given element. Default: `{% do neops.set_facts(response) %}`.

- **`headers`** *(array)*

  - **Items** *(object)*

    - **`header_name`** *(string)*

    - **`header_value`** *(string)*


----------
### URL Template

A Jinja Template to generate the URL whichone is requested.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- entity objects based on `request_on`
    - none: _on `GLOBAL`
    - `device_group`: _on `GROUP`, the current device group object serialized as dictionary_
    - `device`: _on `DEVICE`, the current device object serialized as dictionary_
    - `interface`: _on `INTERFACE`, the current interface object serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)
and to save the facts objects_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_
    - `neops.set_facts(dictionary)`: _sets the facts to be saved_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)


----------
### Mapping Template

A Jinja Template to map the response to facts.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- entity objects based on `request_on`
    - none: _on `GLOBAL`
    - `device_group`: _on `GROUP`, the current device group object serialized as dictionary_
    - `device`: _on `DEVICE`, the current device object serialized as dictionary_
    - `interface`: _on `INTERFACE`, the current interface object serialized as dictionary_
- `response`: _response result or list of response results based on related objects_
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
get_rest(self,url: str,auth: Dict = None,headers: List = None) -> Dict
```
Process the requests based on authentication, headers and the request URL

----------
```python
pre_run_global(self,request_on: str,url: str,task_input_kwargs: Dict,auth: Dict = None,headers: List = None,**kwargs) -> Any
```
Process a global request

----------
```python
pre_run_on_device(self,task: nornir.core.task.Task,device_id: int,request_on: str,url: str,task_input_kwargs: Dict,auth: Dict = None,headers: List = None,**kwargs) -> Any
```
Process a request per device

----------
```python
pre_run_on_device_group(self,device_group_id: int,request_on: str,url: str,task_input_kwargs: Dict,auth: Dict = None,headers: List = None,**kwargs) -> Any
```
Process a request per group

----------
```python
pre_run_on_interface(self,task: nornir.core.task.Task,interface_id: int,request_on: str,url: str,task_input_kwargs: Dict,auth: Dict = None,headers: List = None,**kwargs) -> Any
```
Process a request per device

----------
```python
run_global(self,result: neops.core.provider.base.result.provider_result.ProviderResult,request_on: str,mapping: Dict,**kwargs) -> Any
```
Set common facts based on global request

----------
```python
run_on_device(self,task: nornir.core.task.Task,device_id: int,device_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult,request_on: str,mapping: Dict,task_input_kwargs: Dict,**kwargs) -> Any
```
Set facts to device based on mapping template

----------
```python
run_on_device_group(self,device_group_id: int,device_group_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult,request_on: str,mapping: Dict,task_input_kwargs: Dict,**kwargs) -> Any
```
Set facts to device group based on mapping template

----------
```python
run_on_interface(self,task: nornir.core.task.Task,interface_id: int,interface_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult,request_on: str,mapping: Dict,task_input_kwargs: Dict,**kwargs) -> Any
```
Set facts to interface based on mapping template

----------