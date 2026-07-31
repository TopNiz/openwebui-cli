# UpdateMembersForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | [optional] [default to []]
**group_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.update_members_form import UpdateMembersForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembersForm from a JSON string
update_members_form_instance = UpdateMembersForm.from_json(json)
# print the JSON string representation of the object
print(UpdateMembersForm.to_json())

# convert the object into a dict
update_members_form_dict = update_members_form_instance.to_dict()
# create an instance of UpdateMembersForm from a dict
update_members_form_from_dict = UpdateMembersForm.from_dict(update_members_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


