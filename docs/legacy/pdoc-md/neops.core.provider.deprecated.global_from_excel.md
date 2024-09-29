# neops.core.provider.deprecated.global_from_excel
## GlobalFromExcel
The neops base provider contains all methods and required data processing for a concrete provider.
To create a new provider, either extend this NeopsBaseProvider or a concrete provider

the neops base provider is inherited from the [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)

----------
### JSON Schema
#### Excel to Process Tasks


##### Properties


- **`header_num`** *(number)*: On which line in the sheet is the header placed. Default: `1`.

- **`tasks`** *(array)*: This description is used as a help message.

  - **Items** *(object)*

    - **`hosts_template`** *(string)*: parse excel content (given as excel var to jinja) and create a list of hosts to run the process on. Default: ``.

    - **`task_id`** *(number)*: Default: `0`.

    - **`task_template`** *(string)*: parse excel content (given as excel var to jinja) and provide the data structure for the task. Default: ``.
