# ModelAnalyticsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**count** | **int** |  | 
**unique_users** | **int** |  | [optional] [default to 0]
**unique_chats** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.model_analytics_entry import ModelAnalyticsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAnalyticsEntry from a JSON string
model_analytics_entry_instance = ModelAnalyticsEntry.from_json(json)
# print the JSON string representation of the object
print(ModelAnalyticsEntry.to_json())

# convert the object into a dict
model_analytics_entry_dict = model_analytics_entry_instance.to_dict()
# create an instance of ModelAnalyticsEntry from a dict
model_analytics_entry_from_dict = ModelAnalyticsEntry.from_dict(model_analytics_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


