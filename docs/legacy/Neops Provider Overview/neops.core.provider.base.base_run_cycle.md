# neops.core.provider.base.base_run_cycle
## BaseRunCycle
Description of the base run cycle for a provider

----------
### Access to Task and Input Arguments


To access to the task arguments and to the given input values use the following arguments passed to every run cycle methhod

**Task Arguments**
```python
task_option = task_kwargs.get('task_option')
```
**Run Input Arguments**
```python
input_option = task_input_kwargs.get('input_option')
```
        
### Class variables
```python
name: str
```
### Methods
```python
add_markdown_helptext(self,md_content: neops.core.libs.helptext.markdown_content.MarkDownContent) -> NoneType
```
Add documentation elements to the generated provider documentations to give a better insight how this provider should work.

\
__param__ md_content: MarkDownContent of the current documentation of this element.

----------
```python
pre_run_global(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],result=neops.core.provider.base.result.provider_global_result.ProviderGlobalResult,**kwargs) -> Any
```
This method is executed as the 1. step of a run cycle. It's called once on a global basis.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ result ([ProviderGlobalResult], optional): empty ProviderGlobalResult to be updated

\
__return__: results or exceptions are stored in a ProviderGlobalResult object

----------
```python
pre_run_on_client_of_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,client_id: int,client_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Any
```
This method is executed as the 7. step of a run cycle. It's called once per related (execute_on and execute_on_type) clients connected to the interfaces of step 6.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the related device
\
__param__ interface_id (int): id of the connected interface
\
__param__ client_id (int): id of the current client
\
__param__ client_result ([ProviderClientResult], optional): empty ProviderClientResult to be updated (with a reference to the related parent objects)

\
__return__: results or exceptions are stored in a ProviderClientResult object

----------
```python
pre_run_on_client_of_location(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],location_id: int,client_id: int,client_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Any
```
This method is executed as the 3. step of a run cycle. It's called once per related (execute_on and execute_on_type) client on the location of the 2. step.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ location_id (int): id of the related location/device group
\
__param__ client_id (int): id of the current client
\
__param__ client_result ([ProviderClientResult], optional): empty ProviderClientResult to be updated (with a reference to the related parent objects)

\
__return__: results or exceptions are stored in a ProviderClientResult object

----------
```python
pre_run_on_device(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,device_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult,**kwargs) -> Any
```
This method is executed as the 5. step of a run cycle. It's called once per related (execute_on and execute_on_type) device.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the current device
\
__param__ device_result ([ProviderDeviceResult], optional): empty ProviderDeviceResult to be updated (with a reference to the related parent objects)

\
__return__: results or exceptions are stored in a ProviderDeviceResult object

----------
```python
pre_run_on_device_group(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],device_group_id: int,device_group_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult,**kwargs) -> Any
```
This method is executed as the 2. step of a run cycle. It's called once per related (execute_on and execute_on_type) device group.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ device_group_id (int): id of the current device group
\
__param__ device_group_result ([ProviderDeviceGroupResult], optional): empty ProviderDeviceGroupResult to be updated

\
__return__: results or exceptions are stored in a ProviderDeviceGroupResult object

----------
```python
pre_run_on_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,interface_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult,**kwargs) -> Any
```
This method is executed as the 6. step of a run cycle. It's called once per related (execute_on and execute_on_type) interface.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the related device
\
__param__ interface_id (int): id of the current interface
\
__param__ interface_result ([ProviderInterfaceResult], optional): empty ProviderInterfaceResult to be updated (with a reference to the related parent objects)

\
__return__: results or exceptions are stored in a ProviderInterfaceResult object

----------
```python
pre_run_on_nornir_device(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,nornir_device_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult,**kwargs) -> Any
```
This method is executed as the 4. step of a run cycle. It's called once per related (execute_on and execute_on_type) nornir_device.

A nornir_device is in the most cases the same as a device, except you have controller configured devices, then it's the controller itself or in otherwords where configurations are applied.

Nornir devices are executed and threaded with nornir task runner.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the current nornir device
\
__param__ nornir_device_result ([ProviderNornirDeviceResult], optional): empty ProviderNornirDeviceResult to be updated (with a reference to the related parent objects)

\
__return__: results or exceptions are stored in a ProviderNornirDeviceResult object

