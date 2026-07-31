# UrlForm

Form carrying a single URL string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from openwebui_client.models.url_form import UrlForm

# TODO update the JSON string below
json = "{}"
# create an instance of UrlForm from a JSON string
url_form_instance = UrlForm.from_json(json)
# print the JSON string representation of the object
print(UrlForm.to_json())

# convert the object into a dict
url_form_dict = url_form_instance.to_dict()
# create an instance of UrlForm from a dict
url_form_from_dict = UrlForm.from_dict(url_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


