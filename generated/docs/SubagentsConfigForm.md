# SubagentsConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_subagents** | **bool** |  | 
**subagents_background_enabled** | **bool** |  | 
**subagents_max_concurrent** | **int** |  | 
**subagents_max_async** | **int** |  | 
**subagents_max_iterations** | **int** |  | 
**subagents_max_output** | **int** |  | 
**subagents_system_prompt** | **str** |  | 

## Example

```python
from openwebui_client.models.subagents_config_form import SubagentsConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentsConfigForm from a JSON string
subagents_config_form_instance = SubagentsConfigForm.from_json(json)
# print the JSON string representation of the object
print(SubagentsConfigForm.to_json())

# convert the object into a dict
subagents_config_form_dict = subagents_config_form_instance.to_dict()
# create an instance of SubagentsConfigForm from a dict
subagents_config_form_from_dict = SubagentsConfigForm.from_dict(subagents_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


