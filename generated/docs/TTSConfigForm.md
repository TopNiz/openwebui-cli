# TTSConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai_api_base_url** | **str** |  | 
**openai_api_key** | **str** |  | 
**openai_params** | **Dict[str, object]** |  | [optional] 
**api_key** | **str** |  | 
**engine** | **str** |  | 
**model** | **str** |  | 
**voice** | **str** |  | 
**split_on** | **str** |  | 
**azure_speech_region** | **str** |  | 
**azure_speech_base_url** | **str** |  | 
**azure_speech_output_format** | **str** |  | 
**mistral_api_key** | **str** |  | 
**mistral_api_base_url** | **str** |  | 

## Example

```python
from openwebui_client.models.tts_config_form import TTSConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of TTSConfigForm from a JSON string
tts_config_form_instance = TTSConfigForm.from_json(json)
# print the JSON string representation of the object
print(TTSConfigForm.to_json())

# convert the object into a dict
tts_config_form_dict = tts_config_form_instance.to_dict()
# create an instance of TTSConfigForm from a dict
tts_config_form_from_dict = TTSConfigForm.from_dict(tts_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


