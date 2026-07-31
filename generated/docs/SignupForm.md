# SignupForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.signup_form import SignupForm

# TODO update the JSON string below
json = "{}"
# create an instance of SignupForm from a JSON string
signup_form_instance = SignupForm.from_json(json)
# print the JSON string representation of the object
print(SignupForm.to_json())

# convert the object into a dict
signup_form_dict = signup_form_instance.to_dict()
# create an instance of SignupForm from a dict
signup_form_from_dict = SignupForm.from_dict(signup_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


