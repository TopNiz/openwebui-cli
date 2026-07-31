# ChatStatsExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**tags** | **List[str]** |  | [optional] [default to []]
**stats** | [**AggregateChatStats**](AggregateChatStats.md) |  | 
**chat** | [**ChatBody**](ChatBody.md) |  | 

## Example

```python
from openwebui_client.models.chat_stats_export import ChatStatsExport

# TODO update the JSON string below
json = "{}"
# create an instance of ChatStatsExport from a JSON string
chat_stats_export_instance = ChatStatsExport.from_json(json)
# print the JSON string representation of the object
print(ChatStatsExport.to_json())

# convert the object into a dict
chat_stats_export_dict = chat_stats_export_instance.to_dict()
# create an instance of ChatStatsExport from a dict
chat_stats_export_from_dict = ChatStatsExport.from_dict(chat_stats_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


