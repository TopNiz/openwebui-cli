# SkillModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | 
**meta** | [**SkillMeta**](SkillMeta.md) |  | 
**is_active** | **bool** |  | [optional] [default to True]
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.skill_model import SkillModel

# TODO update the JSON string below
json = "{}"
# create an instance of SkillModel from a JSON string
skill_model_instance = SkillModel.from_json(json)
# print the JSON string representation of the object
print(SkillModel.to_json())

# convert the object into a dict
skill_model_dict = skill_model_instance.to_dict()
# create an instance of SkillModel from a dict
skill_model_from_dict = SkillModel.from_dict(skill_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


