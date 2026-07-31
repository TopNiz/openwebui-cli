# SkillAccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**meta** | [**SkillMeta**](SkillMeta.md) |  | 
**is_active** | **bool** |  | [optional] [default to True]
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**user** | [**OpenWebuiModelsUsersUserResponse**](OpenWebuiModelsUsersUserResponse.md) |  | [optional] 
**write_access** | **bool** |  | [optional] 

## Example

```python
from openwebui_client.models.skill_access_response import SkillAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SkillAccessResponse from a JSON string
skill_access_response_instance = SkillAccessResponse.from_json(json)
# print the JSON string representation of the object
print(SkillAccessResponse.to_json())

# convert the object into a dict
skill_access_response_dict = skill_access_response_instance.to_dict()
# create an instance of SkillAccessResponse from a dict
skill_access_response_from_dict = SkillAccessResponse.from_dict(skill_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


