# UserUsageInsights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**most_used_model** | **str** |  | [optional] 
**average_tokens_per_chat** | **float** |  | [optional] [default to 0]
**average_messages_per_active_day** | **float** |  | [optional] [default to 0]
**user_message_share** | **float** |  | [optional] [default to 0]
**assistant_message_share** | **float** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.user_usage_insights import UserUsageInsights

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageInsights from a JSON string
user_usage_insights_instance = UserUsageInsights.from_json(json)
# print the JSON string representation of the object
print(UserUsageInsights.to_json())

# convert the object into a dict
user_usage_insights_dict = user_usage_insights_instance.to_dict()
# create an instance of UserUsageInsights from a dict
user_usage_insights_from_dict = UserUsageInsights.from_dict(user_usage_insights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


