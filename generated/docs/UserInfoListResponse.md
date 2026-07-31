# UserInfoListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserInfoResponse]**](UserInfoResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.user_info_list_response import UserInfoListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoListResponse from a JSON string
user_info_list_response_instance = UserInfoListResponse.from_json(json)
# print the JSON string representation of the object
print(UserInfoListResponse.to_json())

# convert the object into a dict
user_info_list_response_dict = user_info_list_response_instance.to_dict()
# create an instance of UserInfoListResponse from a dict
user_info_list_response_from_dict = UserInfoListResponse.from_dict(user_info_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


