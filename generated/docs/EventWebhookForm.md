# EventWebhookForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**events** | **List[str]** |  | [optional] 
**targets** | **List[Dict[str, str]]** |  | [optional] 

## Example

```python
from openwebui_client.models.event_webhook_form import EventWebhookForm

# TODO update the JSON string below
json = "{}"
# create an instance of EventWebhookForm from a JSON string
event_webhook_form_instance = EventWebhookForm.from_json(json)
# print the JSON string representation of the object
print(EventWebhookForm.to_json())

# convert the object into a dict
event_webhook_form_dict = event_webhook_form_instance.to_dict()
# create an instance of EventWebhookForm from a dict
event_webhook_form_from_dict = EventWebhookForm.from_dict(event_webhook_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


