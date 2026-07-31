# TerminalServerRefreshForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**key** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**policy_id** | **str** |  | [optional] 
**only_idle** | **bool** |  | [optional] [default to True]
**reset** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.terminal_server_refresh_form import TerminalServerRefreshForm

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalServerRefreshForm from a JSON string
terminal_server_refresh_form_instance = TerminalServerRefreshForm.from_json(json)
# print the JSON string representation of the object
print(TerminalServerRefreshForm.to_json())

# convert the object into a dict
terminal_server_refresh_form_dict = terminal_server_refresh_form_instance.to_dict()
# create an instance of TerminalServerRefreshForm from a dict
terminal_server_refresh_form_from_dict = TerminalServerRefreshForm.from_dict(terminal_server_refresh_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


