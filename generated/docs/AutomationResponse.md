# AutomationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**folder_id** | **str** |  | [optional] 
**name** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | 
**last_run_at** | **int** |  | [optional] 
**next_run_at** | **int** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**last_run** | [**AutomationRunModel**](AutomationRunModel.md) |  | [optional] 
**next_runs** | **List[int]** |  | [optional] 

## Example

```python
from openwebui_client.models.automation_response import AutomationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationResponse from a JSON string
automation_response_instance = AutomationResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationResponse.to_json())

# convert the object into a dict
automation_response_dict = automation_response_instance.to_dict()
# create an instance of AutomationResponse from a dict
automation_response_from_dict = AutomationResponse.from_dict(automation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


