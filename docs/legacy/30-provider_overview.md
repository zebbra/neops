# Provider overview

## Base Providers

Base providers features basic functionality to inherit providers from them.

- [NeopsBaseProvider](Neops Provider Overview/neops.core.provider.base.base.md)
- [NeopsCheckBaseProvider](Neops Provider Overview/neops.core.provider.base.base_check.md)
- [NeopsConfigureBaseProvider](Neops Provider Overview/neops.core.provider.base.base_configure.md)
- [NeopsFactsBaseProvider](Neops Provider Overview/neops.core.provider.base.base_facts.md)

They all include the [Base Run Cycle](/25-provider?id=run-cycle) and the [Base Process Result Cycle](/25-provider?id=result-handling)

- [BaseRunCycle](Neops Provider Overview/neops.core.provider.base.base_run_cycle)
- [BaseProcessResultCycle](Neops Provider Overview/neops.core.provider.base.base_process_result_cycle)

Results are written by the [Base Result Writer](/25-provider?id=result-handling)

- [BaseResultWriter](Neops Provider Overview/neops.core.provider.base.base_result_writer)

## Main Functionality Providers

Those providers are used for the main neops.io functionality.

### Generic Providers

Those providers can be used on all entities, they are mostly to maintain facts and checks.

- [GenericTextFSMFactsV2](Neops Provider Overview/neops.core.provider.generic_textfsm_facts_v2.md)
- [GenericJinjaFactsProvider](Neops Provider Overview/neops.core.provider.generic_jinja_facts.md)
- [GenericJinjaCheckProvider](Neops Provider Overview/neops.core.provider.generic_jinja_check.md)
- [GenericSimpleWorkflow](Neops Provider Overview/neops.core.provider.generic_simple_workflow.md)
- [GenericFromExcel](Neops Provider Overview/neops.core.provider.generic_from_excel.md)
- [GenericReportProvider](Neops Provider Overview/neops.core.provider.generic_report.md)
- [GenericRestFactsProvider](Neops Provider Overview/neops.core.provider.generic_rest_facts.md)

### Device Providers

Those providers are used for device specific functionality.

- [DeviceJinjaConfigureProvider](Neops Provider Overview/neops.core.provider.device_configure_from_jinja.md)
- [DeviceDiscoveryProvider](Neops Provider Overview/neops.core.provider.device_discovery.md)
- [DeviceJinjaExecProvider](Neops Provider Overview/neops.core.provider.device_exec_from_jinja.md)

### Interface Providers

Those providers are used for interface specific functionality.

- [InterfaceJinjaConfigureProvider](Neops Provider Overview/neops.core.provider.interface_configure_from_jinja.md)

### Global Providers

Those providers are used for global functionality.

- [GlobalMail](Neops Provider Overview/neops.core.provider.global_mail.md)

## Additional Providers

### Generic Providers

- [GenericCheckAggregation](Neops Provider Overview/neops.core.provider.generic_check_aggregation.md)
- [GenericPing](Neops Provider Overview/neops.core.provider.generic_ping.md)
- [GenericTextFSMFacts](Neops Provider Overview/neops.core.provider.generic_textfsm_facts.md)

### Device Providers

- [DeviceUpgradeProvider](Neops Provider Overview/neops.core.provider.device_upgrade.md)
- [DeviceUpgradeDirectProvider](Neops Provider Overview/neops.core.provider.device_upgrade_direct.md)
- [DeviceUpgradeUnattendedProvider](Neops Provider Overview/neops.core.provider.device_upgrade_unattended.md)
- [DeviceRestartProvider](Neops Provider Overview/neops.core.provider.device_restart.md)
- [DeviceRommonUpgradeProvider](Neops Provider Overview/neops.core.provider.device_rommon_upgrade.md)
- [DeviceRommonUpgradeUnattendedProvider](Neops Provider Overview/neops.core.provider.device_rommon_upgrade_unattended.md)
- [DeviceStackAutoUpgradeUnattendedProvider](Neops Provider Overview/neops.core.provider.device_stack_auto_upgrade.md)
- [DeviceImageCleanUpProvider](Neops Provider Overview/neops.core.provider.device_image_cleanup.md)
- [DeviceRollbackProvider](Neops Provider Overview/neops.core.provider.device_rollback.md)
- [DeviceNapalmFacts](Neops Provider Overview/neops.core.provider.device_napalm_facts.md)
- [DeviceSNMPFactsProvider](Neops Provider Overview/neops.core.provider.device_snmp_facts.md)
