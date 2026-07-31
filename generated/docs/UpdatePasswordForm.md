# UpdatePasswordForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from openwebui_client.models.update_password_form import UpdatePasswordForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordForm from a JSON string
update_password_form_instance = UpdatePasswordForm.from_json(json)
# print the JSON string representation of the object
print(UpdatePasswordForm.to_json())

# convert the object into a dict
update_password_form_dict = update_password_form_instance.to_dict()
# create an instance of UpdatePasswordForm from a dict
update_password_form_from_dict = UpdatePasswordForm.from_dict(update_password_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


