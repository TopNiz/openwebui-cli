# UserAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserAnalyticsEntry]**](UserAnalyticsEntry.md) |  | 

## Example

```python
from openwebui_client.models.user_analytics_response import UserAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserAnalyticsResponse from a JSON string
user_analytics_response_instance = UserAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(UserAnalyticsResponse.to_json())

# convert the object into a dict
user_analytics_response_dict = user_analytics_response_instance.to_dict()
# create an instance of UserAnalyticsResponse from a dict
user_analytics_response_from_dict = UserAnalyticsResponse.from_dict(user_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


