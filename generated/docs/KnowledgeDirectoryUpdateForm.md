# KnowledgeDirectoryUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_directory_update_form import KnowledgeDirectoryUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDirectoryUpdateForm from a JSON string
knowledge_directory_update_form_instance = KnowledgeDirectoryUpdateForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDirectoryUpdateForm.to_json())

# convert the object into a dict
knowledge_directory_update_form_dict = knowledge_directory_update_form_instance.to_dict()
# create an instance of KnowledgeDirectoryUpdateForm from a dict
knowledge_directory_update_form_from_dict = KnowledgeDirectoryUpdateForm.from_dict(knowledge_directory_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


