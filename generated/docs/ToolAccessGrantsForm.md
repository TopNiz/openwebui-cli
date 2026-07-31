# ToolAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.tool_access_grants_form import ToolAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAccessGrantsForm from a JSON string
tool_access_grants_form_instance = ToolAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(ToolAccessGrantsForm.to_json())

# convert the object into a dict
tool_access_grants_form_dict = tool_access_grants_form_instance.to_dict()
# create an instance of ToolAccessGrantsForm from a dict
tool_access_grants_form_from_dict = ToolAccessGrantsForm.from_dict(tool_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


