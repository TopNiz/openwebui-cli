# KnowledgeFileIdForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**directory_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_file_id_form import KnowledgeFileIdForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeFileIdForm from a JSON string
knowledge_file_id_form_instance = KnowledgeFileIdForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeFileIdForm.to_json())

# convert the object into a dict
knowledge_file_id_form_dict = knowledge_file_id_form_instance.to_dict()
# create an instance of KnowledgeFileIdForm from a dict
knowledge_file_id_form_from_dict = KnowledgeFileIdForm.from_dict(knowledge_file_id_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


