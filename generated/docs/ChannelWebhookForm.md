# ChannelWebhookForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.channel_webhook_form import ChannelWebhookForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelWebhookForm from a JSON string
channel_webhook_form_instance = ChannelWebhookForm.from_json(json)
# print the JSON string representation of the object
print(ChannelWebhookForm.to_json())

# convert the object into a dict
channel_webhook_form_dict = channel_webhook_form_instance.to_dict()
# create an instance of ChannelWebhookForm from a dict
channel_webhook_form_from_dict = ChannelWebhookForm.from_dict(channel_webhook_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


