# FeedbackUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**version** | **int** |  | 
**type** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**user** | [**OpenWebuiModelsFeedbacksUserResponse**](OpenWebuiModelsFeedbacksUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.feedback_user_response import FeedbackUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackUserResponse from a JSON string
feedback_user_response_instance = FeedbackUserResponse.from_json(json)
# print the JSON string representation of the object
print(FeedbackUserResponse.to_json())

# convert the object into a dict
feedback_user_response_dict = feedback_user_response_instance.to_dict()
# create an instance of FeedbackUserResponse from a dict
feedback_user_response_from_dict = FeedbackUserResponse.from_dict(feedback_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


