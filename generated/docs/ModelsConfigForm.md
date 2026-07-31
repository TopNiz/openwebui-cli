# ModelsConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_models** | **str** |  | 
**default_pinned_models** | **str** |  | 
**model_order_list** | **List[Optional[str]]** |  | 
**default_model_metadata** | **Dict[str, object]** |  | [optional] 
**default_model_params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.models_config_form import ModelsConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsConfigForm from a JSON string
models_config_form_instance = ModelsConfigForm.from_json(json)
# print the JSON string representation of the object
print(ModelsConfigForm.to_json())

# convert the object into a dict
models_config_form_dict = models_config_form_instance.to_dict()
# create an instance of ModelsConfigForm from a dict
models_config_form_from_dict = ModelsConfigForm.from_dict(models_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


