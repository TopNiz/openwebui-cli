# ProcessTextForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**content** | **str** |  | 
**collection_name** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.process_text_form import ProcessTextForm

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessTextForm from a JSON string
process_text_form_instance = ProcessTextForm.from_json(json)
# print the JSON string representation of the object
print(ProcessTextForm.to_json())

# convert the object into a dict
process_text_form_dict = process_text_form_instance.to_dict()
# create an instance of ProcessTextForm from a dict
process_text_form_from_dict = ProcessTextForm.from_dict(process_text_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


