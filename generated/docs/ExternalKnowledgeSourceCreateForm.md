# ExternalKnowledgeSourceCreateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**connection** | [**ExternalKnowledgeConnectionForm**](ExternalKnowledgeConnectionForm.md) |  | 
**source** | [**ExternalKnowledgeSourceForm**](ExternalKnowledgeSourceForm.md) |  | 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 
**test_query** | **str** |  | 
**test_count** | **int** |  | [optional] [default to 5]

## Example

```python
from openwebui_client.models.external_knowledge_source_create_form import ExternalKnowledgeSourceCreateForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeSourceCreateForm from a JSON string
external_knowledge_source_create_form_instance = ExternalKnowledgeSourceCreateForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeSourceCreateForm.to_json())

# convert the object into a dict
external_knowledge_source_create_form_dict = external_knowledge_source_create_form_instance.to_dict()
# create an instance of ExternalKnowledgeSourceCreateForm from a dict
external_knowledge_source_create_form_from_dict = ExternalKnowledgeSourceCreateForm.from_dict(external_knowledge_source_create_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


