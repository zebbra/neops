# neops.core.provider.deprecated.interface_test_provider
### Module functions
```python
test_failed_sub_task(task: nornir.core.task.Task,res: str,failed: bool = False) -> nornir.core.task.Result
```
## InterfaceTestProvider
The neops base provider contains all methods and required data processing for a concrete provider.
To create a new provider, either extend this NeopsBaseProvider or a concrete provider

the neops base provider is inherited from the [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)

----------
### JSON Schema
#### Interface Test Provider


##### Properties


- **`foo`** *(string)*: Foo Task Form Value.

- **`bar`** *(boolean)*: Bar Task Form Value.

### Class variables
```python
set_child_to_failed
```