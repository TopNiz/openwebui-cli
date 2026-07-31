# CalendarEventModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**calendar_id** | **str** |  | 
**user_id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**start_at** | **int** |  | 
**end_at** | **int** |  | [optional] 
**all_day** | **bool** |  | [optional] [default to False]
**rrule** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**is_cancelled** | **bool** |  | [optional] [default to False]
**attendees** | [**List[CalendarEventAttendeeModel]**](CalendarEventAttendeeModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.calendar_event_model import CalendarEventModel

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventModel from a JSON string
calendar_event_model_instance = CalendarEventModel.from_json(json)
# print the JSON string representation of the object
print(CalendarEventModel.to_json())

# convert the object into a dict
calendar_event_model_dict = calendar_event_model_instance.to_dict()
# create an instance of CalendarEventModel from a dict
calendar_event_model_from_dict = CalendarEventModel.from_dict(calendar_event_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


