# ChatsImportForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[ChatImportForm]**](ChatImportForm.md) |  | 

## Example

```python
from openwebui_client.models.chats_import_form import ChatsImportForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatsImportForm from a JSON string
chats_import_form_instance = ChatsImportForm.from_json(json)
# print the JSON string representation of the object
print(ChatsImportForm.to_json())

# convert the object into a dict
chats_import_form_dict = chats_import_form_instance.to_dict()
# create an instance of ChatsImportForm from a dict
chats_import_form_from_dict = ChatsImportForm.from_dict(chats_import_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


