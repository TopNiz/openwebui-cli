# EventWebhookUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**targets** | **List[Dict[str, str]]** |  | [optional] 

## Example

```python
from openwebui_client.models.event_webhook_update_form import EventWebhookUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of EventWebhookUpdateForm from a JSON string
event_webhook_update_form_instance = EventWebhookUpdateForm.from_json(json)
# print the JSON string representation of the object
print(EventWebhookUpdateForm.to_json())

# convert the object into a dict
event_webhook_update_form_dict = event_webhook_update_form_instance.to_dict()
# create an instance of EventWebhookUpdateForm from a dict
event_webhook_update_form_from_dict = EventWebhookUpdateForm.from_dict(event_webhook_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


