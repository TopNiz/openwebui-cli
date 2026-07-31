# DailyStatsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**models** | **Dict[str, int]** |  | 

## Example

```python
from openwebui_client.models.daily_stats_entry import DailyStatsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DailyStatsEntry from a JSON string
daily_stats_entry_instance = DailyStatsEntry.from_json(json)
# print the JSON string representation of the object
print(DailyStatsEntry.to_json())

# convert the object into a dict
daily_stats_entry_dict = daily_stats_entry_instance.to_dict()
# create an instance of DailyStatsEntry from a dict
daily_stats_entry_from_dict = DailyStatsEntry.from_dict(daily_stats_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


