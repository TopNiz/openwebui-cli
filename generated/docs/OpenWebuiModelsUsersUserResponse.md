# OpenWebuiModelsUsersUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from openwebui_client.models.open_webui_models_users_user_response import OpenWebuiModelsUsersUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiModelsUsersUserResponse from a JSON string
open_webui_models_users_user_response_instance = OpenWebuiModelsUsersUserResponse.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiModelsUsersUserResponse.to_json())

# convert the object into a dict
open_webui_models_users_user_response_dict = open_webui_models_users_user_response_instance.to_dict()
# create an instance of OpenWebuiModelsUsersUserResponse from a dict
open_webui_models_users_user_response_from_dict = OpenWebuiModelsUsersUserResponse.from_dict(open_webui_models_users_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


