# ModelModel


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

## Example

```python
from openwebui_client.models.model_model import ModelModel

# TODO update the JSON string below
json = "{}"
# create an instance of ModelModel from a JSON string
model_model_instance = ModelModel.from_json(json)
# print the JSON string representation of the object
print(ModelModel.to_json())

# convert the object into a dict
model_model_dict = model_model_instance.to_dict()
# create an instance of ModelModel from a dict
model_model_from_dict = ModelModel.from_dict(model_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


