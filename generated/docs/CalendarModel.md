# CalendarModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**color** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] [default to False]
**is_system** | **bool** |  | [optional] [default to False]
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.calendar_model import CalendarModel

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarModel from a JSON string
calendar_model_instance = CalendarModel.from_json(json)
# print the JSON string representation of the object
print(CalendarModel.to_json())

# convert the object into a dict
calendar_model_dict = calendar_model_instance.to_dict()
# create an instance of CalendarModel from a dict
calendar_model_from_dict = CalendarModel.from_dict(calendar_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


