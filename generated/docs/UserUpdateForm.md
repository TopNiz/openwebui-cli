# UserUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.user_update_form import UserUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateForm from a JSON string
user_update_form_instance = UserUpdateForm.from_json(json)
# print the JSON string representation of the object
print(UserUpdateForm.to_json())

# convert the object into a dict
user_update_form_dict = user_update_form_instance.to_dict()
# create an instance of UserUpdateForm from a dict
user_update_form_from_dict = UserUpdateForm.from_dict(user_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


