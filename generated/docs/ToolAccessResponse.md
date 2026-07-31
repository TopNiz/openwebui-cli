# ToolAccessResponse


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
**write_access** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.tool_access_response import ToolAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAccessResponse from a JSON string
tool_access_response_instance = ToolAccessResponse.from_json(json)
# print the JSON string representation of the object
print(ToolAccessResponse.to_json())

# convert the object into a dict
tool_access_response_dict = tool_access_response_instance.to_dict()
# create an instance of ToolAccessResponse from a dict
tool_access_response_from_dict = ToolAccessResponse.from_dict(tool_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


