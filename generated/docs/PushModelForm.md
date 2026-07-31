# PushModelForm

Payload for pushing a model to a registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**insecure** | **bool** |  | [optional] 
**stream** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.push_model_form import PushModelForm

# TODO update the JSON string below
json = "{}"
# create an instance of PushModelForm from a JSON string
push_model_form_instance = PushModelForm.from_json(json)
# print the JSON string representation of the object
print(PushModelForm.to_json())

# convert the object into a dict
push_model_form_dict = push_model_form_instance.to_dict()
# create an instance of PushModelForm from a dict
push_model_form_from_dict = PushModelForm.from_dict(push_model_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


