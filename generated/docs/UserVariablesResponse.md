# UserVariablesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openwebui_client.models.user_variables_response import UserVariablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserVariablesResponse from a JSON string
user_variables_response_instance = UserVariablesResponse.from_json(json)
# print the JSON string representation of the object
print(UserVariablesResponse.to_json())

# convert the object into a dict
user_variables_response_dict = user_variables_response_instance.to_dict()
# create an instance of UserVariablesResponse from a dict
user_variables_response_from_dict = UserVariablesResponse.from_dict(user_variables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


