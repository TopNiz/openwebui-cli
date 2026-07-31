# UserActiveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**name** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 
**groups** | **List[object]** |  | [optional] 
**is_active** | **bool** |  | 

## Example

```python
from openwebui_client.models.user_active_response import UserActiveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserActiveResponse from a JSON string
user_active_response_instance = UserActiveResponse.from_json(json)
# print the JSON string representation of the object
print(UserActiveResponse.to_json())

# convert the object into a dict
user_active_response_dict = user_active_response_instance.to_dict()
# create an instance of UserActiveResponse from a dict
user_active_response_from_dict = UserActiveResponse.from_dict(user_active_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


