# GroupUpdateForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**permissions** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.group_update_form import GroupUpdateForm

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUpdateForm from a JSON string
group_update_form_instance = GroupUpdateForm.from_json(json)
# print the JSON string representation of the object
print(GroupUpdateForm.to_json())

# convert the object into a dict
group_update_form_dict = group_update_form_instance.to_dict()
# create an instance of GroupUpdateForm from a dict
group_update_form_from_dict = GroupUpdateForm.from_dict(group_update_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


