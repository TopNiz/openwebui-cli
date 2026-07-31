# FileMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from openwebui_client.models.file_meta import FileMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FileMeta from a JSON string
file_meta_instance = FileMeta.from_json(json)
# print the JSON string representation of the object
print(FileMeta.to_json())

# convert the object into a dict
file_meta_dict = file_meta_instance.to_dict()
# create an instance of FileMeta from a dict
file_meta_from_dict = FileMeta.from_dict(file_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


