# ModelChatEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**first_message** | **str** |  | [optional] 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.model_chat_entry import ModelChatEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChatEntry from a JSON string
model_chat_entry_instance = ModelChatEntry.from_json(json)
# print the JSON string representation of the object
print(ModelChatEntry.to_json())

# convert the object into a dict
model_chat_entry_dict = model_chat_entry_instance.to_dict()
# create an instance of ModelChatEntry from a dict
model_chat_entry_from_dict = ModelChatEntry.from_dict(model_chat_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


