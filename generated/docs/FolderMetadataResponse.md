# FolderMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.folder_metadata_response import FolderMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolderMetadataResponse from a JSON string
folder_metadata_response_instance = FolderMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(FolderMetadataResponse.to_json())

# convert the object into a dict
folder_metadata_response_dict = folder_metadata_response_instance.to_dict()
# create an instance of FolderMetadataResponse from a dict
folder_metadata_response_from_dict = FolderMetadataResponse.from_dict(folder_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


