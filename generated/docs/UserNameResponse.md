# UserNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from openwebui_client.models.user_name_response import UserNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameResponse from a JSON string
user_name_response_instance = UserNameResponse.from_json(json)
# print the JSON string representation of the object
print(UserNameResponse.to_json())

# convert the object into a dict
user_name_response_dict = user_name_response_instance.to_dict()
# create an instance of UserNameResponse from a dict
user_name_response_from_dict = UserNameResponse.from_dict(user_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


