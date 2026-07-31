# DeletePipelineForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url_idx** | **int** |  | 

## Example

```python
from openwebui_client.models.delete_pipeline_form import DeletePipelineForm

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePipelineForm from a JSON string
delete_pipeline_form_instance = DeletePipelineForm.from_json(json)
# print the JSON string representation of the object
print(DeletePipelineForm.to_json())

# convert the object into a dict
delete_pipeline_form_dict = delete_pipeline_form_instance.to_dict()
# create an instance of DeletePipelineForm from a dict
delete_pipeline_form_from_dict = DeletePipelineForm.from_dict(delete_pipeline_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


