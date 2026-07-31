# UserVariablesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.user_variables_form import UserVariablesForm

# TODO update the JSON string below
json = "{}"
# create an instance of UserVariablesForm from a JSON string
user_variables_form_instance = UserVariablesForm.from_json(json)
# print the JSON string representation of the object
print(UserVariablesForm.to_json())

# convert the object into a dict
user_variables_form_dict = user_variables_form_instance.to_dict()
# create an instance of UserVariablesForm from a dict
user_variables_form_from_dict = UserVariablesForm.from_dict(user_variables_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


