# ModelAccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**base_model_id** | **str** |  | [optional] 
**name** | **str** |  | 
**params** | **Dict[str, object]** | Parameters for model inference (temperature, top_p, etc.). | 
**meta** | [**ModelMeta**](ModelMeta.md) |  | 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**is_active** | **bool** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 
**write_access** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.model_access_response import ModelAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccessResponse from a JSON string
model_access_response_instance = ModelAccessResponse.from_json(json)
# print the JSON string representation of the object
print(ModelAccessResponse.to_json())

# convert the object into a dict
model_access_response_dict = model_access_response_instance.to_dict()
# create an instance of ModelAccessResponse from a dict
model_access_response_from_dict = ModelAccessResponse.from_dict(model_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


