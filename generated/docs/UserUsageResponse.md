# UserUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | [**UserUsageTotals**](UserUsageTotals.md) |  | 
**heatmap** | [**List[UserUsageHeatmapEntry]**](UserUsageHeatmapEntry.md) |  | 
**weekly_heatmap** | [**List[UserUsageHeatmapEntry]**](UserUsageHeatmapEntry.md) |  | 
**cumulative_heatmap** | [**List[UserUsageHeatmapEntry]**](UserUsageHeatmapEntry.md) |  | 
**insights** | [**UserUsageInsights**](UserUsageInsights.md) |  | 
**top_models** | [**List[UserUsageModelEntry]**](UserUsageModelEntry.md) |  | 
**top_tools** | [**List[UserUsageToolEntry]**](UserUsageToolEntry.md) |  | [optional] [default to []]
**period** | [**UserUsagePeriod**](UserUsagePeriod.md) |  | 

## Example

```python
from openwebui_client.models.user_usage_response import UserUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageResponse from a JSON string
user_usage_response_instance = UserUsageResponse.from_json(json)
# print the JSON string representation of the object
print(UserUsageResponse.to_json())

# convert the object into a dict
user_usage_response_dict = user_usage_response_instance.to_dict()
# create an instance of UserUsageResponse from a dict
user_usage_response_from_dict = UserUsageResponse.from_dict(user_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


