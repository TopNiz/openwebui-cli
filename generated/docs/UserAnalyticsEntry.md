# UserAnalyticsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**count** | **int** |  | 
**input_tokens** | **int** |  | [optional] [default to 0]
**output_tokens** | **int** |  | [optional] [default to 0]
**total_tokens** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.user_analytics_entry import UserAnalyticsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UserAnalyticsEntry from a JSON string
user_analytics_entry_instance = UserAnalyticsEntry.from_json(json)
# print the JSON string representation of the object
print(UserAnalyticsEntry.to_json())

# convert the object into a dict
user_analytics_entry_dict = user_analytics_entry_instance.to_dict()
# create an instance of UserAnalyticsEntry from a dict
user_analytics_entry_from_dict = UserAnalyticsEntry.from_dict(user_analytics_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


