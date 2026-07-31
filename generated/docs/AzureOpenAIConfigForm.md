# AzureOpenAIConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**key** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from openwebui_client.models.azure_open_ai_config_form import AzureOpenAIConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of AzureOpenAIConfigForm from a JSON string
azure_open_ai_config_form_instance = AzureOpenAIConfigForm.from_json(json)
# print the JSON string representation of the object
print(AzureOpenAIConfigForm.to_json())

# convert the object into a dict
azure_open_ai_config_form_dict = azure_open_ai_config_form_instance.to_dict()
# create an instance of AzureOpenAIConfigForm from a dict
azure_open_ai_config_form_from_dict = AzureOpenAIConfigForm.from_dict(azure_open_ai_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


