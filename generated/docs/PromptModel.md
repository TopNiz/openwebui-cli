# PromptModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**command** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**content** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**tags** | **List[Optional[str]]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**version_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 

## Example

```python
from openwebui_client.models.prompt_model import PromptModel

# TODO update the JSON string below
json = "{}"
# create an instance of PromptModel from a JSON string
prompt_model_instance = PromptModel.from_json(json)
# print the JSON string representation of the object
print(PromptModel.to_json())

# convert the object into a dict
prompt_model_dict = prompt_model_instance.to_dict()
# create an instance of PromptModel from a dict
prompt_model_from_dict = PromptModel.from_dict(prompt_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


