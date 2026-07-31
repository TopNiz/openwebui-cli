# SkillAccessListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SkillAccessResponse]**](SkillAccessResponse.md) |  | [optional] [default to []]
**total** | **int** |  | [optional] [default to 0]

## Example

```python
from openwebui_client.models.skill_access_list_response import SkillAccessListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SkillAccessListResponse from a JSON string
skill_access_list_response_instance = SkillAccessListResponse.from_json(json)
# print the JSON string representation of the object
print(SkillAccessListResponse.to_json())

# convert the object into a dict
skill_access_list_response_dict = skill_access_list_response_instance.to_dict()
# create an instance of SkillAccessListResponse from a dict
skill_access_list_response_from_dict = SkillAccessListResponse.from_dict(skill_access_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


