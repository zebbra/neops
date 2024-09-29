# neops.core.provider.device_rommon_upgrade
## DeviceRommonUpgradeProvider
Provider to Upgrade Rommon of Cisco Devices

----------
### JSON Schema
#### Device Upgrade ROMMON


##### Properties


- **`source_url`** *(string)*: from this URL the image will be loaded.


----------
### Run Input JSON Schema
#### Device Upgrade ROMMON


##### Properties


- **`image`** *(string)*: from this URL the image will be loaded.

- **`md5`** *(string)*: MD5 sum to verify. Default: ``.

- **`min_space`** *(integer)*: minimum file size required. Default: `0`.

- **`overwrite`** *(boolean)*: overwrite image if file exists on device. Default: `False`.

- **`restart`** *(boolean)*: restart device when image is copied and installed. Default: `False`.

- **`vrf`** *(string)*: VRF where we should copy. Default: ``.
