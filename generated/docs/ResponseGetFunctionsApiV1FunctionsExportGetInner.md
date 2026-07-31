# ResponseGetFunctionsApiV1FunctionsExportGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**content** | **str** |  | 
**meta** | [**FunctionMeta**](FunctionMeta.md) |  | 
**is_active** | **bool** |  | [optional] [default to False]
**is_global** | **bool** |  | [optional] [default to False]
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**valves** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.response_get_functions_api_v1_functions_export_get_inner import ResponseGetFunctionsApiV1FunctionsExportGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetFunctionsApiV1FunctionsExportGetInner from a JSON string
response_get_functions_api_v1_functions_export_get_inner_instance = ResponseGetFunctionsApiV1FunctionsExportGetInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetFunctionsApiV1FunctionsExportGetInner.to_json())

# convert the object into a dict
response_get_functions_api_v1_functions_export_get_inner_dict = response_get_functions_api_v1_functions_export_get_inner_instance.to_dict()
# create an instance of ResponseGetFunctionsApiV1FunctionsExportGetInner from a dict
response_get_functions_api_v1_functions_export_get_inner_from_dict = ResponseGetFunctionsApiV1FunctionsExportGetInner.from_dict(response_get_functions_api_v1_functions_export_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


