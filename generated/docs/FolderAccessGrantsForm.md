# FolderAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.folder_access_grants_form import FolderAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of FolderAccessGrantsForm from a JSON string
folder_access_grants_form_instance = FolderAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(FolderAccessGrantsForm.to_json())

# convert the object into a dict
folder_access_grants_form_dict = folder_access_grants_form_instance.to_dict()
# create an instance of FolderAccessGrantsForm from a dict
folder_access_grants_form_from_dict = FolderAccessGrantsForm.from_dict(folder_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


