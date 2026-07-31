# DailyStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DailyStatsEntry]**](DailyStatsEntry.md) |  | 

## Example

```python
from openwebui_client.models.daily_stats_response import DailyStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DailyStatsResponse from a JSON string
daily_stats_response_instance = DailyStatsResponse.from_json(json)
# print the JSON string representation of the object
print(DailyStatsResponse.to_json())

# convert the object into a dict
daily_stats_response_dict = daily_stats_response_instance.to_dict()
# create an instance of DailyStatsResponse from a dict
daily_stats_response_from_dict = DailyStatsResponse.from_dict(daily_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


