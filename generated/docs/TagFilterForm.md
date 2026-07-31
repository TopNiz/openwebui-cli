# TagFilterForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**skip** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from openwebui_client.models.tag_filter_form import TagFilterForm

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilterForm from a JSON string
tag_filter_form_instance = TagFilterForm.from_json(json)
# print the JSON string representation of the object
print(TagFilterForm.to_json())

# convert the object into a dict
tag_filter_form_dict = tag_filter_form_instance.to_dict()
# create an instance of TagFilterForm from a dict
tag_filter_form_from_dict = TagFilterForm.from_dict(tag_filter_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


