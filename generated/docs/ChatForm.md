# ChatForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | **Dict[str, object]** |  | 
**variables** | **Dict[str, object]** |  | [optional] 
**folder_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.chat_form import ChatForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatForm from a JSON string
chat_form_instance = ChatForm.from_json(json)
# print the JSON string representation of the object
print(ChatForm.to_json())

# convert the object into a dict
chat_form_dict = chat_form_instance.to_dict()
# create an instance of ChatForm from a dict
chat_form_from_dict = ChatForm.from_dict(chat_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


