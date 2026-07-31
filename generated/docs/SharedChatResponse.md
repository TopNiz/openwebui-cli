# SharedChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chat_id** | **str** |  | 
**title** | **str** |  | 
**share_id** | **str** |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.shared_chat_response import SharedChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SharedChatResponse from a JSON string
shared_chat_response_instance = SharedChatResponse.from_json(json)
# print the JSON string representation of the object
print(SharedChatResponse.to_json())

# convert the object into a dict
shared_chat_response_dict = shared_chat_response_instance.to_dict()
# create an instance of SharedChatResponse from a dict
shared_chat_response_from_dict = SharedChatResponse.from_dict(shared_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


