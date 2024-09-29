# neops.core.provider.deprecated.device_test_provider
### Module functions
```python
test_sub_sub_task(task: nornir.core.task.Task,res: str) -> nornir.core.task.Result
```
```python
test_sub_task(task: nornir.core.task.Task,res: str) -> nornir.core.task.Result
```
## DeviceTestProvider
The neops base provider contains all methods and required data processing for a concrete provider.
To create a new provider, either extend this NeopsBaseProvider or a concrete provider

the neops base provider is inherited from the [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)

----------
### JSON Schema
#### Demo Form JSON Schema


##### Properties


- **`foo`** *(string)*: Foo rendered as normal input field.

- **`bar`** *(string)*: Bar rendered as editor with syntax highlighting for jinja2.

- **`bool`** *(boolean)*: boolean is rendered as checkbox. Default: `False`.
