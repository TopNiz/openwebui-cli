# ChannelMemberListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ChannelMemberResponse]**](ChannelMemberResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.channel_member_list_response import ChannelMemberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelMemberListResponse from a JSON string
channel_member_list_response_instance = ChannelMemberListResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelMemberListResponse.to_json())

# convert the object into a dict
channel_member_list_response_dict = channel_member_list_response_instance.to_dict()
# create an instance of ChannelMemberListResponse from a dict
channel_member_list_response_from_dict = ChannelMemberListResponse.from_dict(channel_member_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


