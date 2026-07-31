# SummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **int** |  | 
**total_chats** | **int** |  | 
**total_models** | **int** |  | 
**total_users** | **int** |  | 

## Example

```python
from openwebui_client.models.summary_response import SummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryResponse from a JSON string
summary_response_instance = SummaryResponse.from_json(json)
# print the JSON string representation of the object
print(SummaryResponse.to_json())

# convert the object into a dict
summary_response_dict = summary_response_instance.to_dict()
# create an instance of SummaryResponse from a dict
summary_response_from_dict = SummaryResponse.from_dict(summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


