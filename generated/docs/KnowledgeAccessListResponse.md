# KnowledgeAccessListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[KnowledgeAccessResponse]**](KnowledgeAccessResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.knowledge_access_list_response import KnowledgeAccessListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeAccessListResponse from a JSON string
knowledge_access_list_response_instance = KnowledgeAccessListResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeAccessListResponse.to_json())

# convert the object into a dict
knowledge_access_list_response_dict = knowledge_access_list_response_instance.to_dict()
# create an instance of KnowledgeAccessListResponse from a dict
knowledge_access_list_response_from_dict = KnowledgeAccessListResponse.from_dict(knowledge_access_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


