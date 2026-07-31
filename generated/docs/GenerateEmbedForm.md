# GenerateEmbedForm

Payload for the newer /api/embed endpoint (batch-capable).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**input** | [**Input**](Input.md) |  | 
**truncate** | **bool** |  | [optional] 
**options** | **Dict[str, object]** |  | [optional] 
**keep_alive** | [**KeepAlive**](KeepAlive.md) |  | [optional] 

## Example

```python
from openwebui_client.models.generate_embed_form import GenerateEmbedForm

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEmbedForm from a JSON string
generate_embed_form_instance = GenerateEmbedForm.from_json(json)
# print the JSON string representation of the object
print(GenerateEmbedForm.to_json())

# convert the object into a dict
generate_embed_form_dict = generate_embed_form_instance.to_dict()
# create an instance of GenerateEmbedForm from a dict
generate_embed_form_from_dict = GenerateEmbedForm.from_dict(generate_embed_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


