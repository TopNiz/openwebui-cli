# LdapConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ldap** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.ldap_config_form import LdapConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfigForm from a JSON string
ldap_config_form_instance = LdapConfigForm.from_json(json)
# print the JSON string representation of the object
print(LdapConfigForm.to_json())

# convert the object into a dict
ldap_config_form_dict = ldap_config_form_instance.to_dict()
# create an instance of LdapConfigForm from a dict
ldap_config_form_from_dict = LdapConfigForm.from_dict(ldap_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


