# UserUsageHeatmapEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**messages** | **int** |  | [optional] [default to 0]
**chats** | **int** |  | [optional] [default to 0]
**tokens** | **int** |  | [optional] [default to 0]
**models** | **Dict[str, int]** |  | [optional] 

## Example

```python
from openwebui_client.models.user_usage_heatmap_entry import UserUsageHeatmapEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageHeatmapEntry from a JSON string
user_usage_heatmap_entry_instance = UserUsageHeatmapEntry.from_json(json)
# print the JSON string representation of the object
print(UserUsageHeatmapEntry.to_json())

# convert the object into a dict
user_usage_heatmap_entry_dict = user_usage_heatmap_entry_instance.to_dict()
# create an instance of UserUsageHeatmapEntry from a dict
user_usage_heatmap_entry_from_dict = UserUsageHeatmapEntry.from_dict(user_usage_heatmap_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


