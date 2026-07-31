# EventForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from openwebui_client.models.event_form import EventForm

# TODO update the JSON string below
json = "{}"
# create an instance of EventForm from a JSON string
event_form_instance = EventForm.from_json(json)
# print the JSON string representation of the object
print(EventForm.to_json())

# convert the object into a dict
event_form_dict = event_form_instance.to_dict()
# create an instance of EventForm from a dict
event_form_from_dict = EventForm.from_dict(event_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


