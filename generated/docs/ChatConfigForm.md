# ChatConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_compaction_model** | **str** |  | [optional] 
**enable_context_compaction** | **bool** |  | 
**context_compaction_token_threshold** | **int** |  | 
**context_compaction_token_cap** | **int** |  | [optional] 
**context_compaction_retention_percentage** | **int** |  | [optional] [default to 40]
**context_compaction_prompt_template** | **str** |  | 

## Example

```python
from openwebui_client.models.chat_config_form import ChatConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of ChatConfigForm from a JSON string
chat_config_form_instance = ChatConfigForm.from_json(json)
# print the JSON string representation of the object
print(ChatConfigForm.to_json())

# convert the object into a dict
chat_config_form_dict = chat_config_form_instance.to_dict()
# create an instance of ChatConfigForm from a dict
chat_config_form_from_dict = ChatConfigForm.from_dict(chat_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


