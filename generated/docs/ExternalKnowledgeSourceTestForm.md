# ExternalKnowledgeSourceTestForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | [optional] 
**connection** | [**ExternalKnowledgeConnectionForm**](ExternalKnowledgeConnectionForm.md) |  | 
**source** | [**ExternalKnowledgeSourceForm**](ExternalKnowledgeSourceForm.md) |  | 
**query** | **str** |  | 
**count** | **int** |  | [optional] [default to 5]

## Example

```python
from openwebui_client.models.external_knowledge_source_test_form import ExternalKnowledgeSourceTestForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeSourceTestForm from a JSON string
external_knowledge_source_test_form_instance = ExternalKnowledgeSourceTestForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeSourceTestForm.to_json())

# convert the object into a dict
external_knowledge_source_test_form_dict = external_knowledge_source_test_form_instance.to_dict()
# create an instance of ExternalKnowledgeSourceTestForm from a dict
external_knowledge_source_test_form_from_dict = ExternalKnowledgeSourceTestForm.from_dict(external_knowledge_source_test_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


