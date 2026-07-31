# WebConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_web_search** | **bool** |  | [optional] 
**enable_web_search_confirmation** | **bool** |  | [optional] 
**web_search_confirmation_content** | **str** |  | [optional] 
**web_search_engine** | **str** |  | [optional] 
**web_search_trust_env** | **bool** |  | [optional] 
**web_search_result_count** | **int** |  | [optional] 
**web_search_concurrent_requests** | **int** |  | [optional] 
**web_search_domain_filter_list** | **List[Optional[str]]** |  | [optional] [default to []]
**web_fetch_max_content_length** | **int** |  | [optional] 
**web_loader_concurrent_requests** | **int** |  | [optional] 
**bypass_web_search_embedding_and_retrieval** | **bool** |  | [optional] 
**bypass_web_search_web_loader** | **bool** |  | [optional] 
**ollama_cloud_web_search_api_key** | **str** |  | [optional] 
**searxng_query_url** | **str** |  | [optional] 
**searxng_language** | **str** |  | [optional] 
**openserp_base_url** | **str** |  | [optional] 
**yacy_query_url** | **str** |  | [optional] 
**yacy_username** | **str** |  | [optional] 
**yacy_password** | **str** |  | [optional] 
**google_pse_api_key** | **str** |  | [optional] 
**google_pse_engine_id** | **str** |  | [optional] 
**brave_search_api_key** | **str** |  | [optional] 
**brave_search_context_tokens** | **int** |  | [optional] 
**kagi_search_api_key** | **str** |  | [optional] 
**mojeek_search_api_key** | **str** |  | [optional] 
**bocha_search_api_key** | **str** |  | [optional] 
**serpstack_api_key** | **str** |  | [optional] 
**serpstack_https** | **bool** |  | [optional] 
**serper_api_key** | **str** |  | [optional] 
**serphouse_api_key** | **str** |  | [optional] 
**serphouse_domain** | **str** |  | [optional] 
**serply_api_key** | **str** |  | [optional] 
**ddgs_backend** | **str** |  | [optional] 
**tavily_api_key** | **str** |  | [optional] 
**searchapi_api_key** | **str** |  | [optional] 
**searchapi_engine** | **str** |  | [optional] 
**serpapi_api_key** | **str** |  | [optional] 
**serpapi_engine** | **str** |  | [optional] 
**jina_api_key** | **str** |  | [optional] 
**jina_api_base_url** | **str** |  | [optional] 
**bing_search_v7_endpoint** | **str** |  | [optional] 
**bing_search_v7_subscription_key** | **str** |  | [optional] 
**exa_api_key** | **str** |  | [optional] 
**perplexity_api_key** | **str** |  | [optional] 
**perplexity_model** | **str** |  | [optional] 
**perplexity_search_context_usage** | **str** |  | [optional] 
**perplexity_search_api_url** | **str** |  | [optional] 
**microsoft_web_iq_api_base_url** | **str** |  | [optional] 
**microsoft_web_iq_api_key** | **str** |  | [optional] 
**microsoft_web_iq_language** | **str** |  | [optional] 
**sougou_api_sid** | **str** |  | [optional] 
**sougou_api_sk** | **str** |  | [optional] 
**web_loader_engine** | **str** |  | [optional] 
**web_loader_timeout** | **str** |  | [optional] 
**enable_web_loader_ssl_verification** | **bool** |  | [optional] 
**playwright_ws_url** | **str** |  | [optional] 
**playwright_timeout** | **int** |  | [optional] 
**firecrawl_api_key** | **str** |  | [optional] 
**firecrawl_api_base_url** | **str** |  | [optional] 
**firecrawl_timeout** | **str** |  | [optional] 
**tavily_extract_depth** | **str** |  | [optional] 
**external_web_search_url** | **str** |  | [optional] 
**external_web_search_api_key** | **str** |  | [optional] 
**external_web_loader_url** | **str** |  | [optional] 
**external_web_loader_api_key** | **str** |  | [optional] 
**youtube_loader_language** | **List[Optional[str]]** |  | [optional] 
**youtube_loader_proxy_url** | **str** |  | [optional] 
**youtube_loader_translation** | **str** |  | [optional] 
**yandex_web_search_url** | **str** |  | [optional] 
**yandex_web_search_api_key** | **str** |  | [optional] 
**yandex_web_search_config** | **str** |  | [optional] 
**youcom_api_key** | **str** |  | [optional] 
**linkup_api_key** | **str** |  | [optional] 
**linkup_search_params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.web_config import WebConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebConfig from a JSON string
web_config_instance = WebConfig.from_json(json)
# print the JSON string representation of the object
print(WebConfig.to_json())

# convert the object into a dict
web_config_dict = web_config_instance.to_dict()
# create an instance of WebConfig from a dict
web_config_from_dict = WebConfig.from_dict(web_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


