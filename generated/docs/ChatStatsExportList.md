# ChatStatsExportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'chats']
**items** | [**List[ChatStatsExport]**](ChatStatsExport.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 

## Example

```python
from openwebui_client.models.chat_stats_export_list import ChatStatsExportList

# TODO update the JSON string below
json = "{}"
# create an instance of ChatStatsExportList from a JSON string
chat_stats_export_list_instance = ChatStatsExportList.from_json(json)
# print the JSON string representation of the object
print(ChatStatsExportList.to_json())

# convert the object into a dict
chat_stats_export_list_dict = chat_stats_export_list_instance.to_dict()
# create an instance of ChatStatsExportList from a dict
chat_stats_export_list_from_dict = ChatStatsExportList.from_dict(chat_stats_export_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


