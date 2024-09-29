# neops.core.provider.deprecated.interface_check
## InterfaceCheckProvider
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
#### Check Interface Facts with Regex


##### Properties


- **`check_key`** *(string)*: Set the key where the check is saved.

- **`checks`** *(array)*: This description is used as a help message.

  - **Items** *(object)*

    - **`element`** *(object)*
