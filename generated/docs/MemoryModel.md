# MemoryModel

Pydantic mirror of the Memory table row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**type** | **str** |  | [optional] [default to 'context']
**path** | **str** |  | [optional] 
**content** | **str** |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.memory_model import MemoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryModel from a JSON string
memory_model_instance = MemoryModel.from_json(json)
# print the JSON string representation of the object
print(MemoryModel.to_json())

# convert the object into a dict
memory_model_dict = memory_model_instance.to_dict()
# create an instance of MemoryModel from a dict
memory_model_from_dict = MemoryModel.from_dict(memory_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


