# ModelChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[ModelChatEntry]**](ModelChatEntry.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.model_chats_response import ModelChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChatsResponse from a JSON string
model_chats_response_instance = ModelChatsResponse.from_json(json)
# print the JSON string representation of the object
print(ModelChatsResponse.to_json())

# convert the object into a dict
model_chats_response_dict = model_chats_response_instance.to_dict()
# create an instance of ModelChatsResponse from a dict
model_chats_response_from_dict = ModelChatsResponse.from_dict(model_chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


