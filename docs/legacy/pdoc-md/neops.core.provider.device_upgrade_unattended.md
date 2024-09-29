# neops.core.provider.device_upgrade_unattended
## DeviceUpgradeUnattendedProvider
Provider to upgrade device image (Unattended, define the values in the task and don't do a dry run)

----------
### JSON Schema
#### Device Upgrade


##### Properties


- **`source_url`** *(string)*: from this URL the image will be loaded.

- **`vrf`** *(string)*: VRF where we should copy. Default: ``.

- **`models`** *(array)*: This description is used as a help message.

  - **Items** *(object)*

    - **`model_regex`** *(string)*: Default: `^$`.

    - **`image`** *(string)*: from this URL the image will be loaded.

    - **`md5`** *(string)*: MD5 sum to verify. Default: ``.

    - **`min_space`** *(integer)*: minimum file size required. Default: `0`.

    - **`overwrite`** *(boolean)*: overwrite image if file exists on device. Default: `False`.

    - **`restart`** *(boolean)*: restart device when image is copied and installed. Default: `False`.

    - **`save_config_if_required`** *(boolean)*: Save config before restart if asked so. Default: `True`.

    - **`reload_wait_time`** *(number)*: How long should the process wait at reload after upgrade. Default: `1200`.
