# neops.core.provider.generic_jinja_check
## GenericJinjaCheckProvider
This Provider is used to set [check](/checks) results from existing facts or checks.

----------
### JSON Schema
#### Generic Jinja Check


##### Properties


- **`check_key`** *(string)*: Set the key where the check is saved.

- **`check_on`** *(string)*: Select on which entity you want save the Check. Must be one of: `['GROUP', 'DEVICE', 'INTERFACE', 'CLIENT ON GROUP', 'CLIENT ON INTERFACE']`.

- **`template`** *(string)*: Jinja Template to set the check results. Default: `{% do neops.set_result(True) %}
{% do neops.set_reason("because") %}`.


----------
### Template

The Jinja template which is processed to map the values to the new facts.


The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- entity objects based on `check_on`
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
    - `neops.set_result(result)`: _sets the check result, if the check is successful (`ok` or `true`),
    not successful (`nok` or `false`) or if the check execution is failed (any other value)_
    - `neops.set_metrics(metrics)`: _set metrics values (dictionary) of a check_
    - `neops.set_reason(reason)`: _set reason for the check result_
    - set reference to related results for teardown
        - `neops.add_related_device_group_facts(device_group_id, fact_key)`: _set reference to device group
facts by id and fact key_
        - `neops.add_related_device_facts(device_id, fact_key)`: _set reference to device facts by id and fact key_
        - `neops.add_related_interface_facts(interface_id, fact_key)`: _set reference to interface facts by id and
fact key_
        - `neops.add_related_client_facts(client_id, fact_key)`: _set reference to client facts by id and fact
key_
        - `neops.add_related_device_group_check(device_group_id, check_key)`: _set reference to device group check by
id and check key_
        - `neops.add_related_device_check(device_id, check_key)`: _set reference to device check by id and check key_
        - `neops.add_related_interface_check(interface_id, check_key)`: _set reference to interface check by id and
check key_
        - `neops.add_related_client_check(client_id, check_key)`: _set reference to client check by id and check key_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

### Methods
```python
run_on_client_of_interface(self,task: nornir.core.task.Task,client_id: int,check_on: str,template: str,**kwargs) -> Union[neops.core.provider.base.base_check.NeopsCheckResult, NoneType]
```
Processes the template if the "Check on" is set to CLIENT ON INTERFACE

----------
```python
run_on_client_of_location(self,client_id: int,check_on: str,template: str,**kwargs) -> Union[neops.core.provider.base.base_check.NeopsCheckResult, NoneType]
```
Processes the template if the "Check on" is set to CLIENT ON GROUP

----------
```python
run_on_device(self,task: nornir.core.task.Task,device_id: int,check_on: str,template: str,**kwargs) -> Union[neops.core.provider.base.base_check.NeopsCheckResult, NoneType]
```
Processes the template if the "Check on" is set to DEVICE

----------
```python
run_on_device_group(self,device_group_id: int,check_on: str,template: str,**kwargs) -> Union[neops.core.provider.base.base_check.NeopsCheckResult, NoneType]
```
Processes the template if the "Check on" is set to GROUP

----------
```python
run_on_interface(self,task: nornir.core.task.Task,interface_id: int,check_on: str,template: str,**kwargs) -> Union[neops.core.provider.base.base_check.NeopsCheckResult, NoneType]
```
Processes the template if the "Check on" is set to INTERFACE

----------