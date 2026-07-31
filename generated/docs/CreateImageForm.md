# CreateImageForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**prompt** | **str** |  | 
**size** | **str** |  | [optional] 
**n** | **int** |  | [optional] [default to 1]
**steps** | **int** |  | [optional] 
**negative_prompt** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.create_image_form import CreateImageForm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImageForm from a JSON string
create_image_form_instance = CreateImageForm.from_json(json)
# print the JSON string representation of the object
print(CreateImageForm.to_json())

# convert the object into a dict
create_image_form_dict = create_image_form_instance.to_dict()
# create an instance of CreateImageForm from a dict
create_image_form_from_dict = CreateImageForm.from_dict(create_image_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


