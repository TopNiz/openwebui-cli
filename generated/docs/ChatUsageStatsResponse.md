# ChatUsageStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**models** | **Dict[str, object]** |  | [optional] 
**message_count** | **int** |  | 
**history_models** | **Dict[str, object]** |  | [optional] 
**history_message_count** | **int** |  | 
**history_user_message_count** | **int** |  | 
**history_assistant_message_count** | **int** |  | 
**average_response_time** | **float** |  | 
**average_user_message_content_length** | **float** |  | 
**average_assistant_message_content_length** | **float** |  | 
**tags** | **List[str]** |  | [optional] [default to []]
**last_message_at** | **int** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.chat_usage_stats_response import ChatUsageStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUsageStatsResponse from a JSON string
chat_usage_stats_response_instance = ChatUsageStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ChatUsageStatsResponse.to_json())

# convert the object into a dict
chat_usage_stats_response_dict = chat_usage_stats_response_instance.to_dict()
# create an instance of ChatUsageStatsResponse from a dict
chat_usage_stats_response_from_dict = ChatUsageStatsResponse.from_dict(chat_usage_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


