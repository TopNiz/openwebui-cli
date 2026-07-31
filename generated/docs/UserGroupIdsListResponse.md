# UserGroupIdsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserGroupIdsModel]**](UserGroupIdsModel.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.user_group_ids_list_response import UserGroupIdsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupIdsListResponse from a JSON string
user_group_ids_list_response_instance = UserGroupIdsListResponse.from_json(json)
# print the JSON string representation of the object
print(UserGroupIdsListResponse.to_json())

# convert the object into a dict
user_group_ids_list_response_dict = user_group_ids_list_response_instance.to_dict()
# create an instance of UserGroupIdsListResponse from a dict
user_group_ids_list_response_from_dict = UserGroupIdsListResponse.from_dict(user_group_ids_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


