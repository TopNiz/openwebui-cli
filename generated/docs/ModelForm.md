# ModelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**base_model_id** | **str** |  | [optional] 
**name** | **str** |  | 
**meta** | [**ModelMeta**](ModelMeta.md) |  | 
**params** | **Dict[str, object]** | Parameters for model inference (temperature, top_p, etc.). | 
**access_grants** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from openwebui_client.models.model_form import ModelForm

# TODO update the JSON string below
json = "{}"
# create an instance of ModelForm from a JSON string
model_form_instance = ModelForm.from_json(json)
# print the JSON string representation of the object
print(ModelForm.to_json())

# convert the object into a dict
model_form_dict = model_form_instance.to_dict()
# create an instance of ModelForm from a dict
model_form_from_dict = ModelForm.from_dict(model_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


