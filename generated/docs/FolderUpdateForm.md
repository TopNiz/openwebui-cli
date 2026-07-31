# FolderUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.folder_update_form import FolderUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateForm from a JSON string
folder_update_form_instance = FolderUpdateForm.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateForm.to_json())

# convert the object into a dict
folder_update_form_dict = folder_update_form_instance.to_dict()
# create an instance of FolderUpdateForm from a dict
folder_update_form_from_dict = FolderUpdateForm.from_dict(folder_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


