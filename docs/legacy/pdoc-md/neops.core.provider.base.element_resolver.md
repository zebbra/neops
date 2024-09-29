# neops.core.provider.base.element_resolver
## ElementResolver

### Methods
```python
resolve_execute(self,resolve_on: ResolveOn,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> Union[List[int], NoneType]
```
This method calls the right resolver based on resolve_on
\
__param__ resolve_on:
\
__param__ execute_on:
\
__param__ execute_on_type:
\
__param__ invert_filter:
\
__return__:

----------
```python
resolve_execute_on_clients(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_execute_on_clients_of_group(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_execute_on_clients_of_interface(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_execute_on_devices(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_execute_on_groups(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> Union[List[int], NoneType]
```
```python
resolve_execute_on_interfaces(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_execute_on_nornir_devices(self,execute_on: List,execute_on_type: RunOnEnum,invert_filter: bool = False) -> List[int]
```
```python
resolve_related_elements(self,resolve_by: ResolveBy,element_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> Union[List[int], NoneType]
```
This method calls the right resolver based on resolve_by
\
__param__ resolve_by:
\
__param__ element_id:
\
__param__ execute_on:
\
__param__ resolve_related_on:
\
__return__:

----------
```python
resolve_related_elements_by_client(self,client_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> List[int]
```
```python
resolve_related_elements_by_device(self,device_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> List
```
```python
resolve_related_elements_by_device_group(self,device_group_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> List[int]
```
```python
resolve_related_elements_by_interface(self,interface_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> List[int]
```
```python
resolve_related_elements_by_nornir_device(self,nornir_device_id: int,execute_on: List,resolve_related_on: RunOnEnum = None) -> List[int]
```
## ResolveBy
An enumeration.

----------

### Class variables
```python
CLIENT
```
```python
DEVICE
```
```python
DEVICE_GROUP
```
```python
INTERFACE
```
```python
NORNIR_DEVICE
```
### Functions
```python
resolve(key: str) -> neops.core.provider.base.element_resolver.ResolveBy
```
## ResolveOn
An enumeration.

----------

### Class variables
```python
CLIENTS
```
```python
DEVICES
```
```python
GROUPS
```
```python
INTERFACES
```
```python
NORNIR_DEVICES
```
### Functions
```python
resolve(key: str) -> neops.core.provider.base.element_resolver.ResolveOn
```