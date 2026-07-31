# KnowledgeDirectoryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**knowledge_id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**name** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.knowledge_directory_model import KnowledgeDirectoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDirectoryModel from a JSON string
knowledge_directory_model_instance = KnowledgeDirectoryModel.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDirectoryModel.to_json())

# convert the object into a dict
knowledge_directory_model_dict = knowledge_directory_model_instance.to_dict()
# create an instance of KnowledgeDirectoryModel from a dict
knowledge_directory_model_from_dict = KnowledgeDirectoryModel.from_dict(knowledge_directory_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


