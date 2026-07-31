# UserUsagePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** |  | 
**end_date** | **int** |  | 
**days** | **int** |  | 

## Example

```python
from openwebui_client.models.user_usage_period import UserUsagePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsagePeriod from a JSON string
user_usage_period_instance = UserUsagePeriod.from_json(json)
# print the JSON string representation of the object
print(UserUsagePeriod.to_json())

# convert the object into a dict
user_usage_period_dict = user_usage_period_instance.to_dict()
# create an instance of UserUsagePeriod from a dict
user_usage_period_from_dict = UserUsagePeriod.from_dict(user_usage_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


