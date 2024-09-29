# Provider overview

## Base Providers

Base providers features basic functionality to inherit providers from them.

- [NeopsBaseProvider](pdoc-md/neops.core.provider.base.base.md)
- [NeopsCheckBaseProvider](pdoc-md/neops.core.provider.base.base_check.md)
- [NeopsConfigureBaseProvider](pdoc-md/neops.core.provider.base.base_configure.md)
- [NeopsFactsBaseProvider](pdoc-md/neops.core.provider.base.base_facts.md)

They all include the [Base Run Cycle](/25-provider?id=run-cycle) and the [Base Process Result Cycle](/25-provider?id=result-handling)

- [BaseRunCycle](pdoc-md/neops.core.provider.base.base_run_cycle)
- [BaseProcessResultCycle](pdoc-md/neops.core.provider.base.base_process_result_cycle)

Results are written by the [Base Result Writer](/25-provider?id=result-handling)

- [BaseResultWriter](pdoc-md/neops.core.provider.base.base_result_writer)

## Main Functionality Providers

Those providers are used for the main neops.io functionality.

### Generic Providers

Those providers can be used on all entities, they are mostly to maintain facts and checks.

- [GenericTextFSMFactsV2](pdoc-md/neops.core.provider.generic_textfsm_facts_v2.md)
- [GenericJinjaFactsProvider](pdoc-md/neops.core.provider.generic_jinja_facts.md)
- [GenericJinjaCheckProvider](pdoc-md/neops.core.provider.generic_jinja_check.md)
- [GenericSimpleWorkflow](pdoc-md/neops.core.provider.generic_simple_workflow.md)
- [GenericFromExcel](pdoc-md/neops.core.provider.generic_from_excel.md)
- [GenericReportProvider](pdoc-md/neops.core.provider.generic_report.md)
- [GenericRestFactsProvider](pdoc-md/neops.core.provider.generic_rest_facts.md)

### Device Providers

Those providers are used for device specific functionality.

- [DeviceJinjaConfigureProvider](pdoc-md/neops.core.provider.device_configure_from_jinja.md)
- [DeviceDiscoveryProvider](pdoc-md/neops.core.provider.device_discovery.md)
- [DeviceJinjaExecProvider](pdoc-md/neops.core.provider.device_exec_from_jinja.md)

### Interface Providers

Those providers are used for interface specific functionality.

- [InterfaceJinjaConfigureProvider](pdoc-md/neops.core.provider.interface_configure_from_jinja.md)

### Global Providers

Those providers are used for global functionality.

- [GlobalMail](pdoc-md/neops.core.provider.global_mail.md)

## Additional Providers

### Generic Providers

- [GenericCheckAggregation](pdoc-md/neops.core.provider.generic_check_aggregation.md)
- [GenericPing](pdoc-md/neops.core.provider.generic_ping.md)
- [GenericTextFSMFacts](pdoc-md/neops.core.provider.generic_textfsm_facts.md)

### Device Providers

- [DeviceUpgradeProvider](pdoc-md/neops.core.provider.device_upgrade.md)
- [DeviceUpgradeDirectProvider](pdoc-md/neops.core.provider.device_upgrade_direct.md)
- [DeviceUpgradeUnattendedProvider](pdoc-md/neops.core.provider.device_upgrade_unattended.md)
- [DeviceRestartProvider](pdoc-md/neops.core.provider.device_restart.md)
- [DeviceRommonUpgradeProvider](pdoc-md/neops.core.provider.device_rommon_upgrade.md)
- [DeviceRommonUpgradeUnattendedProvider](pdoc-md/neops.core.provider.device_rommon_upgrade_unattended.md)
- [DeviceStackAutoUpgradeUnattendedProvider](pdoc-md/neops.core.provider.device_stack_auto_upgrade.md)
- [DeviceImageCleanUpProvider](pdoc-md/neops.core.provider.device_image_cleanup.md)
- [DeviceRollbackProvider](pdoc-md/neops.core.provider.device_rollback.md)
- [DeviceNapalmFacts](pdoc-md/neops.core.provider.device_napalm_facts.md)
- [DeviceSNMPFactsProvider](pdoc-md/neops.core.provider.device_snmp_facts.md)
