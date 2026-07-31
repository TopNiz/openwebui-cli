# EditImageForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | 
**prompt** | **str** |  | 
**model** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**n** | **int** |  | [optional] 
**negative_prompt** | **str** |  | [optional] 
**background** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.edit_image_form import EditImageForm

# TODO update the JSON string below
json = "{}"
# create an instance of EditImageForm from a JSON string
edit_image_form_instance = EditImageForm.from_json(json)
# print the JSON string representation of the object
print(EditImageForm.to_json())

# convert the object into a dict
edit_image_form_dict = edit_image_form_instance.to_dict()
# create an instance of EditImageForm from a dict
edit_image_form_from_dict = EditImageForm.from_dict(edit_image_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


