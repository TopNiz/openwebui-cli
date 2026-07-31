# KnowledgeAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.knowledge_access_grants_form import KnowledgeAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeAccessGrantsForm from a JSON string
knowledge_access_grants_form_instance = KnowledgeAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeAccessGrantsForm.to_json())

# convert the object into a dict
knowledge_access_grants_form_dict = knowledge_access_grants_form_instance.to_dict()
# create an instance of KnowledgeAccessGrantsForm from a dict
knowledge_access_grants_form_from_dict = KnowledgeAccessGrantsForm.from_dict(knowledge_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


