# ChannelListItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**type** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**updated_by** | **str** |  | [optional] 
**archived_at** | **int** |  | [optional] 
**archived_by** | **str** |  | [optional] 
**deleted_at** | **int** |  | [optional] 
**deleted_by** | **str** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**users** | [**List[UserIdNameStatusResponse]**](UserIdNameStatusResponse.md) |  | [optional] 
**last_message_at** | **int** |  | [optional] 
**unread_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.channel_list_item_response import ChannelListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelListItemResponse from a JSON string
channel_list_item_response_instance = ChannelListItemResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelListItemResponse.to_json())

# convert the object into a dict
channel_list_item_response_dict = channel_list_item_response_instance.to_dict()
# create an instance of ChannelListItemResponse from a dict
channel_list_item_response_from_dict = ChannelListItemResponse.from_dict(channel_list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


