# NoteModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**title** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.note_model import NoteModel

# TODO update the JSON string below
json = "{}"
# create an instance of NoteModel from a JSON string
note_model_instance = NoteModel.from_json(json)
# print the JSON string representation of the object
print(NoteModel.to_json())

# convert the object into a dict
note_model_dict = note_model_instance.to_dict()
# create an instance of NoteModel from a dict
note_model_from_dict = NoteModel.from_dict(note_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


