# NoteAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.note_access_grants_form import NoteAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of NoteAccessGrantsForm from a JSON string
note_access_grants_form_instance = NoteAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(NoteAccessGrantsForm.to_json())

# convert the object into a dict
note_access_grants_form_dict = note_access_grants_form_instance.to_dict()
# create an instance of NoteAccessGrantsForm from a dict
note_access_grants_form_from_dict = NoteAccessGrantsForm.from_dict(note_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


