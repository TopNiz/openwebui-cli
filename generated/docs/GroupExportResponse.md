# GroupExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**permissions** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**member_count** | **int** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.group_export_response import GroupExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupExportResponse from a JSON string
group_export_response_instance = GroupExportResponse.from_json(json)
# print the JSON string representation of the object
print(GroupExportResponse.to_json())

# convert the object into a dict
group_export_response_dict = group_export_response_instance.to_dict()
# create an instance of GroupExportResponse from a dict
group_export_response_from_dict = GroupExportResponse.from_dict(group_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


