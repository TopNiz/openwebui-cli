# KnowledgeAccessResponse


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
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 
**file_count** | **int** |  | [optional] 
**write_access** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_access_response import KnowledgeAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeAccessResponse from a JSON string
knowledge_access_response_instance = KnowledgeAccessResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeAccessResponse.to_json())

# convert the object into a dict
knowledge_access_response_dict = knowledge_access_response_instance.to_dict()
# create an instance of KnowledgeAccessResponse from a dict
knowledge_access_response_from_dict = KnowledgeAccessResponse.from_dict(knowledge_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


