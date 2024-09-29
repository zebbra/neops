# neops.core.provider.device_discovery
## DeviceDiscoveryProvider
Discover a device and populate datastructures.

- `Recursive`: _Try to connect to neighbor devices (found with CDP and LLDP, with the same credentials),
if the connection is successful add the device to neops_
- `Interface Discovery`: _Populates and updates the interface data structures_
- `Neighbor Discovery`: _Set relations between interfaces based on CDP and LLDP neighborships_
- `Client Discovery`: _Add Clients to neops.io based on Mac Address-Table information_
- `Get Configuration`: _Backup of Device and Interface Configurations to neops.io_

----------
### JSON Schema
#### Device Discovery


##### Properties


- **`recursive`** *(boolean)*: discover and add neighbors with same credentials as well. Default: `False`.

- **`include_interfaces`** *(boolean)*: discover interfaces of the device. Default: `True`.

- **`include_neighbors`** *(boolean)*: discover neighbors and set edges between devices. Default: `True`.

- **`include_clients`** *(boolean)*: discover network clients and assign to interfaces. Default: `True`.

- **`get_config`** *(boolean)*: get the configuration and update database. Default: `True`.

### Methods
```python
run_on_nornir_device(self,task: nornir.core.task.Task,execute_on: List = None,**kwargs) -> NoneType
```
`run_on_nornir_device` is called by the run cycle.
It discovers the network elements

----------