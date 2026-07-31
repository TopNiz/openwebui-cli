# FunctionWithValvesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**content** | **str** |  | 
**meta** | [**FunctionMeta**](FunctionMeta.md) |  | 
**valves** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to False]
**is_global** | **bool** |  | [optional] [default to False]
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.function_with_valves_model import FunctionWithValvesModel

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionWithValvesModel from a JSON string
function_with_valves_model_instance = FunctionWithValvesModel.from_json(json)
# print the JSON string representation of the object
print(FunctionWithValvesModel.to_json())

# convert the object into a dict
function_with_valves_model_dict = function_with_valves_model_instance.to_dict()
# create an instance of FunctionWithValvesModel from a dict
function_with_valves_model_from_dict = FunctionWithValvesModel.from_dict(function_with_valves_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


