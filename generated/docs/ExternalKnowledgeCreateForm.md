# ExternalKnowledgeCreateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**connection_id** | **str** |  | 
**source** | [**ExternalKnowledgeSourceForm**](ExternalKnowledgeSourceForm.md) |  | 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.external_knowledge_create_form import ExternalKnowledgeCreateForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeCreateForm from a JSON string
external_knowledge_create_form_instance = ExternalKnowledgeCreateForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeCreateForm.to_json())

# convert the object into a dict
external_knowledge_create_form_dict = external_knowledge_create_form_instance.to_dict()
# create an instance of ExternalKnowledgeCreateForm from a dict
external_knowledge_create_form_from_dict = ExternalKnowledgeCreateForm.from_dict(external_knowledge_create_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


