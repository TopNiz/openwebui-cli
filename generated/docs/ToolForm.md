# ToolForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 
**meta** | [**ToolMeta**](ToolMeta.md) |  | 
**access_grants** | **List[Optional[Dict[str, object]]]** |  | [optional] 

## Example

```python
from openwebui_client.models.tool_form import ToolForm

# TODO update the JSON string below
json = "{}"
# create an instance of ToolForm from a JSON string
tool_form_instance = ToolForm.from_json(json)
# print the JSON string representation of the object
print(ToolForm.to_json())

# convert the object into a dict
tool_form_dict = tool_form_instance.to_dict()
# create an instance of ToolForm from a dict
tool_form_from_dict = ToolForm.from_dict(tool_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


