# SettingsPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **bool** |  | [optional] [default to True]

## Example

```python
from openwebui_client.models.settings_permissions import SettingsPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsPermissions from a JSON string
settings_permissions_instance = SettingsPermissions.from_json(json)
# print the JSON string representation of the object
print(SettingsPermissions.to_json())

# convert the object into a dict
settings_permissions_dict = settings_permissions_instance.to_dict()
# create an instance of SettingsPermissions from a dict
settings_permissions_from_dict = SettingsPermissions.from_dict(settings_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


