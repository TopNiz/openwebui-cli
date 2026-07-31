# OAuthConfigForm

All OAuth/OIDC settings exposed to the admin panel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_oauth** | **bool** |  | [optional] 
**enable_oauth_signup** | **bool** |  | [optional] 
**oauth_merge_accounts_by_email** | **bool** |  | [optional] 
**oauth_auto_redirect** | **bool** |  | [optional] 
**oauth_allowed_domains** | **str** |  | [optional] 
**oauth_blocked_groups** | **str** |  | [optional] 
**enable_oauth_role_management** | **bool** |  | [optional] 
**oauth_roles_claim** | **str** |  | [optional] 
**oauth_admin_roles** | **str** |  | [optional] 
**oauth_allowed_roles** | **str** |  | [optional] 
**enable_oauth_group_management** | **bool** |  | [optional] 
**enable_oauth_group_creation** | **bool** |  | [optional] 
**oauth_group_claim** | **str** |  | [optional] 
**oauth_group_default_share** | [**OauthGroupDefaultShare**](OauthGroupDefaultShare.md) |  | [optional] 
**oauth_provider_name** | **str** |  | [optional] 
**openid_provider_url** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | [optional] 
**oauth_client_secret** | **str** |  | [optional] 
**openid_redirect_uri** | **str** |  | [optional] 
**oauth_scopes** | **str** |  | [optional] 
**oauth_code_challenge_method** | **str** |  | [optional] 
**oauth_token_endpoint_auth_method** | **str** |  | [optional] 
**openid_end_session_endpoint** | **str** |  | [optional] 
**oauth_timeout** | [**OauthTimeout**](OauthTimeout.md) |  | [optional] 
**oauth_client_timeout** | [**OauthClientTimeout**](OauthClientTimeout.md) |  | [optional] 
**oauth_email_claim** | **str** |  | [optional] 
**oauth_username_claim** | **str** |  | [optional] 
**oauth_picture_claim** | **str** |  | [optional] 
**oauth_sub_claim** | **str** |  | [optional] 
**oauth_audience** | **str** |  | [optional] 
**oauth_update_email_on_login** | **bool** |  | [optional] 
**oauth_update_name_on_login** | **bool** |  | [optional] 
**oauth_update_picture_on_login** | **bool** |  | [optional] 
**oauth_refresh_token_include_scope** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.o_auth_config_form import OAuthConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthConfigForm from a JSON string
o_auth_config_form_instance = OAuthConfigForm.from_json(json)
# print the JSON string representation of the object
print(OAuthConfigForm.to_json())

# convert the object into a dict
o_auth_config_form_dict = o_auth_config_form_instance.to_dict()
# create an instance of OAuthConfigForm from a dict
o_auth_config_form_from_dict = OAuthConfigForm.from_dict(o_auth_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


