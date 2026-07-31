# FeaturesPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | **bool** |  | [optional] [default to False]
**notes** | **bool** |  | [optional] [default to True]
**channels** | **bool** |  | [optional] [default to True]
**folders** | **bool** |  | [optional] [default to True]
**direct_tool_servers** | **bool** |  | [optional] [default to False]
**web_search** | **bool** |  | [optional] [default to True]
**image_generation** | **bool** |  | [optional] [default to True]
**code_interpreter** | **bool** |  | [optional] [default to True]
**memories** | **bool** |  | [optional] [default to True]
**automations** | **bool** |  | [optional] [default to False]
**calendar** | **bool** |  | [optional] [default to True]
**webhooks** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.features_permissions import FeaturesPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturesPermissions from a JSON string
features_permissions_instance = FeaturesPermissions.from_json(json)
# print the JSON string representation of the object
print(FeaturesPermissions.to_json())

# convert the object into a dict
features_permissions_dict = features_permissions_instance.to_dict()
# create an instance of FeaturesPermissions from a dict
features_permissions_from_dict = FeaturesPermissions.from_dict(features_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


