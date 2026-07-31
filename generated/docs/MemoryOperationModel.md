# MemoryOperationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**id** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.memory_operation_model import MemoryOperationModel

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryOperationModel from a JSON string
memory_operation_model_instance = MemoryOperationModel.from_json(json)
# print the JSON string representation of the object
print(MemoryOperationModel.to_json())

# convert the object into a dict
memory_operation_model_dict = memory_operation_model_instance.to_dict()
# create an instance of MemoryOperationModel from a dict
memory_operation_model_from_dict = MemoryOperationModel.from_dict(memory_operation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


