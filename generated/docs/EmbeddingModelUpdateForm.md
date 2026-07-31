# EmbeddingModelUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai_config** | [**OpenWebuiRoutersRetrievalOpenAIConfigForm**](OpenWebuiRoutersRetrievalOpenAIConfigForm.md) |  | [optional] 
**ollama_config** | [**OpenWebuiRoutersRetrievalOllamaConfigForm**](OpenWebuiRoutersRetrievalOllamaConfigForm.md) |  | [optional] 
**azure_openai_config** | [**AzureOpenAIConfigForm**](AzureOpenAIConfigForm.md) |  | [optional] 
**rag_embedding_engine** | **str** |  | 
**rag_embedding_model** | **str** |  | 
**rag_embedding_batch_size** | **int** |  | [optional] 
**enable_async_embedding** | **bool** |  | [optional] 
**rag_embedding_concurrent_requests** | **int** |  | [optional] 

## Example

```python
from openwebui_client.models.embedding_model_update_form import EmbeddingModelUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingModelUpdateForm from a JSON string
embedding_model_update_form_instance = EmbeddingModelUpdateForm.from_json(json)
# print the JSON string representation of the object
print(EmbeddingModelUpdateForm.to_json())

# convert the object into a dict
embedding_model_update_form_dict = embedding_model_update_form_instance.to_dict()
# create an instance of EmbeddingModelUpdateForm from a dict
embedding_model_update_form_from_dict = EmbeddingModelUpdateForm.from_dict(embedding_model_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


