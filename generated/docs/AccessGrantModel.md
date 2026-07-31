# AccessGrantModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**principal_type** | **str** |  | 
**principal_id** | **str** |  | 
**permission** | **str** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.access_grant_model import AccessGrantModel

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantModel from a JSON string
access_grant_model_instance = AccessGrantModel.from_json(json)
# print the JSON string representation of the object
print(AccessGrantModel.to_json())

# convert the object into a dict
access_grant_model_dict = access_grant_model_instance.to_dict()
# create an instance of AccessGrantModel from a dict
access_grant_model_from_dict = AccessGrantModel.from_dict(access_grant_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


