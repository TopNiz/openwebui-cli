# PromptAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.prompt_access_grants_form import PromptAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of PromptAccessGrantsForm from a JSON string
prompt_access_grants_form_instance = PromptAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(PromptAccessGrantsForm.to_json())

# convert the object into a dict
prompt_access_grants_form_dict = prompt_access_grants_form_instance.to_dict()
# create an instance of PromptAccessGrantsForm from a dict
prompt_access_grants_form_from_dict = PromptAccessGrantsForm.from_dict(prompt_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


