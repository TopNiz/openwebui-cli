# FunctionMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**manifest** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.function_meta import FunctionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionMeta from a JSON string
function_meta_instance = FunctionMeta.from_json(json)
# print the JSON string representation of the object
print(FunctionMeta.to_json())

# convert the object into a dict
function_meta_dict = function_meta_instance.to_dict()
# create an instance of FunctionMeta from a dict
function_meta_from_dict = FunctionMeta.from_dict(function_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


