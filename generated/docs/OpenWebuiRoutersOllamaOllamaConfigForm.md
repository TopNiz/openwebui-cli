# OpenWebuiRoutersOllamaOllamaConfigForm

Payload for updating the Ollama connection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ollama_api** | **bool** |  | [optional] 
**ollama_base_urls** | **List[str]** |  | 
**ollama_api_configs** | **Dict[str, object]** |  | 

## Example

```python
from openwebui_client.models.open_webui_routers_ollama_ollama_config_form import OpenWebuiRoutersOllamaOllamaConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiRoutersOllamaOllamaConfigForm from a JSON string
open_webui_routers_ollama_ollama_config_form_instance = OpenWebuiRoutersOllamaOllamaConfigForm.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiRoutersOllamaOllamaConfigForm.to_json())

# convert the object into a dict
open_webui_routers_ollama_ollama_config_form_dict = open_webui_routers_ollama_ollama_config_form_instance.to_dict()
# create an instance of OpenWebuiRoutersOllamaOllamaConfigForm from a dict
open_webui_routers_ollama_ollama_config_form_from_dict = OpenWebuiRoutersOllamaOllamaConfigForm.from_dict(open_webui_routers_ollama_ollama_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


