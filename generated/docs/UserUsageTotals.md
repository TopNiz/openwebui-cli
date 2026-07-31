# UserUsageTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifetime_tokens** | **int** |  | [optional] [default to 0]
**input_tokens** | **int** |  | [optional] [default to 0]
**output_tokens** | **int** |  | [optional] [default to 0]
**peak_daily_tokens** | **int** |  | [optional] [default to 0]
**longest_chat_seconds** | **int** |  | [optional] [default to 0]
**current_streak** | **int** |  | [optional] [default to 0]
**longest_streak** | **int** |  | [optional] [default to 0]
**total_chats** | **int** |  | [optional] [default to 0]
**active_days** | **int** |  | [optional] [default to 0]
**models_used** | **int** |  | [optional] [default to 0]
**messages** | **int** |  | [optional] [default to 0]
**user_messages** | **int** |  | [optional] [default to 0]
**assistant_messages** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.user_usage_totals import UserUsageTotals

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageTotals from a JSON string
user_usage_totals_instance = UserUsageTotals.from_json(json)
# print the JSON string representation of the object
print(UserUsageTotals.to_json())

# convert the object into a dict
user_usage_totals_dict = user_usage_totals_instance.to_dict()
# create an instance of UserUsageTotals from a dict
user_usage_totals_from_dict = UserUsageTotals.from_dict(user_usage_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


