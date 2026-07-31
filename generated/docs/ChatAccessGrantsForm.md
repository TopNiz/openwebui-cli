# ChatAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from openwebui_client.models.chat_access_grants_form import ChatAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatAccessGrantsForm from a JSON string
chat_access_grants_form_instance = ChatAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(ChatAccessGrantsForm.to_json())

# convert the object into a dict
chat_access_grants_form_dict = chat_access_grants_form_instance.to_dict()
# create an instance of ChatAccessGrantsForm from a dict
chat_access_grants_form_from_dict = ChatAccessGrantsForm.from_dict(chat_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


