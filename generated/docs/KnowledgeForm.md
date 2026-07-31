# KnowledgeForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_form import KnowledgeForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeForm from a JSON string
knowledge_form_instance = KnowledgeForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeForm.to_json())

# convert the object into a dict
knowledge_form_dict = knowledge_form_instance.to_dict()
# create an instance of KnowledgeForm from a dict
knowledge_form_from_dict = KnowledgeForm.from_dict(knowledge_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


