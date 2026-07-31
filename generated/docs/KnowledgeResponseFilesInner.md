# KnowledgeResponseFilesInner


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
from openwebui_client.models.knowledge_response_files_inner import KnowledgeResponseFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeResponseFilesInner from a JSON string
knowledge_response_files_inner_instance = KnowledgeResponseFilesInner.from_json(json)
# print the JSON string representation of the object
print(KnowledgeResponseFilesInner.to_json())

# convert the object into a dict
knowledge_response_files_inner_dict = knowledge_response_files_inner_instance.to_dict()
# create an instance of KnowledgeResponseFilesInner from a dict
knowledge_response_files_inner_from_dict = KnowledgeResponseFilesInner.from_dict(knowledge_response_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


