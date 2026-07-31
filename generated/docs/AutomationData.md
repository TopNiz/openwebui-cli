# AutomationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**model_id** | **str** |  | 
**rrule** | **str** |  | 
**terminal** | [**AutomationTerminalConfig**](AutomationTerminalConfig.md) |  | [optional] 

## Example

```python
from openwebui_client.models.automation_data import AutomationData

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationData from a JSON string
automation_data_instance = AutomationData.from_json(json)
# print the JSON string representation of the object
print(AutomationData.to_json())

# convert the object into a dict
automation_data_dict = automation_data_instance.to_dict()
# create an instance of AutomationData from a dict
automation_data_from_dict = AutomationData.from_dict(automation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


