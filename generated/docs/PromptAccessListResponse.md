# PromptAccessListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PromptAccessResponse]**](PromptAccessResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.prompt_access_list_response import PromptAccessListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptAccessListResponse from a JSON string
prompt_access_list_response_instance = PromptAccessListResponse.from_json(json)
# print the JSON string representation of the object
print(PromptAccessListResponse.to_json())

# convert the object into a dict
prompt_access_list_response_dict = prompt_access_list_response_instance.to_dict()
# create an instance of PromptAccessListResponse from a dict
prompt_access_list_response_from_dict = PromptAccessListResponse.from_dict(prompt_access_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


