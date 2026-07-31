# SetDefaultSuggestionsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions** | [**List[PromptSuggestion]**](PromptSuggestion.md) |  | 

## Example

```python
from openwebui_client.models.set_default_suggestions_form import SetDefaultSuggestionsForm

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultSuggestionsForm from a JSON string
set_default_suggestions_form_instance = SetDefaultSuggestionsForm.from_json(json)
# print the JSON string representation of the object
print(SetDefaultSuggestionsForm.to_json())

# convert the object into a dict
set_default_suggestions_form_dict = set_default_suggestions_form_instance.to_dict()
# create an instance of SetDefaultSuggestionsForm from a dict
set_default_suggestions_form_from_dict = SetDefaultSuggestionsForm.from_dict(set_default_suggestions_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


