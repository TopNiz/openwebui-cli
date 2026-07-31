# ToolServersConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_server_connections** | [**List[ToolServerConnection]**](ToolServerConnection.md) |  | 

## Example

```python
from openwebui_client.models.tool_servers_config_form import ToolServersConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of ToolServersConfigForm from a JSON string
tool_servers_config_form_instance = ToolServersConfigForm.from_json(json)
# print the JSON string representation of the object
print(ToolServersConfigForm.to_json())

# convert the object into a dict
tool_servers_config_form_dict = tool_servers_config_form_instance.to_dict()
# create an instance of ToolServersConfigForm from a dict
tool_servers_config_form_from_dict = ToolServersConfigForm.from_dict(tool_servers_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


