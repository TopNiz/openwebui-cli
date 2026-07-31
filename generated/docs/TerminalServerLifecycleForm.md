# TerminalServerLifecycleForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**key** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**policy_id** | **str** |  | 
**lifecycle_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.terminal_server_lifecycle_form import TerminalServerLifecycleForm

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalServerLifecycleForm from a JSON string
terminal_server_lifecycle_form_instance = TerminalServerLifecycleForm.from_json(json)
# print the JSON string representation of the object
print(TerminalServerLifecycleForm.to_json())

# convert the object into a dict
terminal_server_lifecycle_form_dict = terminal_server_lifecycle_form_instance.to_dict()
# create an instance of TerminalServerLifecycleForm from a dict
terminal_server_lifecycle_form_from_dict = TerminalServerLifecycleForm.from_dict(terminal_server_lifecycle_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


