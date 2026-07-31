# CalendarUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.calendar_update_form import CalendarUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarUpdateForm from a JSON string
calendar_update_form_instance = CalendarUpdateForm.from_json(json)
# print the JSON string representation of the object
print(CalendarUpdateForm.to_json())

# convert the object into a dict
calendar_update_form_dict = calendar_update_form_instance.to_dict()
# create an instance of CalendarUpdateForm from a dict
calendar_update_form_from_dict = CalendarUpdateForm.from_dict(calendar_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


