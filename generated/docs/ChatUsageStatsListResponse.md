# ChatUsageStatsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChatUsageStatsResponse]**](ChatUsageStatsResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.chat_usage_stats_list_response import ChatUsageStatsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUsageStatsListResponse from a JSON string
chat_usage_stats_list_response_instance = ChatUsageStatsListResponse.from_json(json)
# print the JSON string representation of the object
print(ChatUsageStatsListResponse.to_json())

# convert the object into a dict
chat_usage_stats_list_response_dict = chat_usage_stats_list_response_instance.to_dict()
# create an instance of ChatUsageStatsListResponse from a dict
chat_usage_stats_list_response_from_dict = ChatUsageStatsListResponse.from_dict(chat_usage_stats_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


