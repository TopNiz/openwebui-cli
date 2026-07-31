# ProcessUrlForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from openwebui_client.models.process_url_form import ProcessUrlForm

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessUrlForm from a JSON string
process_url_form_instance = ProcessUrlForm.from_json(json)
# print the JSON string representation of the object
print(ProcessUrlForm.to_json())

# convert the object into a dict
process_url_form_dict = process_url_form_instance.to_dict()
# create an instance of ProcessUrlForm from a dict
process_url_form_from_dict = ProcessUrlForm.from_dict(process_url_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


