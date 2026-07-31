# AddMemoryForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | [optional] [default to 'context']
**path** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.add_memory_form import AddMemoryForm

# TODO update the JSON string below
json = "{}"
# create an instance of AddMemoryForm from a JSON string
add_memory_form_instance = AddMemoryForm.from_json(json)
# print the JSON string representation of the object
print(AddMemoryForm.to_json())

# convert the object into a dict
add_memory_form_dict = add_memory_form_instance.to_dict()
# create an instance of AddMemoryForm from a dict
add_memory_form_from_dict = AddMemoryForm.from_dict(add_memory_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


