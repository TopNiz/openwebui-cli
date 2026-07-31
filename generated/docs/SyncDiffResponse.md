# SyncDiffResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **List[Optional[Dict[str, object]]]** |  | 
**modified** | **List[Optional[Dict[str, object]]]** |  | 
**deleted** | **List[Optional[Dict[str, object]]]** |  | 
**mkdir** | **List[str]** |  | 
**rmdir** | **List[str]** |  | 
**unmodified_count** | **int** |  | 
**directory_map** | **Dict[str, str]** |  | 

## Example

```python
from openwebui_client.models.sync_diff_response import SyncDiffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDiffResponse from a JSON string
sync_diff_response_instance = SyncDiffResponse.from_json(json)
# print the JSON string representation of the object
print(SyncDiffResponse.to_json())

# convert the object into a dict
sync_diff_response_dict = sync_diff_response_instance.to_dict()
# create an instance of SyncDiffResponse from a dict
sync_diff_response_from_dict = SyncDiffResponse.from_dict(sync_diff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


