# FileManifestEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**path** | **str** |  | 
**checksum** | **str** |  | 
**size** | **int** |  | 

## Example

```python
from openwebui_client.models.file_manifest_entry import FileManifestEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FileManifestEntry from a JSON string
file_manifest_entry_instance = FileManifestEntry.from_json(json)
# print the JSON string representation of the object
print(FileManifestEntry.to_json())

# convert the object into a dict
file_manifest_entry_dict = file_manifest_entry_instance.to_dict()
# create an instance of FileManifestEntry from a dict
file_manifest_entry_from_dict = FileManifestEntry.from_dict(file_manifest_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


