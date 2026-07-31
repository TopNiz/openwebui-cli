# ChatTitleMessagesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**messages** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from openwebui_client.models.chat_title_messages_form import ChatTitleMessagesForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatTitleMessagesForm from a JSON string
chat_title_messages_form_instance = ChatTitleMessagesForm.from_json(json)
# print the JSON string representation of the object
print(ChatTitleMessagesForm.to_json())

# convert the object into a dict
chat_title_messages_form_dict = chat_title_messages_form_instance.to_dict()
# create an instance of ChatTitleMessagesForm from a dict
chat_title_messages_form_from_dict = ChatTitleMessagesForm.from_dict(chat_title_messages_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


