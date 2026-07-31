# AggregateChatStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_response_time** | **float** |  | 
**average_user_message_content_length** | **float** |  | 
**average_assistant_message_content_length** | **float** |  | 
**models** | **Dict[str, int]** |  | 
**message_count** | **int** |  | 
**history_models** | **Dict[str, int]** |  | 
**history_message_count** | **int** |  | 
**history_user_message_count** | **int** |  | 
**history_assistant_message_count** | **int** |  | 

## Example

```python
from openwebui_client.models.aggregate_chat_stats import AggregateChatStats

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateChatStats from a JSON string
aggregate_chat_stats_instance = AggregateChatStats.from_json(json)
# print the JSON string representation of the object
print(AggregateChatStats.to_json())

# convert the object into a dict
aggregate_chat_stats_dict = aggregate_chat_stats_instance.to_dict()
# create an instance of AggregateChatStats from a dict
aggregate_chat_stats_from_dict = AggregateChatStats.from_dict(aggregate_chat_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


