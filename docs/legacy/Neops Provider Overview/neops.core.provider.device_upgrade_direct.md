# neops.core.provider.device_upgrade_direct
## DeviceUpgradeDirectProvider
Provider to upgrade device image (without dry run)

----------
### JSON Schema
#### Device Upgrade


##### Properties


- **`source_url`** *(string)*: from this URL the image will be loaded.


----------
### Run Input JSON Schema
#### Device Upgrade


##### Properties


- **`image`** *(string)*: from this URL the image will be loaded.

- **`md5`** *(string)*: MD5 sum to verify. Default: ``.

- **`min_space`** *(integer)*: minimum file size required. Default: `0`.

- **`overwrite`** *(boolean)*: overwrite image if file exists on device. Default: `False`.

- **`restart`** *(boolean)*: restart device when image is copied and installed. Default: `False`.

- **`vrf`** *(string)*: VRF where we should copy. Default: ``.

- **`save_config_if_required`** *(boolean)*: Save config before restart if asked so. Default: `True`.
