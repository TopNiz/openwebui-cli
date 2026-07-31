# ModelOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | [**List[HistoryEntry]**](HistoryEntry.md) |  | 
**tags** | [**List[TagEntry]**](TagEntry.md) |  | 

## Example

```python
from openwebui_client.models.model_overview_response import ModelOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOverviewResponse from a JSON string
model_overview_response_instance = ModelOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(ModelOverviewResponse.to_json())

# convert the object into a dict
model_overview_response_dict = model_overview_response_instance.to_dict()
# create an instance of ModelOverviewResponse from a dict
model_overview_response_from_dict = ModelOverviewResponse.from_dict(model_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


