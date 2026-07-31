# ChatHistoryStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**Dict[str, MessageStats]**](MessageStats.md) |  | 
**current_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.chat_history_stats import ChatHistoryStats

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistoryStats from a JSON string
chat_history_stats_instance = ChatHistoryStats.from_json(json)
# print the JSON string representation of the object
print(ChatHistoryStats.to_json())

# convert the object into a dict
chat_history_stats_dict = chat_history_stats_instance.to_dict()
# create an instance of ChatHistoryStats from a dict
chat_history_stats_from_dict = ChatHistoryStats.from_dict(chat_history_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


