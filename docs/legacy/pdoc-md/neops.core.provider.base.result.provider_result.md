# neops.core.provider.base.result.provider_result
## ProviderResult

### Methods
```python
add_child(self,child: ProviderResult,reverse: bool = True) -> NoneType
```
```python
add_parent(self,parent: ProviderResult,reverse: bool = True) -> NoneType
```
```python
child_has_state(self,state: neops.core.models.execution_result.ExecutionResultStateEnum) -> bool
```
```python
child_has_state_recursive(self,state: neops.core.models.execution_result.ExecutionResultStateEnum) -> bool
```
```python
child_is_failed(self) -> bool
```
```python
child_is_failed_recursive(self) -> bool
```
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
is_failed(self) -> bool
```
```python
parent_is_failed(self) -> bool
```
```python
related_is_failed(self) -> bool
```
```python
set_children_as_failed(self) -> NoneType
```
```python
set_parents_as_failed(self) -> NoneType
```
```python
update(self,pre_run_result: Any = None,result: Any = None,message: str = None,exception: Exception = None,failed: bool = None,state: Union[neops.core.models.execution_result.ExecutionResultStateEnum, neops.core.models.device_execution.DeviceExecutionStateEnum] = None,from_object: ProviderResult = None,reset_result: bool = False,set_children_as_failed: bool = True,set_parents_as_failed: bool = False,overwrite: bool = True) -> NoneType
```
```python
write_result(self,execution_id: int) -> 
```