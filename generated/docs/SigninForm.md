# SigninForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from openwebui_client.models.signin_form import SigninForm

# TODO update the JSON string below
json = "{}"
# create an instance of SigninForm from a JSON string
signin_form_instance = SigninForm.from_json(json)
# print the JSON string representation of the object
print(SigninForm.to_json())

# convert the object into a dict
signin_form_dict = signin_form_instance.to_dict()
# create an instance of SigninForm from a dict
signin_form_from_dict = SigninForm.from_dict(signin_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


