# ChannelMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 
**presence_state** | **str** |  | [optional] 
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.channel_member_response import ChannelMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelMemberResponse from a JSON string
channel_member_response_instance = ChannelMemberResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelMemberResponse.to_json())

# convert the object into a dict
channel_member_response_dict = channel_member_response_instance.to_dict()
# create an instance of ChannelMemberResponse from a dict
channel_member_response_from_dict = ChannelMemberResponse.from_dict(channel_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


