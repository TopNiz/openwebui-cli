# MemoryUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.memory_update_model import MemoryUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryUpdateModel from a JSON string
memory_update_model_instance = MemoryUpdateModel.from_json(json)
# print the JSON string representation of the object
print(MemoryUpdateModel.to_json())

# convert the object into a dict
memory_update_model_dict = memory_update_model_instance.to_dict()
# create an instance of MemoryUpdateModel from a dict
memory_update_model_from_dict = MemoryUpdateModel.from_dict(memory_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


