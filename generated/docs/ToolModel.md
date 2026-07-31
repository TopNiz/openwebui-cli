# ToolModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**content** | **str** |  | [optional] 
**specs** | **List[Optional[Dict[str, object]]]** |  | 
**meta** | [**ToolMeta**](ToolMeta.md) |  | 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.tool_model import ToolModel

# TODO update the JSON string below
json = "{}"
# create an instance of ToolModel from a JSON string
tool_model_instance = ToolModel.from_json(json)
# print the JSON string representation of the object
print(ToolModel.to_json())

# convert the object into a dict
tool_model_dict = tool_model_instance.to_dict()
# create an instance of ToolModel from a dict
tool_model_from_dict = ToolModel.from_dict(tool_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


