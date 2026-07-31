# ChatPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controls** | **bool** |  | [optional] [default to True]
**valves** | **bool** |  | [optional] [default to True]
**system_prompt** | **bool** |  | [optional] [default to True]
**params** | **bool** |  | [optional] [default to True]
**file_upload** | **bool** |  | [optional] [default to True]
**web_upload** | **bool** |  | [optional] [default to True]
**delete** | **bool** |  | [optional] [default to True]
**delete_message** | **bool** |  | [optional] [default to True]
**continue_response** | **bool** |  | [optional] [default to True]
**regenerate_response** | **bool** |  | [optional] [default to True]
**rate_response** | **bool** |  | [optional] [default to True]
**edit** | **bool** |  | [optional] [default to True]
**share** | **bool** |  | [optional] [default to True]
**export** | **bool** |  | [optional] [default to True]
**var_import** | **bool** |  | [optional] [default to True]
**stt** | **bool** |  | [optional] [default to True]
**tts** | **bool** |  | [optional] [default to True]
**call** | **bool** |  | [optional] [default to True]
**multiple_models** | **bool** |  | [optional] [default to True]
**temporary** | **bool** |  | [optional] [default to True]
**temporary_enforced** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.chat_permissions import ChatPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ChatPermissions from a JSON string
chat_permissions_instance = ChatPermissions.from_json(json)
# print the JSON string representation of the object
print(ChatPermissions.to_json())

# convert the object into a dict
chat_permissions_dict = chat_permissions_instance.to_dict()
# create an instance of ChatPermissions from a dict
chat_permissions_from_dict = ChatPermissions.from_dict(chat_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


