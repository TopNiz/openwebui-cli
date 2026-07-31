# KnowledgeDirectoryCreateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.knowledge_directory_create_form import KnowledgeDirectoryCreateForm

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDirectoryCreateForm from a JSON string
knowledge_directory_create_form_instance = KnowledgeDirectoryCreateForm.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDirectoryCreateForm.to_json())

# convert the object into a dict
knowledge_directory_create_form_dict = knowledge_directory_create_form_instance.to_dict()
# create an instance of KnowledgeDirectoryCreateForm from a dict
knowledge_directory_create_form_from_dict = KnowledgeDirectoryCreateForm.from_dict(knowledge_directory_create_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


