# KnowledgeFileListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FileUserResponse]**](FileUserResponse.md) |  | 
**directories** | [**List[KnowledgeDirectoryModel]**](KnowledgeDirectoryModel.md) |  | [optional] 
**breadcrumbs** | [**List[KnowledgeDirectoryModel]**](KnowledgeDirectoryModel.md) |  | [optional] 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.knowledge_file_list_response import KnowledgeFileListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeFileListResponse from a JSON string
knowledge_file_list_response_instance = KnowledgeFileListResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeFileListResponse.to_json())

# convert the object into a dict
knowledge_file_list_response_dict = knowledge_file_list_response_instance.to_dict()
# create an instance of KnowledgeFileListResponse from a dict
knowledge_file_list_response_from_dict = KnowledgeFileListResponse.from_dict(knowledge_file_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


