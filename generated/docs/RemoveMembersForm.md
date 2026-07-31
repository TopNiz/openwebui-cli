# RemoveMembersForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.remove_members_form import RemoveMembersForm

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMembersForm from a JSON string
remove_members_form_instance = RemoveMembersForm.from_json(json)
# print the JSON string representation of the object
print(RemoveMembersForm.to_json())

# convert the object into a dict
remove_members_form_dict = remove_members_form_instance.to_dict()
# create an instance of RemoveMembersForm from a dict
remove_members_form_from_dict = RemoveMembersForm.from_dict(remove_members_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


