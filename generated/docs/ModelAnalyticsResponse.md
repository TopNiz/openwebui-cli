# ModelAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[ModelAnalyticsEntry]**](ModelAnalyticsEntry.md) |  | 

## Example

```python
from openwebui_client.models.model_analytics_response import ModelAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAnalyticsResponse from a JSON string
model_analytics_response_instance = ModelAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(ModelAnalyticsResponse.to_json())

# convert the object into a dict
model_analytics_response_dict = model_analytics_response_instance.to_dict()
# create an instance of ModelAnalyticsResponse from a dict
model_analytics_response_from_dict = ModelAnalyticsResponse.from_dict(model_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


