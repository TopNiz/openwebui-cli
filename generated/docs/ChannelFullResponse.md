# ChannelFullResponse


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
**is_manager** | **bool** |  | [optional] [default to False]
**write_access** | **bool** |  | [optional] [default to False]
**user_count** | **int** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**users** | [**List[UserIdNameStatusResponse]**](UserIdNameStatusResponse.md) |  | [optional] 
**last_read_at** | **int** |  | [optional] 
**unread_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.channel_full_response import ChannelFullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelFullResponse from a JSON string
channel_full_response_instance = ChannelFullResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelFullResponse.to_json())

# convert the object into a dict
channel_full_response_dict = channel_full_response_instance.to_dict()
# create an instance of ChannelFullResponse from a dict
channel_full_response_from_dict = ChannelFullResponse.from_dict(channel_full_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


