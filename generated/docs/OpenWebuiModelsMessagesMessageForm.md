# OpenWebuiModelsMessagesMessageForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temp_id** | **str** |  | [optional] 
**content** | **str** |  | 
**reply_to_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.open_webui_models_messages_message_form import OpenWebuiModelsMessagesMessageForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiModelsMessagesMessageForm from a JSON string
open_webui_models_messages_message_form_instance = OpenWebuiModelsMessagesMessageForm.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiModelsMessagesMessageForm.to_json())

# convert the object into a dict
open_webui_models_messages_message_form_dict = open_webui_models_messages_message_form_instance.to_dict()
# create an instance of OpenWebuiModelsMessagesMessageForm from a dict
open_webui_models_messages_message_form_from_dict = OpenWebuiModelsMessagesMessageForm.from_dict(open_webui_models_messages_message_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


