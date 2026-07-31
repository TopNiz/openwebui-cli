# FeedbackIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.feedback_id_response import FeedbackIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackIdResponse from a JSON string
feedback_id_response_instance = FeedbackIdResponse.from_json(json)
# print the JSON string representation of the object
print(FeedbackIdResponse.to_json())

# convert the object into a dict
feedback_id_response_dict = feedback_id_response_instance.to_dict()
# create an instance of FeedbackIdResponse from a dict
feedback_id_response_from_dict = FeedbackIdResponse.from_dict(feedback_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


