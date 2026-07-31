# OAuthClientRegistrationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**client_id** | **str** |  | 
**client_name** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**oauth_server_url** | **str** |  | [optional] 
**oauth_scope** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.o_auth_client_registration_form import OAuthClientRegistrationForm

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClientRegistrationForm from a JSON string
o_auth_client_registration_form_instance = OAuthClientRegistrationForm.from_json(json)
# print the JSON string representation of the object
print(OAuthClientRegistrationForm.to_json())

# convert the object into a dict
o_auth_client_registration_form_dict = o_auth_client_registration_form_instance.to_dict()
# create an instance of OAuthClientRegistrationForm from a dict
o_auth_client_registration_form_from_dict = OAuthClientRegistrationForm.from_dict(o_auth_client_registration_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


