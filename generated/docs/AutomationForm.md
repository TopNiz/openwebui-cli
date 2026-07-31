# AutomationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**folder_id** | **str** |  | [optional] 
**data** | [**AutomationData**](AutomationData.md) |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.automation_form import AutomationForm

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationForm from a JSON string
automation_form_instance = AutomationForm.from_json(json)
# print the JSON string representation of the object
print(AutomationForm.to_json())

# convert the object into a dict
automation_form_dict = automation_form_instance.to_dict()
# create an instance of AutomationForm from a dict
automation_form_from_dict = AutomationForm.from_dict(automation_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


