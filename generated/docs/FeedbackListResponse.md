# FeedbackListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FeedbackUserResponse]**](FeedbackUserResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.feedback_list_response import FeedbackListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackListResponse from a JSON string
feedback_list_response_instance = FeedbackListResponse.from_json(json)
# print the JSON string representation of the object
print(FeedbackListResponse.to_json())

# convert the object into a dict
feedback_list_response_dict = feedback_list_response_instance.to_dict()
# create an instance of FeedbackListResponse from a dict
feedback_list_response_from_dict = FeedbackListResponse.from_dict(feedback_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


