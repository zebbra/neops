# neops.core.provider.generic_from_excel
## GenericFromExcel
Provider to summarize other tasks and take input values from excel.

Every other task is called by its id or uniquetaskname,
it has two templates on to set the entities on which the task is called and one to pass the input values.

----------
### JSON Schema
#### Process Tasks with Excel as Input


##### Properties


- **`run_as`** *(string)*: Select on which entity the task should run on. Must be one of: `['GLOBAL', 'GROUP', 'DEVICE', 'INTERFACE', 'CLIENT']`.

- **`header_num`** *(number)*: On which line in the sheet is the header placed. Default: `1`.

- **`tasks`** *(array)*: This description is used as a help message.

  - **Items** *(object)*

    - **`titleProp`** *(string)*

    - **`run_as`** *(string)*: Select on which execute on entities will be passed to the task. Must be one of: `['GROUP', 'DEVICE', 'INTERFACE', 'CLIENT']`.

    - **`allow_all`** *(boolean)*: some providers have the ability to run on all elements if there are none given, decide if this is fine for your task. Default: `False`.

    - **`entity_template`** *(string)*: Get a List of Entity by the Template. Default: `{% set device_list = [] %}
{% for device in neops.search_devices("devices.hostname: *.neops.io") %}
    {{ device.hostname }}
    {% do device_list.append(device.id) %}
{% endfor %}
{% do neops.set_entities(device_list) %}`.

    - **`task_id`** *(number)*: Default: `0`.

    - **`task_uniquename`** *(string)*: Set unique task name of task to process (task_id has priority).

    - **`task_main`** *(boolean)*: Include pre and post run tasks in this step. Default: `True`.

    - **`task_template`** *(string)*: parse excel content (given as excel var to jinja) and provide the data structure for the task. Default: `{% do neops.set_params({}) %}`.


----------
### Run Input JSON Schema
#### Process Tasks with Excel as Input


##### Properties


- **`excel`** *(string)*: Task input values from Excel file.


----------
### Excel

The excel is passed as a dictionary.

Every sheet has its own key and contains list as value.
The list contans a dictionary for every row, the key are set from the columns titles

----------
### Entity and Params Templates
##### Entity Template

A Jinja Template which is processed to select the entities where the task is applied on.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `excel`: _all dictionary of excel content_
- `elements`: _the current selected objects based on `run_as` serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)
and to save the facts objects_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_
    - `neops.set_entities(ids)`: _sets entities to run the task as list of ids_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

##### Params Template

A Jinja Template which is processed to pass the params to the task.

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `excel`: _all dictionary of excel content_
- `entities`: _ids of elements to run the task on_
- `elements`: _entity objects serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)
and to save the facts objects_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_
    - `neops.set_params(dictionary)`: _sets params as input values for the task_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

### Methods
```python
run_global(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],result=neops.core.provider.base.result.provider_global_result.ProviderGlobalResult,**kwargs) -> Any
```
Process all subtasks

----------