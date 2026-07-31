# SyncDiffForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest** | [**List[FileManifestEntry]**](FileManifestEntry.md) |  | 

## Example

```python
from openwebui_client.models.sync_diff_form import SyncDiffForm

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDiffForm from a JSON string
sync_diff_form_instance = SyncDiffForm.from_json(json)
# print the JSON string representation of the object
print(SyncDiffForm.to_json())

# convert the object into a dict
sync_diff_form_dict = sync_diff_form_instance.to_dict()
# create an instance of SyncDiffForm from a dict
sync_diff_form_from_dict = SyncDiffForm.from_dict(sync_diff_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


