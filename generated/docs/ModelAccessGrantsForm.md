# ModelAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.model_access_grants_form import ModelAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccessGrantsForm from a JSON string
model_access_grants_form_instance = ModelAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(ModelAccessGrantsForm.to_json())

# convert the object into a dict
model_access_grants_form_dict = model_access_grants_form_instance.to_dict()
# create an instance of ModelAccessGrantsForm from a dict
model_access_grants_form_from_dict = ModelAccessGrantsForm.from_dict(model_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


