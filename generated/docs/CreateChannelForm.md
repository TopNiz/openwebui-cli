# CreateChannelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [default to '']
**description** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | **List[Dict[str, object]]** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.create_channel_form import CreateChannelForm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChannelForm from a JSON string
create_channel_form_instance = CreateChannelForm.from_json(json)
# print the JSON string representation of the object
print(CreateChannelForm.to_json())

# convert the object into a dict
create_channel_form_dict = create_channel_form_instance.to_dict()
# create an instance of CreateChannelForm from a dict
create_channel_form_from_dict = CreateChannelForm.from_dict(create_channel_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


