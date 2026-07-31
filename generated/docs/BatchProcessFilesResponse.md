# BatchProcessFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BatchProcessFilesResult]**](BatchProcessFilesResult.md) |  | 
**errors** | [**List[BatchProcessFilesResult]**](BatchProcessFilesResult.md) |  | 

## Example

```python
from openwebui_client.models.batch_process_files_response import BatchProcessFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchProcessFilesResponse from a JSON string
batch_process_files_response_instance = BatchProcessFilesResponse.from_json(json)
# print the JSON string representation of the object
print(BatchProcessFilesResponse.to_json())

# convert the object into a dict
batch_process_files_response_dict = batch_process_files_response_instance.to_dict()
# create an instance of BatchProcessFilesResponse from a dict
batch_process_files_response_from_dict = BatchProcessFilesResponse.from_dict(batch_process_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


