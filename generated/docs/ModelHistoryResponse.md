# ModelHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**history** | [**List[ModelHistoryEntry]**](ModelHistoryEntry.md) |  | 

## Example

```python
from openwebui_client.models.model_history_response import ModelHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelHistoryResponse from a JSON string
model_history_response_instance = ModelHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ModelHistoryResponse.to_json())

# convert the object into a dict
model_history_response_dict = model_history_response_instance.to_dict()
# create an instance of ModelHistoryResponse from a dict
model_history_response_from_dict = ModelHistoryResponse.from_dict(model_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


