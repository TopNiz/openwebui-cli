# ConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rag_template** | **str** |  | [optional] 
**top_k** | **int** |  | [optional] 
**bypass_embedding_and_retrieval** | **bool** |  | [optional] 
**rag_full_context** | **bool** |  | [optional] 
**enable_rag_hybrid_search** | **bool** |  | [optional] 
**enable_rag_hybrid_search_enriched_texts** | **bool** |  | [optional] 
**top_k_reranker** | **int** |  | [optional] 
**relevance_threshold** | **float** |  | [optional] 
**hybrid_bm25_weight** | **float** |  | [optional] 
**content_extraction_engine** | **str** |  | [optional] 
**content_extraction_supported_media_mime_types** | **List[str]** |  | [optional] 
**pdf_extract_images** | **bool** |  | [optional] 
**pdf_loader_mode** | **str** |  | [optional] 
**datalab_marker_api_key** | **str** |  | [optional] 
**datalab_marker_api_base_url** | **str** |  | [optional] 
**datalab_marker_additional_config** | **str** |  | [optional] 
**datalab_marker_skip_cache** | **bool** |  | [optional] 
**datalab_marker_force_ocr** | **bool** |  | [optional] 
**datalab_marker_paginate** | **bool** |  | [optional] 
**datalab_marker_strip_existing_ocr** | **bool** |  | [optional] 
**datalab_marker_disable_image_extraction** | **bool** |  | [optional] 
**datalab_marker_format_lines** | **bool** |  | [optional] 
**datalab_marker_use_llm** | **bool** |  | [optional] 
**datalab_marker_output_format** | **str** |  | [optional] 
**external_document_loader_url** | **str** |  | [optional] 
**external_document_loader_api_key** | **str** |  | [optional] 
**external_document_loader_headers** | **Dict[str, object]** |  | [optional] 
**tika_server_url** | **str** |  | [optional] 
**docling_server_url** | **str** |  | [optional] 
**docling_api_key** | **str** |  | [optional] 
**docling_params** | **Dict[str, object]** |  | [optional] 
**document_intelligence_endpoint** | **str** |  | [optional] 
**document_intelligence_key** | **str** |  | [optional] 
**document_intelligence_model** | **str** |  | [optional] 
**mistral_ocr_api_base_url** | **str** |  | [optional] 
**mistral_ocr_api_key** | **str** |  | [optional] 
**mistral_ocr_use_base64** | **bool** |  | [optional] 
**paddleocr_vl_base_url** | **str** |  | [optional] 
**paddleocr_vl_token** | **str** |  | [optional] 
**mineru_api_mode** | **str** |  | [optional] 
**mineru_api_url** | **str** |  | [optional] 
**mineru_api_key** | **str** |  | [optional] 
**mineru_api_timeout** | **int** |  | [optional] 
**mineru_params** | **Dict[str, object]** |  | [optional] 
**mineru_file_extensions** | **List[str]** |  | [optional] 
**rag_reranking_model** | **str** |  | [optional] 
**rag_reranking_engine** | **str** |  | [optional] 
**rag_reranking_batch_size** | **int** |  | [optional] 
**rag_external_reranker_url** | **str** |  | [optional] 
**rag_external_reranker_api_key** | **str** |  | [optional] 
**rag_external_reranker_timeout** | **str** |  | [optional] 
**text_splitter** | **str** |  | [optional] 
**rag_tokenizer_model** | **str** |  | [optional] 
**enable_markdown_header_text_splitter** | **bool** |  | [optional] 
**chunk_size** | **int** |  | [optional] 
**chunk_min_size_target** | **int** |  | [optional] 
**chunk_overlap** | **int** |  | [optional] 
**file_max_size** | [**FileMaxSize**](FileMaxSize.md) |  | [optional] 
**file_max_count** | [**FileMaxCount**](FileMaxCount.md) |  | [optional] 
**file_image_compression_width** | [**FileImageCompressionWidth**](FileImageCompressionWidth.md) |  | [optional] 
**file_image_compression_height** | [**FileImageCompressionHeight**](FileImageCompressionHeight.md) |  | [optional] 
**allowed_file_extensions** | **List[Optional[str]]** |  | [optional] 
**enable_google_drive_integration** | **bool** |  | [optional] 
**enable_onedrive_integration** | **bool** |  | [optional] 
**web** | [**WebConfig**](WebConfig.md) |  | [optional] 

## Example

```python
from openwebui_client.models.config_form import ConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigForm from a JSON string
config_form_instance = ConfigForm.from_json(json)
# print the JSON string representation of the object
print(ConfigForm.to_json())

# convert the object into a dict
config_form_dict = config_form_instance.to_dict()
# create an instance of ConfigForm from a dict
config_form_from_dict = ConfigForm.from_dict(config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


