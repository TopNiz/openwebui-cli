# PromptHistoryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**prompt_id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**snapshot** | **Dict[str, object]** |  | 
**user_id** | **str** |  | 
**commit_message** | **str** |  | [optional] 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.prompt_history_model import PromptHistoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of PromptHistoryModel from a JSON string
prompt_history_model_instance = PromptHistoryModel.from_json(json)
# print the JSON string representation of the object
print(PromptHistoryModel.to_json())

# convert the object into a dict
prompt_history_model_dict = prompt_history_model_instance.to_dict()
# create an instance of PromptHistoryModel from a dict
prompt_history_model_from_dict = PromptHistoryModel.from_dict(prompt_history_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


