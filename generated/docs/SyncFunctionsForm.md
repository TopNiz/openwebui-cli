# SyncFunctionsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[FunctionWithValvesModel]**](FunctionWithValvesModel.md) |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.sync_functions_form import SyncFunctionsForm

# TODO update the JSON string below
json = "{}"
# create an instance of SyncFunctionsForm from a JSON string
sync_functions_form_instance = SyncFunctionsForm.from_json(json)
# print the JSON string representation of the object
print(SyncFunctionsForm.to_json())

# convert the object into a dict
sync_functions_form_dict = sync_functions_form_instance.to_dict()
# create an instance of SyncFunctionsForm from a dict
sync_functions_form_from_dict = SyncFunctionsForm.from_dict(sync_functions_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


