# CalendarEventAttendeeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_id** | **str** |  | 
**user_id** | **str** |  | 
**status** | **str** |  | [optional] [default to 'pending']
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.calendar_event_attendee_model import CalendarEventAttendeeModel

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventAttendeeModel from a JSON string
calendar_event_attendee_model_instance = CalendarEventAttendeeModel.from_json(json)
# print the JSON string representation of the object
print(CalendarEventAttendeeModel.to_json())

# convert the object into a dict
calendar_event_attendee_model_dict = calendar_event_attendee_model_instance.to_dict()
# create an instance of CalendarEventAttendeeModel from a dict
calendar_event_attendee_model_from_dict = CalendarEventAttendeeModel.from_dict(calendar_event_attendee_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


