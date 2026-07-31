# ExternalKnowledgeConnectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[Optional[Dict[str, object]]]** |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.external_knowledge_connection_list_response import ExternalKnowledgeConnectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeConnectionListResponse from a JSON string
external_knowledge_connection_list_response_instance = ExternalKnowledgeConnectionListResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeConnectionListResponse.to_json())

# convert the object into a dict
external_knowledge_connection_list_response_dict = external_knowledge_connection_list_response_instance.to_dict()
# create an instance of ExternalKnowledgeConnectionListResponse from a dict
external_knowledge_connection_list_response_from_dict = ExternalKnowledgeConnectionListResponse.from_dict(external_knowledge_connection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


