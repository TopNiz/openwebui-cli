# ListMemoryPathsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'all']
**limit** | **int** |  | [optional] [default to 100]

## Example

```python
from openwebui_client.models.list_memory_paths_form import ListMemoryPathsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ListMemoryPathsForm from a JSON string
list_memory_paths_form_instance = ListMemoryPathsForm.from_json(json)
# print the JSON string representation of the object
print(ListMemoryPathsForm.to_json())

# convert the object into a dict
list_memory_paths_form_dict = list_memory_paths_form_instance.to_dict()
# create an instance of ListMemoryPathsForm from a dict
list_memory_paths_form_from_dict = ListMemoryPathsForm.from_dict(list_memory_paths_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


