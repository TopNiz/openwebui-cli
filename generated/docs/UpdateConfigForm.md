# UpdateConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_evaluation_arena_models** | **bool** |  | [optional] 
**evaluation_arena_models** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from openwebui_client.models.update_config_form import UpdateConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigForm from a JSON string
update_config_form_instance = UpdateConfigForm.from_json(json)
# print the JSON string representation of the object
print(UpdateConfigForm.to_json())

# convert the object into a dict
update_config_form_dict = update_config_form_instance.to_dict()
# create an instance of UpdateConfigForm from a dict
update_config_form_from_dict = UpdateConfigForm.from_dict(update_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


