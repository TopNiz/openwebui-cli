# UserIdNameStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**is_active** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.user_id_name_status_response import UserIdNameStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdNameStatusResponse from a JSON string
user_id_name_status_response_instance = UserIdNameStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UserIdNameStatusResponse.to_json())

# convert the object into a dict
user_id_name_status_response_dict = user_id_name_status_response_instance.to_dict()
# create an instance of UserIdNameStatusResponse from a dict
user_id_name_status_response_from_dict = UserIdNameStatusResponse.from_dict(user_id_name_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


