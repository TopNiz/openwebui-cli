# UserInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**bio** | **str** |  | [optional] 
**groups** | **List[object]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.user_info_response import UserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoResponse from a JSON string
user_info_response_instance = UserInfoResponse.from_json(json)
# print the JSON string representation of the object
print(UserInfoResponse.to_json())

# convert the object into a dict
user_info_response_dict = user_info_response_instance.to_dict()
# create an instance of UserInfoResponse from a dict
user_info_response_from_dict = UserInfoResponse.from_dict(user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


