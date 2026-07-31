# SearchForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** |  | 

## Example

```python
from openwebui_client.models.search_form import SearchForm

# TODO update the JSON string below
json = "{}"
# create an instance of SearchForm from a JSON string
search_form_instance = SearchForm.from_json(json)
# print the JSON string representation of the object
print(SearchForm.to_json())

# convert the object into a dict
search_form_dict = search_form_instance.to_dict()
# create an instance of SearchForm from a dict
search_form_from_dict = SearchForm.from_dict(search_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


