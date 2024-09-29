# neops.core.provider.base.base
## NeopsBaseProvider
The neops base provider contains all methods and required data processing for a concrete provider.
To create a new provider, either extend this NeopsBaseProvider or a concrete provider

the neops base provider is inherited from the [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)

----------
### JSON Schema
#### JSON Schema


### Class variables
```python
deprecated: bool
```
Indicates if this provider will no longer be supported in the future.

----------
```python
description: str
```
Description String, to give the user an indication of the purpose of this provider

----------
```python
execution_updater: neops.core.provider.base.execution_updater.ExecutionUpdater
```
class to update logs of the current execution (is set by initialization)

----------
```python
json_schema: Dict
```
The `json_schema` specifies the required input values to instantiate the provider as a task.

----------
```python
provider_type: neops.core.provider.base.enum.ProviderTypeEnum
```
`provider_type` specifices the provider type, currently we are suppoting vor different types of providers `CONFIGURE`, `FACTS`, `CHECK` and `EXECUTE`. 
The provider type can be used by "frontend" applications to have different processes for the provider types. The neops.io frontend the normal handels for example `CONFIGURE` provider types with a two step run, first dry run then apply.

----------
```python
result_writer: neops.core.provider.base.base_result_writer.BaseResultWriter
```
class to write results (is set by initialization)

----------
```python
run_input_json_schema: Dict
```
\
The `run_input_json_schema` specifies the required parameter a provider uses to run, but they must be given on every run and not on task instantination. 

\
On a task instantination additional parameters can be requested as input values on a task run. They are merged with the `run_input_json_schema` values.

----------
```python
run_on: neops.core.provider.base.enum.RunOnEnum
```
`run_on` specifies on which entity the provider runs, possible values are `GLOBAL`, `GROUP`, `DEVICE`, `INTERFACE`, `CLIENT` and `GENERIC`.
On `GENERIC` the task instance must overwrite the run on value with the `init_adjust_run_on` method, to specify the excact run_on.

----------
```python
run_on_all_if_empty: bool
```
\
`run_on_all_if_empty` specifies if all elements of a given `run_on` type are selected when a empty list is given as `execute_on` parameter on the `run` method.

