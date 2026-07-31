# GenerateCompletionForm

Payload for the Ollama /api/generate endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**prompt** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**images** | **List[Optional[str]]** |  | [optional] 
**format** | [**Format**](Format.md) |  | [optional] 
**options** | **Dict[str, object]** |  | [optional] 
**system** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**context** | **List[Optional[int]]** |  | [optional] 
**stream** | **bool** |  | [optional] 
**raw** | **bool** |  | [optional] 
**keep_alive** | [**KeepAlive**](KeepAlive.md) |  | [optional] 

## Example

```python
from openwebui_client.models.generate_completion_form import GenerateCompletionForm

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCompletionForm from a JSON string
generate_completion_form_instance = GenerateCompletionForm.from_json(json)
# print the JSON string representation of the object
print(GenerateCompletionForm.to_json())

# convert the object into a dict
generate_completion_form_dict = generate_completion_form_instance.to_dict()
# create an instance of GenerateCompletionForm from a dict
generate_completion_form_from_dict = GenerateCompletionForm.from_dict(generate_completion_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


