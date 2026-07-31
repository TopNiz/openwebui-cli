# AddUserForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.add_user_form import AddUserForm

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserForm from a JSON string
add_user_form_instance = AddUserForm.from_json(json)
# print the JSON string representation of the object
print(AddUserForm.to_json())

# convert the object into a dict
add_user_form_dict = add_user_form_instance.to_dict()
# create an instance of AddUserForm from a dict
add_user_form_from_dict = AddUserForm.from_dict(add_user_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


