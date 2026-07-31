# SyncCleanupForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[str]** |  | 
**dir_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.sync_cleanup_form import SyncCleanupForm

# TODO update the JSON string below
json = "{}"
# create an instance of SyncCleanupForm from a JSON string
sync_cleanup_form_instance = SyncCleanupForm.from_json(json)
# print the JSON string representation of the object
print(SyncCleanupForm.to_json())

# convert the object into a dict
sync_cleanup_form_dict = sync_cleanup_form_instance.to_dict()
# create an instance of SyncCleanupForm from a dict
sync_cleanup_form_from_dict = SyncCleanupForm.from_dict(sync_cleanup_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


