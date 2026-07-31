# ProcessFileForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**content** | **str** |  | [optional] 
**collection_name** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.process_file_form import ProcessFileForm

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessFileForm from a JSON string
process_file_form_instance = ProcessFileForm.from_json(json)
# print the JSON string representation of the object
print(ProcessFileForm.to_json())

# convert the object into a dict
process_file_form_dict = process_file_form_instance.to_dict()
# create an instance of ProcessFileForm from a dict
process_file_form_from_dict = ProcessFileForm.from_dict(process_file_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


