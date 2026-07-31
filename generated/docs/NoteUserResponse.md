# NoteUserResponse


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
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.note_user_response import NoteUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteUserResponse from a JSON string
note_user_response_instance = NoteUserResponse.from_json(json)
# print the JSON string representation of the object
print(NoteUserResponse.to_json())

# convert the object into a dict
note_user_response_dict = note_user_response_instance.to_dict()
# create an instance of NoteUserResponse from a dict
note_user_response_from_dict = NoteUserResponse.from_dict(note_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


