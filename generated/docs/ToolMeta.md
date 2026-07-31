# ToolMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**manifest** | **Dict[str, object]** |  | [optional] 
**has_user_valves** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.tool_meta import ToolMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ToolMeta from a JSON string
tool_meta_instance = ToolMeta.from_json(json)
# print the JSON string representation of the object
print(ToolMeta.to_json())

# convert the object into a dict
tool_meta_dict = tool_meta_instance.to_dict()
# create an instance of ToolMeta from a dict
tool_meta_from_dict = ToolMeta.from_dict(tool_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


