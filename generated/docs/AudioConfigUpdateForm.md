# AudioConfigUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tts** | [**TTSConfigForm**](TTSConfigForm.md) |  | 
**stt** | [**STTConfigForm**](STTConfigForm.md) |  | 

## Example

```python
from openwebui_client.models.audio_config_update_form import AudioConfigUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of AudioConfigUpdateForm from a JSON string
audio_config_update_form_instance = AudioConfigUpdateForm.from_json(json)
# print the JSON string representation of the object
print(AudioConfigUpdateForm.to_json())

# convert the object into a dict
audio_config_update_form_dict = audio_config_update_form_instance.to_dict()
# create an instance of AudioConfigUpdateForm from a dict
audio_config_update_form_from_dict = AudioConfigUpdateForm.from_dict(audio_config_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