----------
```python
run_on_result: Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
`run_on_result` specifies for which entity the result is written. 
Normally this is the same as the `run_on` value and if `run_on_result` is `None` then the `run_on` value is used. 

Example for different values of `run_on` and `run_on_result`:
If you build a provider which get facts for interfaces, but those facts are only collectable per device (you always get the facts for all interfaces on this device). 
In such a case it could make sense to set `run_on` to `DEVICE` and `run_on_result` to `INTERFACE`, then you got the result per interface and it's visible for which interfaces the facts are collected.

----------
```python
run_on_strict: bool
```
\
`run_on_strict` specifies if we accept loose input entities for the `execute_on_type` and `execute_on` parameters on the `run` method.

Example: if `run_on_strict` is false and `run_on` is INTERFACE, then we accept a list of devices on the `run` method and will resolve all interfaces on those devices where the task is executed.
This could be a problem for some cases, e.g if you have a configure provider where you prefere to know the exact entities. Because of that `run_on_strict` is true per default.

----------
```python
short_description: str
```
A Short description for list views or others.

----------
```python
success_message: str
```
The `success_message` is used if no message is set on the results object and if a task is successfully executed on an entity.

----------
```python
validate_input: bool
```
\
`validate_input` specifies if the parameters on the `run` method should by verified against the json schema definitions of the task itself, the provider `run_input_json_schema` and `json_schema`.

----------
### Methods
```python
add_markdown_helptext(self,md_content: neops.core.libs.helptext.markdown_content.MarkDownContent) -> NoneType
```
Add documentation elements to the generated provider documentations to give a better insight how this provider should work.

\
On the base provider we add only the json schema of the task instantiation to give a better overview which parameters are required for this provider.

\
__param__ md_content: MarkDownContent of the current documentation of this element.

----------
```python
add_nornir_processors(self) -> List[nornir.core.processor.Processor]
```
Add additional Nornir Processors, for more information see https://nornir.readthedocs.io/en/v2.5.0/tutorials/intro/processors.html

----------
```python
init_adjust_run_on(self,execute_on: Union[List[int], NoneType] = None,execute_on_type: Union[neops.core.provider.base.enum.RunOnEnum, NoneType] = None,dry_run: Union[bool, NoneType] = None,task_input_kwargs: Union[Dict[Any, Any], NoneType] = None,search_query: str = '',task_kwargs: Union[Dict[Any, Any], NoneType] = None,**kwargs) -> NoneType
```
Method to overwrite `run_on`, `run_on_strict` and `run_on_result` values on provider initialization based on the given paremeters of the run and the task itself.

For example used by generic providers.

\
__param__ execute_on: List of element IDs to run on
\
__param__ execute_on_type: Type of those IDs (GROUP, DEVICE, INTERFACE, CLIENT)
\
__param__ dry_run: Indicates if no configuration changes should be made
\
__param__ task_input_kwargs: Run input arguments
\
__param__ task_kwargs: Task arguments

----------
```python
init_before_run(self,task_input_kwargs: Dict,execute_on: List = None,execute_on_type: neops.core.provider.base.enum.RunOnEnum = device,dry_run: bool = True,search_query: str = '',**kwargs) -> NoneType
```
Initialization of all elements before the task runs. This methots initializes all result objects.

\
__param__ task_input_kwargs: Run input arguments
\
__param__ execute_on: List of element IDs to run on
\
__param__ execute_on_type: Type of those IDs (GROUP, DEVICE, INTERFACE, CLIENT)
\
__param__ dry_run: Indicates if no configuration changes should be made
\
__param__ search_query: An optional search query to limit the entities to run on (not yet supported)

----------
```python
init_without_run(self,**kwargs) -> NoneType
```
```python
print_results(self) -> 
```
prints the current result set.

----------
```python
run(self,task_input_kwargs: Dict,execute_on: List = None,execute_on_type: neops.core.provider.base.enum.RunOnEnum = device,dry_run: bool = True,search_query: str = '',**kwargs) -> NoneType
```
Runs the provider based on the initialized task.

\
__param__ task_input_kwargs: Run input arguments
\
__param__ execute_on: List of element IDs to run on
\
__param__ execute_on_type: Type of those IDs (GROUP, DEVICE, INTERFACE, CLIENT)
\
__param__ dry_run: Indicates if no configuration changes should be made
\
__param__ search_query: An optional search query to limit the entities to run on (not yet supported)

----------
```python
update_do(self,do: str,append: bool = True) -> NoneType
```
Wrapper method to the execution updater `update_do` method

\
__param__ do: string what is to do
\
__param__ append: decides if the do string is appended or replaced

----------
```python
update_done(self,done: str,append: bool = True) -> NoneType
```
```python
update_log(self,log: str,append: bool = True) -> NoneType
```
Wrapper method to the execution updater `update_log` method

\
__param__ log: the log string
\
__param__ append: decides if the log string is appended or replaced

----------
```python
validate_schema(self,task_kwargs: Dict = None) -> NoneType
```
\
Validates if the parameters of the task

\
__param__ task_kwargs: task parameters

----------
```python
write_results(self,subtask_finish: bool = False,task_finish: bool = False) -> NoneType
```
Write the result states to the database.

\
__param__ subtask_finish: is true if i am a subtasks (pre/post run task) and the task itself is finished
\
__param__ task_finish: is true if all subtasks and the task itself is finished

----------
### Functions
```python
inherit_json_schema(json_schema: Dict = None) -> Dict
```
Merges JSON Schemas: If this method is called on one of the classes children, then
super().json_schema resolves, else we do a pseudo merge.
\
__param__ json_schema:
\
__return__: Dict of merged JSON Schema

----------
```python
init_from_task_model(neops_task: neops.core.models.neops_task.NeopsTask,nr: nornir.core.Nornir = None,**kwargs) -> neops.core.provider.base.base.NeopsBaseProvider
```
Initialization of the task by a the given `NeopsTask` model and the `Nornir` inventory.

\
__param__ neops_task: Neops Task Model
\
__param__ nr: Nornir Inventory

\
__return__: Instance of the provider/task itself

----------
```python
merge_run_input_json_schema(json_schema: Dict = None) -> 
```
Merges the JSON Schemas of instanciated task and those of this provider

\
__param__ json_schema:
\
__return__: merged JSON Schema

----------