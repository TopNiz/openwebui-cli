# CalendarEventUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_at** | **int** |  | [optional] 
**end_at** | **int** |  | [optional] 
**all_day** | **bool** |  | [optional] 
**rrule** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**is_cancelled** | **bool** |  | [optional] 
**attendees** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.calendar_event_update_form import CalendarEventUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventUpdateForm from a JSON string
calendar_event_update_form_instance = CalendarEventUpdateForm.from_json(json)
# print the JSON string representation of the object
print(CalendarEventUpdateForm.to_json())

# convert the object into a dict
calendar_event_update_form_dict = calendar_event_update_form_instance.to_dict()
# create an instance of CalendarEventUpdateForm from a dict
calendar_event_update_form_from_dict = CalendarEventUpdateForm.from_dict(calendar_event_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


