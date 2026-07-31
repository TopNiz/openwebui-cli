# QueryDocForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** |  | 
**query** | **str** |  | 
**k** | **int** |  | [optional] 
**k_reranker** | **int** |  | [optional] 
**r** | **float** |  | [optional] 
**hybrid** | **bool** |  | [optional] 
**hybrid_bm25_weight** | **float** |  | [optional] 

## Example

```python
from openwebui_client.models.query_doc_form import QueryDocForm

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDocForm from a JSON string
query_doc_form_instance = QueryDocForm.from_json(json)
# print the JSON string representation of the object
print(QueryDocForm.to_json())

# convert the object into a dict
query_doc_form_dict = query_doc_form_instance.to_dict()
# create an instance of QueryDocForm from a dict
query_doc_form_from_dict = QueryDocForm.from_dict(query_doc_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


