# neops.core.provider.global_mail
## GlobalMail
Send email notification

----------
### JSON Schema
#### Mail


##### Properties


- **`include_executor`** *(boolean)*: Add the task executor to the list to recipients. Default: `False`.

- **`mail_to`** *(string)*: recipients email addresses comma separated. Default: ``.

- **`title`** *(string)*: Process Jinja template to set email title. Default: ``.

- **`body`** *(string)*: Process Jinja template to set email body. Default: ``.

- **`as_attachment`** *(string)*: Process Jinja template to send infomarations as email attachment. Default: ``.

- **`attachment_name`** *(string)*: name of the attachment. Default: ``.

- **`zip_attachment`** *(boolean)*: should we compress the attachment. Default: `False`.

- **`mail_from`** *(string)*: set the from address of the email. Default: ``.


----------
### Templates

Jinja Template options for processing email title, body and attachment

The following parameters are passed to the template processing:

- `input`: _all inputs from the task run arguments_
- `execution`: _the current execution information serialized as dictionary_
- `neops`: _the neops object brings methods to access to other elements over the [neops.io search](#search)_
    - `neops.search_devices(query)`: _returns a list of devices found by the search query_
    - `neops.search_interfaces(query)`: _returns a list of interfaces found by the search query_
    - `neops.search_device_groups(query)`: _returns a list of groups found by the search query_
    - `neops.search_client(query)`: _returns a list of clients found by the search query_
    - `neops.get_common_facts(key)`: _returns the common/global fact of the given key_

For more information on how to build a Jinja2 template, have a look at [Appendix under Jinja2](appendix.md#jinja2)

### Methods
```python
run_global(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],result,**kwargs) -> Any
```
Process template and send email

----------