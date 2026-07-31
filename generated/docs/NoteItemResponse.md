# NoteItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**is_pinned** | **bool** |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.note_item_response import NoteItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteItemResponse from a JSON string
note_item_response_instance = NoteItemResponse.from_json(json)
# print the JSON string representation of the object
print(NoteItemResponse.to_json())

# convert the object into a dict
note_item_response_dict = note_item_response_instance.to_dict()
# create an instance of NoteItemResponse from a dict
note_item_response_from_dict = NoteItemResponse.from_dict(note_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


