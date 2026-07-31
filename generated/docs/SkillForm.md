# SkillForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | 
**meta** | [**SkillMeta**](SkillMeta.md) |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**access_grants** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.skill_form import SkillForm

# TODO update the JSON string below
json = "{}"
# create an instance of SkillForm from a JSON string
skill_form_instance = SkillForm.from_json(json)
# print the JSON string representation of the object
print(SkillForm.to_json())

# convert the object into a dict
skill_form_dict = skill_form_instance.to_dict()
# create an instance of SkillForm from a dict
skill_form_from_dict = SkillForm.from_dict(skill_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


