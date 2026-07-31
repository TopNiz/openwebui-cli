# SkillAccessGrantsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_grants** | **List[Dict[str, object]]** |  | 

## Example

```python
from openwebui_client.models.skill_access_grants_form import SkillAccessGrantsForm

# TODO update the JSON string below
json = "{}"
# create an instance of SkillAccessGrantsForm from a JSON string
skill_access_grants_form_instance = SkillAccessGrantsForm.from_json(json)
# print the JSON string representation of the object
print(SkillAccessGrantsForm.to_json())

# convert the object into a dict
skill_access_grants_form_dict = skill_access_grants_form_instance.to_dict()
# create an instance of SkillAccessGrantsForm from a dict
skill_access_grants_form_from_dict = SkillAccessGrantsForm.from_dict(skill_access_grants_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


