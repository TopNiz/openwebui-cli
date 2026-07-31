# OpenWebuiRoutersOpenaiOpenAIConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_openai_api** | **bool** |  | [optional] 
**openai_api_base_urls** | **List[str]** |  | 
**openai_api_keys** | **List[str]** |  | 
**openai_api_configs** | **Dict[str, object]** |  | 

## Example

```python
from openwebui_client.models.open_webui_routers_openai_open_ai_config_form import OpenWebuiRoutersOpenaiOpenAIConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiRoutersOpenaiOpenAIConfigForm from a JSON string
open_webui_routers_openai_open_ai_config_form_instance = OpenWebuiRoutersOpenaiOpenAIConfigForm.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiRoutersOpenaiOpenAIConfigForm.to_json())

# convert the object into a dict
open_webui_routers_openai_open_ai_config_form_dict = open_webui_routers_openai_open_ai_config_form_instance.to_dict()
# create an instance of OpenWebuiRoutersOpenaiOpenAIConfigForm from a dict
open_webui_routers_openai_open_ai_config_form_from_dict = OpenWebuiRoutersOpenaiOpenAIConfigForm.from_dict(open_webui_routers_openai_open_ai_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


