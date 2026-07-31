# ChannelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [default to '']
**description** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from openwebui_client.models.channel_form import ChannelForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelForm from a JSON string
channel_form_instance = ChannelForm.from_json(json)
# print the JSON string representation of the object
print(ChannelForm.to_json())

# convert the object into a dict
channel_form_dict = channel_form_instance.to_dict()
# create an instance of ChannelForm from a dict
channel_form_from_dict = ChannelForm.from_dict(channel_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


