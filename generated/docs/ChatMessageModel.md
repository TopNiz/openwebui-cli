# ChatMessageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chat_id** | **str** |  | 
**user_id** | **str** |  | 
**role** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**content** | [**AnyOf**](AnyOf.md) |  | [optional] 
**output** | **List[object]** |  | [optional] 
**model_id** | **str** |  | [optional] 
**files** | **List[object]** |  | [optional] 
**sources** | **List[object]** |  | [optional] 
**embeds** | **List[object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**done** | **bool** |  | [optional] [default to True]
**status_history** | **List[object]** |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**usage** | **Dict[str, object]** |  | [optional] 
**context_summary** | **str** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.chat_message_model import ChatMessageModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageModel from a JSON string
chat_message_model_instance = ChatMessageModel.from_json(json)
# print the JSON string representation of the object
print(ChatMessageModel.to_json())

# convert the object into a dict
chat_message_model_dict = chat_message_model_instance.to_dict()
# create an instance of ChatMessageModel from a dict
chat_message_model_from_dict = ChatMessageModel.from_dict(chat_message_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


