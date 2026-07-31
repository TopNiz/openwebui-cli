# BannerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**content** | **str** |  | 
**dismissible** | **bool** |  | 
**timestamp** | **int** |  | 

## Example

```python
from openwebui_client.models.banner_model import BannerModel

# TODO update the JSON string below
json = "{}"
# create an instance of BannerModel from a JSON string
banner_model_instance = BannerModel.from_json(json)
# print the JSON string representation of the object
print(BannerModel.to_json())

# convert the object into a dict
banner_model_dict = banner_model_instance.to_dict()
# create an instance of BannerModel from a dict
banner_model_from_dict = BannerModel.from_dict(banner_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


