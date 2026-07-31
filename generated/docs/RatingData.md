# RatingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | [**Rating**](Rating.md) |  | [optional] 
**model_id** | **str** |  | [optional] 
**sibling_model_ids** | **List[str]** |  | [optional] 
**reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.rating_data import RatingData

# TODO update the JSON string below
json = "{}"
# create an instance of RatingData from a JSON string
rating_data_instance = RatingData.from_json(json)
# print the JSON string representation of the object
print(RatingData.to_json())

# convert the object into a dict
rating_data_dict = rating_data_instance.to_dict()
# create an instance of RatingData from a dict
rating_data_from_dict = RatingData.from_dict(rating_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


