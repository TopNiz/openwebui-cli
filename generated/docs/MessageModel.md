# MessageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**reply_to_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_pinned** | **bool** |  | [optional] [default to False]
**pinned_by** | **str** |  | [optional] 
**pinned_at** | **int** |  | [optional] 
**content** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.message_model import MessageModel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageModel from a JSON string
message_model_instance = MessageModel.from_json(json)
# print the JSON string representation of the object
print(MessageModel.to_json())

# convert the object into a dict
message_model_dict = message_model_instance.to_dict()
# create an instance of MessageModel from a dict
message_model_from_dict = MessageModel.from_dict(message_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


