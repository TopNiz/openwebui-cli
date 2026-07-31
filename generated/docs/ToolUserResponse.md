# ToolUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**meta** | [**ToolMeta**](ToolMeta.md) |  | 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.tool_user_response import ToolUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolUserResponse from a JSON string
tool_user_response_instance = ToolUserResponse.from_json(json)
# print the JSON string representation of the object
print(ToolUserResponse.to_json())

# convert the object into a dict
tool_user_response_dict = tool_user_response_instance.to_dict()
# create an instance of ToolUserResponse from a dict
tool_user_response_from_dict = ToolUserResponse.from_dict(tool_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


