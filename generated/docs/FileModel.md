# FileModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**hash** | **str** |  | [optional] 
**filename** | **str** |  | 
**path** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from openwebui_client.models.file_model import FileModel

# TODO update the JSON string below
json = "{}"
# create an instance of FileModel from a JSON string
file_model_instance = FileModel.from_json(json)
# print the JSON string representation of the object
print(FileModel.to_json())

# convert the object into a dict
file_model_dict = file_model_instance.to_dict()
# create an instance of FileModel from a dict
file_model_from_dict = FileModel.from_dict(file_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


