# CalendarEventListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CalendarEventUserResponse]**](CalendarEventUserResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.calendar_event_list_response import CalendarEventListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventListResponse from a JSON string
calendar_event_list_response_instance = CalendarEventListResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarEventListResponse.to_json())

# convert the object into a dict
calendar_event_list_response_dict = calendar_event_list_response_instance.to_dict()
# create an instance of CalendarEventListResponse from a dict
calendar_event_list_response_from_dict = CalendarEventListResponse.from_dict(calendar_event_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


