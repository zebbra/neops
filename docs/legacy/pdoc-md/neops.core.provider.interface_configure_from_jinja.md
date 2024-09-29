# neops.core.provider.interface_configure_from_jinja
## InterfaceJinjaConfigureProvider
Provider to configure a device based on the passed interface selection to a jinja template

----------
### Interface Configure Parameters
#### Template

A Jinja Template which is processed before apply the result of this template to the device.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `device`: _the current device object serialized as dictionary_
- `interfaces`: _the current selected interface objects serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

Example of device and neops usage (only to show usage, config change doesn't make sense):
```jinja
hostname {{ device.hostname }}

{% for interface in interfaces %}
interface {{ interface.name }}
  description NEW-DESCRIPTION
{% endfor %}
```


----------
### Global Base Configure Parameters
#### Apply Method

The apply method descripbes how the configuration is written to the device.

* `cli`: the configuration is applied directly in the configration mode
* `scp`: the configuration is copied (with scp) as a file to the device and applied with an merge operation
* `scp-startup`: the configuration is copied (with scp) as a file to the device and written to the start up
configuration


#### Slow Devices

With the `slow_device` parameter you can specify a delay factor to wait a longer time on responses from
            slow devices

----------
### JSON Schema
#### Interface Configuration


##### Properties


- **`apply`** *(string)*: Method how to apply the configuration, over cli or copy with scp and merge. Must be one of: `['scp', 'cli', 'scp-startup']`.

- **`slow_device`** *(integer)*: Add a factor for longer wait times for heavy loaded devices. Default: `0`.

- **`template`** *(string)*: Jinja Template to generate the configuration.

### Methods
```python
run_on_device(self,task: nornir.core.task.Task,device_id: int,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,**kwargs) -> nornir.core.task.Result
```
Process the template and apply the configuration to the device

----------