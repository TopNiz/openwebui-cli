# BatchProcessFilesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**status** | **str** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.batch_process_files_result import BatchProcessFilesResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProcessFilesResult from a JSON string
batch_process_files_result_instance = BatchProcessFilesResult.from_json(json)
# print the JSON string representation of the object
print(BatchProcessFilesResult.to_json())

# convert the object into a dict
batch_process_files_result_dict = batch_process_files_result_instance.to_dict()
# create an instance of BatchProcessFilesResult from a dict
batch_process_files_result_from_dict = BatchProcessFilesResult.from_dict(batch_process_files_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


