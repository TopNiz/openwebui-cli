# BatchProcessFilesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileModel]**](FileModel.md) |  | 
**collection_name** | **str** |  | 

## Example

```python
from openwebui_client.models.batch_process_files_form import BatchProcessFilesForm

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProcessFilesForm from a JSON string
batch_process_files_form_instance = BatchProcessFilesForm.from_json(json)
# print the JSON string representation of the object
print(BatchProcessFilesForm.to_json())

# convert the object into a dict
batch_process_files_form_dict = batch_process_files_form_instance.to_dict()
# create an instance of BatchProcessFilesForm from a dict
batch_process_files_form_from_dict = BatchProcessFilesForm.from_dict(batch_process_files_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


