# FunctionUserResponse


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
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.function_user_response import FunctionUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionUserResponse from a JSON string
function_user_response_instance = FunctionUserResponse.from_json(json)
# print the JSON string representation of the object
print(FunctionUserResponse.to_json())

# convert the object into a dict
function_user_response_dict = function_user_response_instance.to_dict()
# create an instance of FunctionUserResponse from a dict
function_user_response_from_dict = FunctionUserResponse.from_dict(function_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


