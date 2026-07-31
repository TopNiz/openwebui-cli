# CalendarEventForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **str** |  | 
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
**attendees** | **List[Optional[Dict[str, object]]]** |  | [optional] 

## Example

```python
from openwebui_client.models.calendar_event_form import CalendarEventForm

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventForm from a JSON string
calendar_event_form_instance = CalendarEventForm.from_json(json)
# print the JSON string representation of the object
print(CalendarEventForm.to_json())

# convert the object into a dict
calendar_event_form_dict = calendar_event_form_instance.to_dict()
# create an instance of CalendarEventForm from a dict
calendar_event_form_from_dict = CalendarEventForm.from_dict(calendar_event_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


