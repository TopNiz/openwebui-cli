# OpenWebuiModelsFeedbacksUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | [optional] [default to 'pending']
**last_active_at** | **int** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.open_webui_models_feedbacks_user_response import OpenWebuiModelsFeedbacksUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiModelsFeedbacksUserResponse from a JSON string
open_webui_models_feedbacks_user_response_instance = OpenWebuiModelsFeedbacksUserResponse.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiModelsFeedbacksUserResponse.to_json())

# convert the object into a dict
open_webui_models_feedbacks_user_response_dict = open_webui_models_feedbacks_user_response_instance.to_dict()
# create an instance of OpenWebuiModelsFeedbacksUserResponse from a dict
open_webui_models_feedbacks_user_response_from_dict = OpenWebuiModelsFeedbacksUserResponse.from_dict(open_webui_models_feedbacks_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


