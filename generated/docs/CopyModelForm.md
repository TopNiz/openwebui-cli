# CopyModelForm

Payload for duplicating an existing model under a new name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**destination** | **str** |  | 

## Example

```python
from openwebui_client.models.copy_model_form import CopyModelForm

# TODO update the JSON string below
json = "{}"
# create an instance of CopyModelForm from a JSON string
copy_model_form_instance = CopyModelForm.from_json(json)
# print the JSON string representation of the object
print(CopyModelForm.to_json())

# convert the object into a dict
copy_model_form_dict = copy_model_form_instance.to_dict()
# create an instance of CopyModelForm from a dict
copy_model_form_from_dict = CopyModelForm.from_dict(copy_model_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


