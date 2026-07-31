# NotificationTargetForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**delivery** | **str** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.notification_target_form import NotificationTargetForm

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTargetForm from a JSON string
notification_target_form_instance = NotificationTargetForm.from_json(json)
# print the JSON string representation of the object
print(NotificationTargetForm.to_json())

# convert the object into a dict
notification_target_form_dict = notification_target_form_instance.to_dict()
# create an instance of NotificationTargetForm from a dict
notification_target_form_from_dict = NotificationTargetForm.from_dict(notification_target_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


