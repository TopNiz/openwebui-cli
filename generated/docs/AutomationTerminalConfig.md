# AutomationTerminalConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 
**cwd** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.automation_terminal_config import AutomationTerminalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTerminalConfig from a JSON string
automation_terminal_config_instance = AutomationTerminalConfig.from_json(json)
# print the JSON string representation of the object
print(AutomationTerminalConfig.to_json())

# convert the object into a dict
automation_terminal_config_dict = automation_terminal_config_instance.to_dict()
# create an instance of AutomationTerminalConfig from a dict
automation_terminal_config_from_dict = AutomationTerminalConfig.from_dict(automation_terminal_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


