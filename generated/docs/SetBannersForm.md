# SetBannersForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banners** | [**List[BannerModel]**](BannerModel.md) |  | 

## Example

```python
from openwebui_client.models.set_banners_form import SetBannersForm

# TODO update the JSON string below
json = "{}"
# create an instance of SetBannersForm from a JSON string
set_banners_form_instance = SetBannersForm.from_json(json)
# print the JSON string representation of the object
print(SetBannersForm.to_json())

# convert the object into a dict
set_banners_form_dict = set_banners_form_instance.to_dict()
# create an instance of SetBannersForm from a dict
set_banners_form_from_dict = SetBannersForm.from_dict(set_banners_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