----------
```python
run_global(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],result=neops.core.provider.base.result.provider_global_result.ProviderGlobalResult,**kwargs) -> Any
```
This method is executed as the 14. step of a run cycle. It's called once on a global basis.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ result ([ProviderGlobalResult], optional): ProviderGlobalResult with the result of step 1
\
__return__: results or exceptions are stored in a ProviderGlobalResult object

----------
```python
run_on_client_of_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,client_id: int,client_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Any
```
This method is executed as the 8. step of a run cycle. It's called once per related (execute_on and execute_on_type) clients connected to the interfaces of step 9.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the related device
\
__param__ interface_id (int): id of the connected interface
\
__param__ client_id (int): id of the current client
\
__param__ client_result ([ProviderClientResult], optional): ProviderClientResult with the results of step 7

\
__return__: results or exceptions are stored in a ProviderClientResult object

----------
```python
run_on_client_of_location(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],location_id: int,client_id: int,client_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult,**kwargs) -> Any
```
This method is executed as the 12. step of a run cycle. It's called once per related (execute_on and execute_on_type) client on the location of the 2. step.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ location_id (int): id of the related location/device group
\
__param__ client_id (int): id of the current client
\
__param__ client_result ([ProviderClientResult], optional): ProviderClientResult with the result of step 3

\
__return__: results or exceptions are stored in a ProviderClientResult object

----------
```python
run_on_device(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,device_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult,**kwargs) -> Any
```
This method is executed as the 10. step of a run cycle. It's called once per related (execute_on and execute_on_type) device.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the current device
\
__param__ device_result ([ProviderDeviceResult], optional): ProviderDeviceResult with the result of step 5

\
__return__: results or exceptions are stored in a ProviderDeviceResult object

----------
```python
run_on_device_group(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],device_group_id: int,device_group_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult,**kwargs) -> Any
```
This method is executed as the 13. step of a run cycle. It's called once per related (execute_on and execute_on_type) device group.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ device_group_id (int): id of the current device group
\
__param__ device_group_result ([ProviderDeviceGroupResult], optional): ProviderDeviceGroupResult with the result of step 2

\
__return__: results or exceptions are stored in a ProviderDeviceGroupResult object

----------
```python
run_on_interface(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,device_id: int,interface_id: int,interface_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult,**kwargs) -> Any
```
This method is executed as the 9. step of a run cycle. It's called once per related (execute_on and execute_on_type) interface.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the related nornir device
\
__param__ device_id (int): id of the related device
\
__param__ interface_id (int): id of the current interface
\
__param__ interface_result ([ProviderInterfaceResult], optional): ProviderInterfaceResult with the result of step 6

\
__return__: results or exceptions are stored in a ProviderInterfaceResult object

----------
```python
run_on_nornir_device(self,execute_on: List[int],execute_on_type: neops.core.provider.base.enum.RunOnEnum,dry_run: bool,task_input_kwargs: Dict[Any, Any],search_query: str,task_kwargs: Dict[Any, Any],task: nornir.core.task.Task,nornir_device_id: int,nornir_device_result=neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult,**kwargs) -> Any
```
This method is executed as the 11. step of a run cycle. It's called once per related (execute_on and execute_on_type) nornir_device.

A nornir_device is in the most cases the same as a device, except you have controller configured devices, then it's the controller itself or in otherwords where configurations are applied.

Nornir devices are executed and threaded with nornir task runner.

\
__param__ execute_on (List[int]): ids on which elements the task is executed
\
__param__ execute_on_type (RunOnEnum): on which entity type the task is executed
\
__param__ dry_run (bool): defines if no changes should be applied (especially for configuration tasks)
\
__param__ task_input_kwargs (Dict[Any, Any]): additional input arguments per task
\
__param__ search_query (str): search query to limit elements to run on
\
__param__ task_kwargs (Dict[Any, Any]): task arguments
\
__param__ task (Task): nornir Task object
\
__param__ nornir_device_id (int): id of the current nornir device
\
__param__ nornir_device_result ([ProviderNornirDeviceResult], optional): ProviderNornirDeviceResult with the result of step 4

\
__return__: results or exceptions are stored in a ProviderNornirDeviceResult object

----------