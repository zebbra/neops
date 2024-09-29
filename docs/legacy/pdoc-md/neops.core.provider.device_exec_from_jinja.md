# neops.core.provider.device_exec_from_jinja
## DeviceJinjaExecProvider
Provider to execute commands in exec mode

----------
### Device Configure Parameters
#### Template

A Jinja Template which is processed before apply the result of this template.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `device`: _the current device object serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

Example of device and neops usage (only to show usage, config change doesn't make sense):
```jinja
copy ftp://host/file.text flash: :expect destination
yes
```
**Expecting User Feedback**

Normally a prompt is expected after executing commands on a device.
But as you can see in the template above, there could be commands whichone are asking for user feedback.
To handle user feedbacks you can pass an other value than the prompt to be expected by passing `:expect [expect value]`.


----------
### JSON Schema
#### Device Exec


##### Properties


- **`template`** *(string)*: Jinja Template to generate the configuration.

### Methods
```python
run_on_device(self,task: nornir.core.task.Task,device_id: int,**kwargs) -> nornir.core.task.Result
```
`run_on_device` is called by the run cycle.
It processes the template and executes the commands on the device

----------