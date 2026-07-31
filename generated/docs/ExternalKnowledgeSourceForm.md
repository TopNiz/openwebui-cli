# ExternalKnowledgeSourceForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'collection']
**name** | **str** |  | 
**config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.external_knowledge_source_form import ExternalKnowledgeSourceForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeSourceForm from a JSON string
external_knowledge_source_form_instance = ExternalKnowledgeSourceForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeSourceForm.to_json())

# convert the object into a dict
external_knowledge_source_form_dict = external_knowledge_source_form_instance.to_dict()
# create an instance of ExternalKnowledgeSourceForm from a dict
external_knowledge_source_form_from_dict = ExternalKnowledgeSourceForm.from_dict(external_knowledge_source_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


