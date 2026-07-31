# FileModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**hash** | **str** |  | [optional] 
**filename** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | [**FileMeta**](FileMeta.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | [optional] 

## Example

```python
from openwebui_client.models.file_model_response import FileModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileModelResponse from a JSON string
file_model_response_instance = FileModelResponse.from_json(json)
# print the JSON string representation of the object
print(FileModelResponse.to_json())

# convert the object into a dict
file_model_response_dict = file_model_response_instance.to_dict()
# create an instance of FileModelResponse from a dict
file_model_response_from_dict = FileModelResponse.from_dict(file_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


