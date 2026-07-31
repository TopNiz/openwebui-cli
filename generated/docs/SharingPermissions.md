# SharingPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **bool** |  | [optional] [default to False]
**public_models** | **bool** |  | [optional] [default to False]
**knowledge** | **bool** |  | [optional] [default to False]
**public_knowledge** | **bool** |  | [optional] [default to False]
**prompts** | **bool** |  | [optional] [default to False]
**public_prompts** | **bool** |  | [optional] [default to False]
**tools** | **bool** |  | [optional] [default to False]
**public_tools** | **bool** |  | [optional] [default to True]
**skills** | **bool** |  | [optional] [default to False]
**public_skills** | **bool** |  | [optional] [default to False]
**notes** | **bool** |  | [optional] [default to False]
**public_notes** | **bool** |  | [optional] [default to True]
**folders** | **bool** |  | [optional] [default to False]
**public_chats** | **bool** |  | [optional] [default to False]
**public_calendars** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.sharing_permissions import SharingPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of SharingPermissions from a JSON string
sharing_permissions_instance = SharingPermissions.from_json(json)
# print the JSON string representation of the object
print(SharingPermissions.to_json())

# convert the object into a dict
sharing_permissions_dict = sharing_permissions_instance.to_dict()
# create an instance of SharingPermissions from a dict
sharing_permissions_from_dict = SharingPermissions.from_dict(sharing_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


