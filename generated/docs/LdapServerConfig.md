# LdapServerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**host** | **str** |  | 
**port** | **int** |  | [optional] 
**attribute_for_mail** | **str** |  | [optional] [default to 'mail']
**attribute_for_username** | **str** |  | [optional] [default to 'uid']
**app_dn** | **str** |  | 
**app_dn_password** | **str** |  | 
**search_base** | **str** |  | 
**search_filters** | **str** |  | [optional] [default to '']
**use_tls** | **bool** |  | [optional] [default to True]
**certificate_path** | **str** |  | [optional] 
**validate_cert** | **bool** |  | [optional] [default to True]
**ciphers** | **str** |  | [optional] 
**enable_group_management** | **bool** |  | [optional] [default to False]
**enable_group_creation** | **bool** |  | [optional] [default to False]
**attribute_for_groups** | **str** |  | [optional] [default to 'memberOf']

## Example

```python
from openwebui_client.models.ldap_server_config import LdapServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LdapServerConfig from a JSON string
ldap_server_config_instance = LdapServerConfig.from_json(json)
# print the JSON string representation of the object
print(LdapServerConfig.to_json())

# convert the object into a dict
ldap_server_config_dict = ldap_server_config_instance.to_dict()
# create an instance of LdapServerConfig from a dict
ldap_server_config_from_dict = LdapServerConfig.from_dict(ldap_server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


