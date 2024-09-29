# neops.core.provider.base.result.coupled_provider_result_types
## ProviderClientResult

### Methods
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
set_interface(self,interface: ProviderInterfaceResult,reverse: bool = True) -> NoneType
```
```python
set_location(self,location: ProviderDeviceGroupResult,reverse: bool = True) -> NoneType
```
```python
write_result(self,execution_id: int,neops_task_id: Optional[int] = None,granularity: int = 5) -> 
```
## ProviderDeviceGroupResult

### Methods
```python
add_client(self,client: ProviderClientResult,reverse: bool = True) -> NoneType
```
```python
add_device(self,device: ProviderDeviceResult,reverse: bool = True) -> NoneType
```
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
write_result(self,execution_id: int,neops_task_id: Optional[int] = None,granularity: int = 5) -> 
```
## ProviderDeviceResult

### Methods
```python
add_device_group(self,device_group: "'ProviderDeviceGroupResult'",reverse: bool = True) -> NoneType
```
```python
add_interface(self,interface: ProviderInterfaceResult,reverse: bool = True) -> NoneType
```
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
set_nornir_device(self,nornir_device: "'ProviderNornirDeviceResult'",reverse: bool = True) -> NoneType
```
```python
write_result(self,execution_id: int,neops_task_id: Optional[int] = None,granularity: int = 5) -> 
```
## ProviderInterfaceResult

### Methods
```python
add_client(self,client: "'ProviderClientResult'",reverse: bool = True) -> NoneType
```
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
set_device(self,device: "'ProviderDeviceResult'",reverse: bool = True) -> NoneType
```
```python
write_result(self,execution_id: int,neops_task_id: Optional[int] = None,granularity: int = 5) -> 
```
## ProviderNornirDeviceResult

### Methods
```python
add_device(self,device: ProviderDeviceResult,reverse: bool = True) -> NoneType
```
```python
get_ran_on(self) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```
```python
write_result(self,execution_id: int,neops_task_id: Optional[int] = None,granularity: int = 5) -> 
```