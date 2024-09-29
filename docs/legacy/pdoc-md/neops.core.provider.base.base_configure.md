# neops.core.provider.base.base_configure
## NeopsConfigureBaseProvider
This provider extends the NeopsBaseProvider by the functionality of storing configurations (on device results)
to the device it self by different apply methods.

This provider should be the base for configuration providers. So if you create a new configuration provider with,
either extend this `NeopsConfigureBaseProvider` or a concrete configuration provider

----------
### Global Base Configure Parameters
#### Apply Method

The apply method descripbes how the configuration is written to the device.

* `cli`: the configuration is applied directly in the configration mode
* `scp`: the configuration is copied (with scp) as a file to the device and applied with an merge operation
* `scp-startup`: the configuration is copied (with scp) as a file to the device and written to the start up
configuration


#### Slow Devices

With the `slow_device` parameter you can specify a delay factor to wait a longer time on responses from
            slow devices

----------
### JSON Schema
#### Configure Base Provider


##### Properties


- **`apply`** *(string)*: Method how to apply the configuration, over cli or copy with scp and merge. Must be one of: `['scp', 'cli', 'scp-startup']`.

- **`slow_device`** *(integer)*: Add a factor for longer wait times for heavy loaded devices. Default: `0`.

### Methods
```python
run_on_nornir_device(self,task: nornir.core.task.Task,nornir_device_result: neops.core.provider.base.result.coupled_provider_result_types.ProviderNornirDeviceResult,dry_run: bool = True,**kwargs) -> str
```
`run_on_nornir_device` is called by the run cycle.

It takes the result from the `pre_run_on_nornir_device` and from every related device with the
`pre_run_on_device` and `run_on_device` methods and writes the configuration to the device.

----------