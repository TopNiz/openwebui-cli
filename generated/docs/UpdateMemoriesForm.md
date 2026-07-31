# UpdateMemoriesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[MemoryOperationModel]**](MemoryOperationModel.md) |  | 
**source** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.update_memories_form import UpdateMemoriesForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMemoriesForm from a JSON string
update_memories_form_instance = UpdateMemoriesForm.from_json(json)
# print the JSON string representation of the object
print(UpdateMemoriesForm.to_json())

# convert the object into a dict
update_memories_form_dict = update_memories_form_instance.to_dict()
# create an instance of UpdateMemoriesForm from a dict
update_memories_form_from_dict = UpdateMemoriesForm.from_dict(update_memories_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


