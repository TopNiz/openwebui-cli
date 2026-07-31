# TerminalServerConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**url** | **str** |  | 
**path** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 
**server_type** | **str** |  | [optional] 
**policy_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.terminal_server_connection import TerminalServerConnection

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalServerConnection from a JSON string
terminal_server_connection_instance = TerminalServerConnection.from_json(json)
# print the JSON string representation of the object
print(TerminalServerConnection.to_json())

# convert the object into a dict
terminal_server_connection_dict = terminal_server_connection_instance.to_dict()
# create an instance of TerminalServerConnection from a dict
terminal_server_connection_from_dict = TerminalServerConnection.from_dict(terminal_server_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


