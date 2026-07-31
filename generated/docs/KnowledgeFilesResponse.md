# KnowledgeFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**files** | [**List[Optional[FileMetadataResponse]]**](FileMetadataResponse.md) |  | [optional] 
**write_access** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeFilesResponse from a JSON string
knowledge_files_response_instance = KnowledgeFilesResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeFilesResponse.to_json())

# convert the object into a dict
knowledge_files_response_dict = knowledge_files_response_instance.to_dict()
# create an instance of KnowledgeFilesResponse from a dict
knowledge_files_response_from_dict = KnowledgeFilesResponse.from_dict(knowledge_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


