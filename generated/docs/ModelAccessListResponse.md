# ModelAccessListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ModelAccessResponse]**](ModelAccessResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from openwebui_client.models.model_access_list_response import ModelAccessListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccessListResponse from a JSON string
model_access_list_response_instance = ModelAccessListResponse.from_json(json)
# print the JSON string representation of the object
print(ModelAccessListResponse.to_json())

# convert the object into a dict
model_access_list_response_dict = model_access_list_response_instance.to_dict()
# create an instance of ModelAccessListResponse from a dict
model_access_list_response_from_dict = ModelAccessListResponse.from_dict(model_access_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


