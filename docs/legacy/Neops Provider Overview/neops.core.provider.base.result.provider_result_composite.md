# neops.core.provider.base.result.provider_result_composite
## ProviderResultsComposite

### Methods
```python
get_client_result(self,client_id: int) -> neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult
```
```python
get_device_group_result(self,device_group_id: int) -> neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult
```
```python
get_device_result(self,device_id: int) -> neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult
```
```python
get_interface_result(self,interface_id: int) -> neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult
```
```python
get_nornir_device_result(self,nornir_device_id: int) -> neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult
```
```python
load_from_db(self,execution_id: int,pre_check_as_failed: bool = False,post_check_as_failed: bool = False) -> 
```
```python
merge(self,merge_object: ProviderResultsComposite) -> NoneType
```
```python
reset_result(self) -> NoneType
```
```python
set_client_interface_relation(self,client_id: int,interface_id: int) -> NoneType
```
```python
set_client_location_relation(self,client_id: int,location_id: int) -> NoneType
```
```python
set_device_device_group_relation(self,device_id: int,device_group_id: int) -> NoneType
```
```python
set_device_nornir_device_relation(self,device_id: int,nornir_device_id: int) -> NoneType
```
```python
set_interface_device_relation(self,interface_id: int,device_id: int) -> NoneType
```
```python
update_client_result(self,client_id: int,**kwargs) -> NoneType
```
```python
update_device_group_result(self,device_group_id: int,**kwargs) -> NoneType
```
```python
update_device_result(self,device_id: int,**kwargs) -> NoneType
```
```python
update_interface_result(self,interface_id: int,**kwargs) -> NoneType
```
```python
update_nornir_device_result(self,nornir_device_id: int,**kwargs) -> NoneType
```
```python
upsert_client_result(self,client_id: int,**kwargs) -> NoneType
```
```python
upsert_device_group_result(self,device_group_id: int,**kwargs) -> NoneType
```
```python
upsert_device_result(self,device_id: int,**kwargs) -> NoneType
```
```python
upsert_interface_result(self,interface_id: int,**kwargs) -> NoneType
```
```python
upsert_nornir_device_result(self,nornir_device_id: int,**kwargs) -> NoneType
```