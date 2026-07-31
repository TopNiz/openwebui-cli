# ChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**title** | **str** |  | 
**chat** | **Dict[str, object]** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**share_id** | **str** |  | [optional] 
**archived** | **bool** |  | 
**pinned** | **bool** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**variables** | **Dict[str, object]** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**tasks** | **List[object]** |  | [optional] 
**summary** | **str** |  | [optional] 
**current_message_id** | **str** |  | [optional] 
**context_usage** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.chat_response import ChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatResponse from a JSON string
chat_response_instance = ChatResponse.from_json(json)
# print the JSON string representation of the object
print(ChatResponse.to_json())

# convert the object into a dict
chat_response_dict = chat_response_instance.to_dict()
# create an instance of ChatResponse from a dict
chat_response_from_dict = ChatResponse.from_dict(chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


