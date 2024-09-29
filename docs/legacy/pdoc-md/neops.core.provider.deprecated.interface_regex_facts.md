# neops.core.provider.deprecated.interface_regex_facts
## InterfaceRegexFactsProvider
This Provider is inherited from the `NeopsBaseProvider`, it brings additional functionality to handle facts (flexible data structures per entity).

Every task based on this provider needs a facts key where the facts result is stored in the database per element.

For providers inherits from this provider the facts results are written automatically based on the result set of the pre- and run methods per element.
It supports data structures of any kind as long as they are compatible to JSON.

This provider should be the base for fact providers. So if you create a new fact provider with, either extend this `NeopsFactsBaseProvider` or a concrete fact provider

----------
### JSON Schema
#### Add Structured Command to Facts


##### Properties


- **`facts_key`** *(string)*: Set the key where the facts are saved.

- **`command`** *(string)*: Show command to convert to structured data, use $interface$ as variable for interface name .

- **`regex`** *(string)*: Regular expression.

- **`regex_ignore`** *(boolean)*: Regular expression case sensitive or not. Default: `False`.

- **`regex_multi`** *(boolean)*: Regular expression multiline or not. Default: `False`.

- **`regex_dotall`** *(boolean)*: Dot stands for special characters as well. Default: `False`.

- **`match_keys`** *(array)*: map the matches to keys,
                if multiple (for OR in regex without match use (?:expr1|expr2) ).

  - **Items** *(string)*
