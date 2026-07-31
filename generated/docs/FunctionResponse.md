# FunctionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**type** | **str** |  | 
**name** | **str** |  | 
**meta** | [**FunctionMeta**](FunctionMeta.md) |  | 
**is_active** | **bool** |  | 
**is_global** | **bool** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.function_response import FunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionResponse from a JSON string
function_response_instance = FunctionResponse.from_json(json)
# print the JSON string representation of the object
print(FunctionResponse.to_json())

# convert the object into a dict
function_response_dict = function_response_instance.to_dict()
# create an instance of FunctionResponse from a dict
function_response_from_dict = FunctionResponse.from_dict(function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


