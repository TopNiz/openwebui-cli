# PromptMetadataForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**command** | **str** |  | 
**tags** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from openwebui_client.models.prompt_metadata_form import PromptMetadataForm

# TODO update the JSON string below
json = "{}"
# create an instance of PromptMetadataForm from a JSON string
prompt_metadata_form_instance = PromptMetadataForm.from_json(json)
# print the JSON string representation of the object
print(PromptMetadataForm.to_json())

# convert the object into a dict
prompt_metadata_form_dict = prompt_metadata_form_instance.to_dict()
# create an instance of PromptMetadataForm from a dict
prompt_metadata_form_from_dict = PromptMetadataForm.from_dict(prompt_metadata_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


