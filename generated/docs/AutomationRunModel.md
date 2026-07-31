# AutomationRunModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**automation_id** | **str** |  | 
**chat_id** | **str** |  | [optional] 
**status** | **str** |  | 
**error** | **str** |  | [optional] 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.automation_run_model import AutomationRunModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationRunModel from a JSON string
automation_run_model_instance = AutomationRunModel.from_json(json)
# print the JSON string representation of the object
print(AutomationRunModel.to_json())

# convert the object into a dict
automation_run_model_dict = automation_run_model_instance.to_dict()
# create an instance of AutomationRunModel from a dict
automation_run_model_from_dict = AutomationRunModel.from_dict(automation_run_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


