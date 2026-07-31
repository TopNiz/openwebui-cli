# TerminalServersConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_server_connections** | [**List[TerminalServerConnection]**](TerminalServerConnection.md) |  | 

## Example

```python
from openwebui_client.models.terminal_servers_config_form import TerminalServersConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalServersConfigForm from a JSON string
terminal_servers_config_form_instance = TerminalServersConfigForm.from_json(json)
# print the JSON string representation of the object
print(TerminalServersConfigForm.to_json())

# convert the object into a dict
terminal_servers_config_form_dict = terminal_servers_config_form_instance.to_dict()
# create an instance of TerminalServersConfigForm from a dict
terminal_servers_config_form_from_dict = TerminalServersConfigForm.from_dict(terminal_servers_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


