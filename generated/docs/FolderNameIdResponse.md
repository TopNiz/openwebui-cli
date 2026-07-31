# FolderNameIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**meta** | [**FolderMetadataResponse**](FolderMetadataResponse.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_expanded** | **bool** |  | [optional] [default to False]
**unread_count** | **int** |  | [optional] [default to 0]
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.folder_name_id_response import FolderNameIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolderNameIdResponse from a JSON string
folder_name_id_response_instance = FolderNameIdResponse.from_json(json)
# print the JSON string representation of the object
print(FolderNameIdResponse.to_json())

# convert the object into a dict
folder_name_id_response_dict = folder_name_id_response_instance.to_dict()
# create an instance of FolderNameIdResponse from a dict
folder_name_id_response_from_dict = FolderNameIdResponse.from_dict(folder_name_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


