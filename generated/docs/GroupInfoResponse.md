# GroupInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**member_count** | **int** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.group_info_response import GroupInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInfoResponse from a JSON string
group_info_response_instance = GroupInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GroupInfoResponse.to_json())

# convert the object into a dict
group_info_response_dict = group_info_response_instance.to_dict()
# create an instance of GroupInfoResponse from a dict
group_info_response_from_dict = GroupInfoResponse.from_dict(group_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


