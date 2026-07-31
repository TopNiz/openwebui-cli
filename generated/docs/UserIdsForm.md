# UserIdsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from openwebui_client.models.user_ids_form import UserIdsForm

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdsForm from a JSON string
user_ids_form_instance = UserIdsForm.from_json(json)
# print the JSON string representation of the object
print(UserIdsForm.to_json())

# convert the object into a dict
user_ids_form_dict = user_ids_form_instance.to_dict()
# create an instance of UserIdsForm from a dict
user_ids_form_from_dict = UserIdsForm.from_dict(user_ids_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


