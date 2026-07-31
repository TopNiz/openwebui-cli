# NoteForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.note_form import NoteForm

# TODO update the JSON string below
json = "{}"
# create an instance of NoteForm from a JSON string
note_form_instance = NoteForm.from_json(json)
# print the JSON string representation of the object
print(NoteForm.to_json())

# convert the object into a dict
note_form_dict = note_form_instance.to_dict()
# create an instance of NoteForm from a dict
note_form_from_dict = NoteForm.from_dict(note_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


