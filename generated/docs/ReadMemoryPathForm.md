# ReadMemoryPathForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**type** | **str** |  | [optional] [default to 'all']
**include_children** | **bool** |  | [optional] [default to True]
**limit** | **int** |  | [optional] [default to 50]

## Example

```python
from openwebui_client.models.read_memory_path_form import ReadMemoryPathForm

# TODO update the JSON string below
json = "{}"
# create an instance of ReadMemoryPathForm from a JSON string
read_memory_path_form_instance = ReadMemoryPathForm.from_json(json)
# print the JSON string representation of the object
print(ReadMemoryPathForm.to_json())

# convert the object into a dict
read_memory_path_form_dict = read_memory_path_form_instance.to_dict()
# create an instance of ReadMemoryPathForm from a dict
read_memory_path_form_from_dict = ReadMemoryPathForm.from_dict(read_memory_path_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


