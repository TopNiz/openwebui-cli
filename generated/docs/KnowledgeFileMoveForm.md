# KnowledgeFileMoveForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**directory_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_file_move_form import KnowledgeFileMoveForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeFileMoveForm from a JSON string
knowledge_file_move_form_instance = KnowledgeFileMoveForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeFileMoveForm.to_json())

# convert the object into a dict
knowledge_file_move_form_dict = knowledge_file_move_form_instance.to_dict()
# create an instance of KnowledgeFileMoveForm from a dict
knowledge_file_move_form_from_dict = KnowledgeFileMoveForm.from_dict(knowledge_file_move_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


