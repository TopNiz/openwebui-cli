# ChatBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | [**ChatHistoryStats**](ChatHistoryStats.md) |  | 

## Example

```python
from openwebui_client.models.chat_body import ChatBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBody from a JSON string
chat_body_instance = ChatBody.from_json(json)
# print the JSON string representation of the object
print(ChatBody.to_json())

# convert the object into a dict
chat_body_dict = chat_body_instance.to_dict()
# create an instance of ChatBody from a dict
chat_body_from_dict = ChatBody.from_dict(chat_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


