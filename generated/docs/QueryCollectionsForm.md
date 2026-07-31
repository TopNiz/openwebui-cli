# QueryCollectionsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_names** | **List[str]** |  | 
**query** | **str** |  | 
**k** | **int** |  | [optional] 
**k_reranker** | **int** |  | [optional] 
**r** | **float** |  | [optional] 
**hybrid** | **bool** |  | [optional] 
**hybrid_bm25_weight** | **float** |  | [optional] 
**enable_enriched_texts** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.query_collections_form import QueryCollectionsForm

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCollectionsForm from a JSON string
query_collections_form_instance = QueryCollectionsForm.from_json(json)
# print the JSON string representation of the object
print(QueryCollectionsForm.to_json())

# convert the object into a dict
query_collections_form_dict = query_collections_form_instance.to_dict()
# create an instance of QueryCollectionsForm from a dict
query_collections_form_from_dict = QueryCollectionsForm.from_dict(query_collections_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


