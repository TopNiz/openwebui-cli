# AccessGrantsPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_users** | **bool** |  | [optional] [default to True]
**allow_groups** | **bool** |  | [optional] [default to True]

## Example

```python
from openwebui_client.models.access_grants_permissions import AccessGrantsPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantsPermissions from a JSON string
access_grants_permissions_instance = AccessGrantsPermissions.from_json(json)
# print the JSON string representation of the object
print(AccessGrantsPermissions.to_json())

# convert the object into a dict
access_grants_permissions_dict = access_grants_permissions_instance.to_dict()
# create an instance of AccessGrantsPermissions from a dict
access_grants_permissions_from_dict = AccessGrantsPermissions.from_dict(access_grants_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


