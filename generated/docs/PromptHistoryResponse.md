# PromptHistoryResponse

Response model with user info.

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
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 

## Example

```python
from openwebui_client.models.prompt_history_response import PromptHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptHistoryResponse from a JSON string
prompt_history_response_instance = PromptHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(PromptHistoryResponse.to_json())

# convert the object into a dict
prompt_history_response_dict = prompt_history_response_instance.to_dict()
# create an instance of PromptHistoryResponse from a dict
prompt_history_response_from_dict = PromptHistoryResponse.from_dict(prompt_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


