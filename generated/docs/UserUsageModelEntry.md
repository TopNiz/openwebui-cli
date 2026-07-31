# UserUsageModelEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**messages** | **int** |  | [optional] [default to 0]
**input_tokens** | **int** |  | [optional] [default to 0]
**output_tokens** | **int** |  | [optional] [default to 0]
**total_tokens** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.user_usage_model_entry import UserUsageModelEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageModelEntry from a JSON string
user_usage_model_entry_instance = UserUsageModelEntry.from_json(json)
# print the JSON string representation of the object
print(UserUsageModelEntry.to_json())

# convert the object into a dict
user_usage_model_entry_dict = user_usage_model_entry_instance.to_dict()
# create an instance of UserUsageModelEntry from a dict
user_usage_model_entry_from_dict = UserUsageModelEntry.from_dict(user_usage_model_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


