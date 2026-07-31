# ConnectionsConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_direct_connections** | **bool** |  | 
**enable_base_models_cache** | **bool** |  | 

## Example

```python
from openwebui_client.models.connections_config_form import ConnectionsConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionsConfigForm from a JSON string
connections_config_form_instance = ConnectionsConfigForm.from_json(json)
# print the JSON string representation of the object
print(ConnectionsConfigForm.to_json())

# convert the object into a dict
connections_config_form_dict = connections_config_form_instance.to_dict()
# create an instance of ConnectionsConfigForm from a dict
connections_config_form_from_dict = ConnectionsConfigForm.from_dict(connections_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


