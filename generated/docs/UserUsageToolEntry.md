# UserUsageToolEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from openwebui_client.models.user_usage_tool_entry import UserUsageToolEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageToolEntry from a JSON string
user_usage_tool_entry_instance = UserUsageToolEntry.from_json(json)
# print the JSON string representation of the object
print(UserUsageToolEntry.to_json())

# convert the object into a dict
user_usage_tool_entry_dict = user_usage_tool_entry_instance.to_dict()
# create an instance of UserUsageToolEntry from a dict
user_usage_tool_entry_from_dict = UserUsageToolEntry.from_dict(user_usage_tool_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


