# FunctionForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 
**meta** | [**FunctionMeta**](FunctionMeta.md) |  | 

## Example

```python
from openwebui_client.models.function_form import FunctionForm

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionForm from a JSON string
function_form_instance = FunctionForm.from_json(json)
# print the JSON string representation of the object
print(FunctionForm.to_json())

# convert the object into a dict
function_form_dict = function_form_instance.to_dict()
# create an instance of FunctionForm from a dict
function_form_from_dict = FunctionForm.from_dict(function_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


