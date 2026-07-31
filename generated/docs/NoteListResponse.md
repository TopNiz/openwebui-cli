# NoteListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NoteUserResponse]**](NoteUserResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.note_list_response import NoteListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteListResponse from a JSON string
note_list_response_instance = NoteListResponse.from_json(json)
# print the JSON string representation of the object
print(NoteListResponse.to_json())

# convert the object into a dict
note_list_response_dict = note_list_response_instance.to_dict()
# create an instance of NoteListResponse from a dict
note_list_response_from_dict = NoteListResponse.from_dict(note_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


