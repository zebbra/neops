# neops.core.provider.registry
### Module functions
```python
get_provider(name: str) -> Union[Dict, NoneType]
```
```python
get_providers() -> 
```
```python
register_provider(cls) -> 
```
Register a neops provider. Tasks can be registered for specific vendors and (also optional) specific models.
This decorator only adds a marker attribute on the function, the provider_loader.load_providers function builds the
actual registry. This way we can enforce the correct order of the tasks (default builtin neops providers, after that
all tasks loaded from the NEOPS_PROVIDER_MODULES), and do not depend on the import order of the modules.

----------