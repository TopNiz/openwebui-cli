# CalendarForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.calendar_form import CalendarForm

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarForm from a JSON string
calendar_form_instance = CalendarForm.from_json(json)
# print the JSON string representation of the object
print(CalendarForm.to_json())

# convert the object into a dict
calendar_form_dict = calendar_form_instance.to_dict()
# create an instance of CalendarForm from a dict
calendar_form_from_dict = CalendarForm.from_dict(calendar_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


