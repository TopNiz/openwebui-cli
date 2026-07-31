# PromptSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **List[str]** |  | 
**content** | **str** |  | 

## Example

```python
from openwebui_client.models.prompt_suggestion import PromptSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSuggestion from a JSON string
prompt_suggestion_instance = PromptSuggestion.from_json(json)
# print the JSON string representation of the object
print(PromptSuggestion.to_json())

# convert the object into a dict
prompt_suggestion_dict = prompt_suggestion_instance.to_dict()
# create an instance of PromptSuggestion from a dict
prompt_suggestion_from_dict = PromptSuggestion.from_dict(prompt_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


