# WorkspacePermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **bool** |  | [optional] [default to False]
**knowledge** | **bool** |  | [optional] [default to False]
**prompts** | **bool** |  | [optional] [default to False]
**tools** | **bool** |  | [optional] [default to False]
**skills** | **bool** |  | [optional] [default to False]
**models_import** | **bool** |  | [optional] [default to False]
**models_export** | **bool** |  | [optional] [default to False]
**prompts_import** | **bool** |  | [optional] [default to False]
**prompts_export** | **bool** |  | [optional] [default to False]
**tools_import** | **bool** |  | [optional] [default to False]
**tools_export** | **bool** |  | [optional] [default to False]
**skills_import** | **bool** |  | [optional] [default to False]
**skills_export** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.workspace_permissions import WorkspacePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePermissions from a JSON string
workspace_permissions_instance = WorkspacePermissions.from_json(json)
# print the JSON string representation of the object
print(WorkspacePermissions.to_json())

# convert the object into a dict
workspace_permissions_dict = workspace_permissions_instance.to_dict()
# create an instance of WorkspacePermissions from a dict
workspace_permissions_from_dict = WorkspacePermissions.from_dict(workspace_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


