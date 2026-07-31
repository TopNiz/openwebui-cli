# CreateModelForm

Payload for creating a new model via Modelfile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**stream** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.create_model_form import CreateModelForm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelForm from a JSON string
create_model_form_instance = CreateModelForm.from_json(json)
# print the JSON string representation of the object
print(CreateModelForm.to_json())

# convert the object into a dict
create_model_form_dict = create_model_form_instance.to_dict()
# create an instance of CreateModelForm from a dict
create_model_form_from_dict = CreateModelForm.from_dict(create_model_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


