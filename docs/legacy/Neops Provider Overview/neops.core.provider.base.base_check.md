# neops.core.provider.base.base_check
## NeopsCheckBaseProvider
This Provider is inherited from the `NeopsBaseProvider`, it brings additional functionality to handle checks.

Every Task based on this provider needs a check key where the check result is stored in the database per element.

For providers inherits from this provider the check results are written automatically based on the result set
of the pre- and run methods per element.
It supports check results, boolean values and handels exceptions.

This provider should be the base for check providers. So if you create a new check provider with, either
extend this `NeopsCheckBaseProvider` or a concrete check provider

----------
### Check Result
see below

----------
### JSON Schema
#### Check Base Provider


##### Properties


- **`check_key`** *(string)*: Set the key where the check is saved.

### Class variables
```python
based_on_checks
```
If the check result is based on other checks, specify them for trancing.

----------
```python
check_for
```
The entity where the checks are for can be different from the `run_on`, so specify if required otherwise we will
use the `run_on` value.

----------
```python
related_facts
```
Specify on which facts the check result is based on. This enables tracing when and how the values are stored in
neops.io

----------
### Methods
```python
process_client_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult] = None) -> NoneType
```
`process_client_results` is called at the end of the run cycle.
It stores the client results as checks to the database if the `check_for` variable is set to `CLIENT`

----------
```python
process_device_group_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult] = None) -> NoneType
```
`process_device_group_results` is called at the end of the run cycle.
It stores the device group results as checks to the database if the `check_for` variable is set to `GROUP`

----------
```python
process_device_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult] = None) -> NoneType
```
`process_device_results` is called at the end of the run cycle.
It stores the device results as checks to the database if the `check_for` variable is set to `DEVICE`

----------
```python
process_global_result(self,result: nornir.core.task.Result = None) -> NoneType
```
Global checks are currently not supported..

----------
```python
process_interface_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult] = None) -> NoneType
```
`process_interface_results` is called at the end of the run cycle.
It stores the interface results as checks to the database if the `check_for` variable is set to `INTERFACE`

----------
## NeopsCheckResult
A check result contains the result, metrics and a reason for the result of the check.

----------

### Class variables
```python
metrics: Dict
```
additional metrics of this checks, this is a flexible data structure to be used in custom frontends

----------
```python
reason: str
```
the reason for this result

----------
```python
result: neops.core.models.check.CheckResultEnum
```
* OK: the check was executed successfully and fullfills the requirements
* NOK: the check was executed successfull but does not fullfill the requirements
* FAILED: there was an error to perform this check

----------