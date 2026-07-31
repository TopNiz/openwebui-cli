# ModelMeta

Metadata for a workspace model entry (profile, description, tags, capabilities).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_image_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**capabilities** | **Dict[str, object]** |  | [optional] 
**knowledge** | **List[object]** |  | [optional] 

## Example

```python
from openwebui_client.models.model_meta import ModelMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ModelMeta from a JSON string
model_meta_instance = ModelMeta.from_json(json)
# print the JSON string representation of the object
print(ModelMeta.to_json())

# convert the object into a dict
model_meta_dict = model_meta_instance.to_dict()
# create an instance of ModelMeta from a dict
model_meta_from_dict = ModelMeta.from_dict(model_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


