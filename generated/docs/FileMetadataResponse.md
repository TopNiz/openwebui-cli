# FileMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**hash** | **str** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.file_metadata_response import FileMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileMetadataResponse from a JSON string
file_metadata_response_instance = FileMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(FileMetadataResponse.to_json())

# convert the object into a dict
file_metadata_response_dict = file_metadata_response_instance.to_dict()
# create an instance of FileMetadataResponse from a dict
file_metadata_response_from_dict = FileMetadataResponse.from_dict(file_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


