# TaskConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_model** | **str** |  | 
**task_model_external** | **str** |  | 
**enable_title_generation** | **bool** |  | 
**title_generation_prompt_template** | **str** |  | 
**image_prompt_generation_prompt_template** | **str** |  | 
**enable_autocomplete_generation** | **bool** |  | 
**autocomplete_generation_input_max_length** | **int** |  | 
**autocomplete_generation_prompt_template** | **str** |  | 
**tags_generation_prompt_template** | **str** |  | 
**follow_up_generation_prompt_template** | **str** |  | 
**enable_follow_up_generation** | **bool** |  | 
**enable_tags_generation** | **bool** |  | 
**enable_search_query_generation** | **bool** |  | 
**enable_retrieval_query_generation** | **bool** |  | 
**query_generation_prompt_template** | **str** |  | 
**tools_function_calling_prompt_template** | **str** |  | 
**enable_voice_mode_prompt** | **bool** |  | 
**voice_mode_prompt_template** | **str** |  | 

## Example

```python
from openwebui_client.models.task_config_form import TaskConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of TaskConfigForm from a JSON string
task_config_form_instance = TaskConfigForm.from_json(json)
# print the JSON string representation of the object
print(TaskConfigForm.to_json())

# convert the object into a dict
task_config_form_dict = task_config_form_instance.to_dict()
# create an instance of TaskConfigForm from a dict
task_config_form_from_dict = TaskConfigForm.from_dict(task_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


