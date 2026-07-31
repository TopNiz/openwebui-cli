# UserProfileImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 
**profile_image_url** | **str** |  | 

## Example

```python
from openwebui_client.models.user_profile_image_response import UserProfileImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileImageResponse from a JSON string
user_profile_image_response_instance = UserProfileImageResponse.from_json(json)
# print the JSON string representation of the object
print(UserProfileImageResponse.to_json())

# convert the object into a dict
user_profile_image_response_dict = user_profile_image_response_instance.to_dict()
# create an instance of UserProfileImageResponse from a dict
user_profile_image_response_from_dict = UserProfileImageResponse.from_dict(user_profile_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


