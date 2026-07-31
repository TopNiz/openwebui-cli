# GroupForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**permissions** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.group_form import GroupForm

# TODO update the JSON string below
json = "{}"
# create an instance of GroupForm from a JSON string
group_form_instance = GroupForm.from_json(json)
# print the JSON string representation of the object
print(GroupForm.to_json())

# convert the object into a dict
group_form_dict = group_form_instance.to_dict()
# create an instance of GroupForm from a dict
group_form_from_dict = GroupForm.from_dict(group_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


