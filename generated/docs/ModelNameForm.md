# ModelNameForm

Generic form carrying an optional model identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.model_name_form import ModelNameForm

# TODO update the JSON string below
json = "{}"
# create an instance of ModelNameForm from a JSON string
model_name_form_instance = ModelNameForm.from_json(json)
# print the JSON string representation of the object
print(ModelNameForm.to_json())

# convert the object into a dict
model_name_form_dict = model_name_form_instance.to_dict()
# create an instance of ModelNameForm from a dict
model_name_form_from_dict = ModelNameForm.from_dict(model_name_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


