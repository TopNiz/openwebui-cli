# WebhookMessageForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 

## Example

```python
from openwebui_client.models.webhook_message_form import WebhookMessageForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessageForm from a JSON string
webhook_message_form_instance = WebhookMessageForm.from_json(json)
# print the JSON string representation of the object
print(WebhookMessageForm.to_json())

# convert the object into a dict
webhook_message_form_dict = webhook_message_form_instance.to_dict()
# create an instance of WebhookMessageForm from a dict
webhook_message_form_from_dict = WebhookMessageForm.from_dict(webhook_message_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


