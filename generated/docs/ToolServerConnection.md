# ToolServerConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**path** | **str** |  | 
**type** | **str** |  | [optional] 
**auth_type** | **str** |  | 
**headers** | [**Headers**](Headers.md) |  | [optional] 
**key** | **str** |  | 
**config** | **Dict[str, object]** |  | 
**info** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.tool_server_connection import ToolServerConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ToolServerConnection from a JSON string
tool_server_connection_instance = ToolServerConnection.from_json(json)
# print the JSON string representation of the object
print(ToolServerConnection.to_json())

# convert the object into a dict
tool_server_connection_dict = tool_server_connection_instance.to_dict()
# create an instance of ToolServerConnection from a dict
tool_server_connection_from_dict = ToolServerConnection.from_dict(tool_server_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


