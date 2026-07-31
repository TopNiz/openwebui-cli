# SearchMemoriesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'all']
**path** | **str** |  | [optional] 
**memory_id** | **str** |  | [optional] 
**limit** | **int** |  | [optional] [default to 20]

## Example

```python
from openwebui_client.models.search_memories_form import SearchMemoriesForm

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMemoriesForm from a JSON string
search_memories_form_instance = SearchMemoriesForm.from_json(json)
# print the JSON string representation of the object
print(SearchMemoriesForm.to_json())

# convert the object into a dict
search_memories_form_dict = search_memories_form_instance.to_dict()
# create an instance of SearchMemoriesForm from a dict
search_memories_form_from_dict = SearchMemoriesForm.from_dict(search_memories_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


