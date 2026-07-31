# ModelHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**won** | **int** |  | 
**lost** | **int** |  | 

## Example

```python
from openwebui_client.models.model_history_entry import ModelHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelHistoryEntry from a JSON string
model_history_entry_instance = ModelHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(ModelHistoryEntry.to_json())

# convert the object into a dict
model_history_entry_dict = model_history_entry_instance.to_dict()
# create an instance of ModelHistoryEntry from a dict
model_history_entry_from_dict = ModelHistoryEntry.from_dict(model_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


