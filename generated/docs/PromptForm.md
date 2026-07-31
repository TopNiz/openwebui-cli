# PromptForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**tags** | **List[Optional[str]]** |  | [optional] 
**access_grants** | **List[Optional[Dict[str, object]]]** |  | [optional] 
**version_id** | **str** |  | [optional] 
**commit_message** | **str** |  | [optional] 
**is_production** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.prompt_form import PromptForm

# TODO update the JSON string below
json = "{}"
# create an instance of PromptForm from a JSON string
prompt_form_instance = PromptForm.from_json(json)
# print the JSON string representation of the object
print(PromptForm.to_json())

# convert the object into a dict
prompt_form_dict = prompt_form_instance.to_dict()
# create an instance of PromptForm from a dict
prompt_form_from_dict = PromptForm.from_dict(prompt_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


