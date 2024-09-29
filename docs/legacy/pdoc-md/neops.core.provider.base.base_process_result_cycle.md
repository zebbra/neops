# neops.core.provider.base.base_process_result_cycle
## BaseProcessResultCycle
This class describes the methods provided to process different result objects.

They are used for example by the facts or check base providers to save the results to the database.

----------

### Methods
```python
process_client_result(self,result: neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult) -> NoneType
```
This method is called for every client result (does not matters if ran on interface or on group).

\
__param__ result (ProviderClientResult): client result object.

----------
```python
process_client_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderClientResult]) -> NoneType
```
This method is called once with a list of all client results (does not matters if ran on interface or on group).

\
__param__ results (List[ProviderClientResult]): list of client result objects.

----------
```python
process_device_group_result(self,result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult) -> NoneType
```
This method is called for every device group result.

\
__param__ result (ProviderDeviceGroupResult): device group result object.

----------
```python
process_device_group_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceGroupResult]) -> NoneType
```
This method is called once with a list of all device group results.

\
__param__ results (List[ProviderDeviceGroupResult]): list of device group result objects.

----------
```python
process_device_result(self,result: neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult) -> NoneType
```
This method is called for every device result.

\
__param__ result (ProviderDeviceResult): device result object.

----------
```python
process_device_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderDeviceResult]) -> NoneType
```
This method is called once with a list of all device results.

\
__param__ results (List[ProviderDeviceResult]): list of device result objects.

----------
```python
process_global_result(self,result: neops.core.provider.base.result.provider_result.ProviderResult) -> NoneType
```
This method is called once for the global result.

\
__param__ result (ProviderResult): global result object.

----------
```python
process_interface_result(self,result: neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult) -> NoneType
```
This method is called for every interface result.

\
__param__ result (ProviderInterfaceResult): interface result object.

----------
```python
process_interface_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderInterfaceResult]) -> NoneType
```
This method is called once with a list of all interface results.

\
__param__ results (List[ProviderInterfaceResult]): list of interface result objects.

----------
```python
process_nornir_device_result(self,result: neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult) -> NoneType
```
This method is called for every nornir device result.

\
__param__ result (ProviderNornirDeviceResult): nornir device result object.

----------
```python
process_nornir_device_results(self,results: List[neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult]) -> NoneType
```
This method is called once with a list of all nornir device results.

\
__param__ results (List[ProviderNornirDeviceResult]): list of nornir device result objects.

----------