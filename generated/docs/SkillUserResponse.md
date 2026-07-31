# SkillUserResponse


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

## Example

```python
from openwebui_client.models.skill_user_response import SkillUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SkillUserResponse from a JSON string
skill_user_response_instance = SkillUserResponse.from_json(json)
# print the JSON string representation of the object
print(SkillUserResponse.to_json())

# convert the object into a dict
skill_user_response_dict = skill_user_response_instance.to_dict()
# create an instance of SkillUserResponse from a dict
skill_user_response_from_dict = SkillUserResponse.from_dict(skill_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


