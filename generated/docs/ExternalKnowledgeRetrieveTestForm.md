# ExternalKnowledgeRetrieveTestForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**source** | [**ExternalKnowledgeSourceForm**](ExternalKnowledgeSourceForm.md) |  | [optional] 
**count** | **int** |  | [optional] [default to 5]

## Example

```python
from openwebui_client.models.external_knowledge_retrieve_test_form import ExternalKnowledgeRetrieveTestForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeRetrieveTestForm from a JSON string
external_knowledge_retrieve_test_form_instance = ExternalKnowledgeRetrieveTestForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeRetrieveTestForm.to_json())

# convert the object into a dict
external_knowledge_retrieve_test_form_dict = external_knowledge_retrieve_test_form_instance.to_dict()
# create an instance of ExternalKnowledgeRetrieveTestForm from a dict
external_knowledge_retrieve_test_form_from_dict = ExternalKnowledgeRetrieveTestForm.from_dict(external_knowledge_retrieve_test_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


