# KnowledgeResponse


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
**files** | [**List[KnowledgeResponseFilesInner]**](KnowledgeResponseFilesInner.md) |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_response import KnowledgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeResponse from a JSON string
knowledge_response_instance = KnowledgeResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeResponse.to_json())

# convert the object into a dict
knowledge_response_dict = knowledge_response_instance.to_dict()
# create an instance of KnowledgeResponse from a dict
knowledge_response_from_dict = KnowledgeResponse.from_dict(knowledge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


