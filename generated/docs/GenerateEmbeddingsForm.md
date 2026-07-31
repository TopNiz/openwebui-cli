# GenerateEmbeddingsForm

Payload for the legacy /api/embeddings endpoint (single-prompt).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**prompt** | **str** |  | 
**options** | **Dict[str, object]** |  | [optional] 
**keep_alive** | [**KeepAlive**](KeepAlive.md) |  | [optional] 

## Example

```python
from openwebui_client.models.generate_embeddings_form import GenerateEmbeddingsForm

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEmbeddingsForm from a JSON string
generate_embeddings_form_instance = GenerateEmbeddingsForm.from_json(json)
# print the JSON string representation of the object
print(GenerateEmbeddingsForm.to_json())

# convert the object into a dict
generate_embeddings_form_dict = generate_embeddings_form_instance.to_dict()
# create an instance of GenerateEmbeddingsForm from a dict
generate_embeddings_form_from_dict = GenerateEmbeddingsForm.from_dict(generate_embeddings_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


