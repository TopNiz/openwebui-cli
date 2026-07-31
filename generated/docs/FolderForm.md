# FolderForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.folder_form import FolderForm

# TODO update the JSON string below
json = "{}"
# create an instance of FolderForm from a JSON string
folder_form_instance = FolderForm.from_json(json)
# print the JSON string representation of the object
print(FolderForm.to_json())

# convert the object into a dict
folder_form_dict = folder_form_instance.to_dict()
# create an instance of FolderForm from a dict
folder_form_from_dict = FolderForm.from_dict(folder_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


