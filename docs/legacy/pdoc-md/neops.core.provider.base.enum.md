# neops.core.provider.base.enum
## ExpandElement
An enumeration.

----------

### Class variables
```python
CLIENTS_ON_INTERFACES
```
```python
CLIENTS_ON_LOCATIONS
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
intersects(list1: List[ExpandElement],list2: List[ExpandElement]) -> 
```
```python
resolve(key: str) -> neops.core.provider.base.enum.ExpandElement
```
```python
resolve_for(key: str,selection: List[ExpandElement]) -> Union[neops.core.provider.base.enum.ExpandElement, NoneType]
```
## ProviderTypeEnum
An enumeration.

----------

### Class variables
```python
CHECK
```
```python
CONFIGURE
```
```python
EXECUTE
```
```python
FACTS
```
```python
NONE
```
### Instance variables
```python
is_check
```
```python
is_configure
```
```python
is_execute
```
```python
is_facts
```
```python
is_none
```
### Functions
```python
resolve(key: str) -> neops.core.provider.base.enum.ProviderTypeEnum
```
## RunOnEnum
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
GENERIC
```
```python
GLOBAL
```
```python
GROUP
```
```python
INTERFACE
```
### Instance variables
```python
is_client
```
```python
is_device
```
```python
is_generic
```
```python
is_global
```
```python
is_group
```
```python
is_interface
```
### Functions
```python
resolve(key: str) -> neops.core.provider.base.enum.RunOnEnum
```
```python
resolve_for(key: str,selection: List[RunOnEnum]) -> Union[neops.core.provider.base.enum.RunOnEnum, NoneType]
```