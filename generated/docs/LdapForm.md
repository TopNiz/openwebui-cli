# LdapForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from openwebui_client.models.ldap_form import LdapForm

# TODO update the JSON string below
json = "{}"
# create an instance of LdapForm from a JSON string
ldap_form_instance = LdapForm.from_json(json)
# print the JSON string representation of the object
print(LdapForm.to_json())

# convert the object into a dict
ldap_form_dict = ldap_form_instance.to_dict()
# create an instance of LdapForm from a dict
ldap_form_from_dict = LdapForm.from_dict(ldap_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


