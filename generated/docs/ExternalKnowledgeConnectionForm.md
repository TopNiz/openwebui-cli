# ExternalKnowledgeConnectionForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**provider** | **str** |  | 
**endpoint** | **str** |  | 
**auth_config** | **Dict[str, object]** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 
**capabilities** | **Dict[str, object]** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from openwebui_client.models.external_knowledge_connection_form import ExternalKnowledgeConnectionForm

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKnowledgeConnectionForm from a JSON string
external_knowledge_connection_form_instance = ExternalKnowledgeConnectionForm.from_json(json)
# print the JSON string representation of the object
print(ExternalKnowledgeConnectionForm.to_json())

# convert the object into a dict
external_knowledge_connection_form_dict = external_knowledge_connection_form_instance.to_dict()
# create an instance of ExternalKnowledgeConnectionForm from a dict
external_knowledge_connection_form_from_dict = ExternalKnowledgeConnectionForm.from_dict(external_knowledge_connection_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


