# UpdateProfileForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_image_url** | **str** |  | 
**name** | **str** |  | 
**bio** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 

## Example

```python
from openwebui_client.models.update_profile_form import UpdateProfileForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileForm from a JSON string
update_profile_form_instance = UpdateProfileForm.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileForm.to_json())

# convert the object into a dict
update_profile_form_dict = update_profile_form_instance.to_dict()
# create an instance of UpdateProfileForm from a dict
update_profile_form_from_dict = UpdateProfileForm.from_dict(update_profile_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


