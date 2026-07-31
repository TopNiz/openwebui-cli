# STTConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai_api_base_url** | **str** |  | 
**openai_api_key** | **str** |  | 
**openai_api_request_format** | **str** |  | [optional] [default to 'multipart']
**engine** | **str** |  | 
**model** | **str** |  | 
**supported_content_types** | **List[str]** |  | [optional] [default to []]
**allowed_extensions** | **List[str]** |  | [optional] [default to []]
**whisper_model** | **str** |  | 
**deepgram_api_key** | **str** |  | 
**azure_api_key** | **str** |  | 
**azure_region** | **str** |  | 
**azure_locales** | **str** |  | 
**azure_base_url** | **str** |  | 
**azure_max_speakers** | **str** |  | 
**mistral_api_key** | **str** |  | 
**mistral_api_base_url** | **str** |  | 
**mistral_use_chat_completions** | **bool** |  | 

## Example

```python
from openwebui_client.models.stt_config_form import STTConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of STTConfigForm from a JSON string
stt_config_form_instance = STTConfigForm.from_json(json)
# print the JSON string representation of the object
print(STTConfigForm.to_json())

# convert the object into a dict
stt_config_form_dict = stt_config_form_instance.to_dict()
# create an instance of STTConfigForm from a dict
stt_config_form_from_dict = STTConfigForm.from_dict(stt_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


