# FunctionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**content** | **str** |  | 
**meta** | [**FunctionMeta**](FunctionMeta.md) |  | 
**is_active** | **bool** |  | [optional] [default to False]
**is_global** | **bool** |  | [optional] [default to False]
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.function_model import FunctionModel

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionModel from a JSON string
function_model_instance = FunctionModel.from_json(json)
# print the JSON string representation of the object
print(FunctionModel.to_json())

# convert the object into a dict
function_model_dict = function_model_instance.to_dict()
# create an instance of FunctionModel from a dict
function_model_from_dict = FunctionModel.from_dict(function_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


