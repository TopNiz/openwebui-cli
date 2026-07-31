# ChatImportForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | **Dict[str, object]** |  | 
**variables** | **Dict[str, object]** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**current_message_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from openwebui_client.models.chat_import_form import ChatImportForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatImportForm from a JSON string
chat_import_form_instance = ChatImportForm.from_json(json)
# print the JSON string representation of the object
print(ChatImportForm.to_json())

# convert the object into a dict
chat_import_form_dict = chat_import_form_instance.to_dict()
# create an instance of ChatImportForm from a dict
chat_import_form_from_dict = ChatImportForm.from_dict(chat_import_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


