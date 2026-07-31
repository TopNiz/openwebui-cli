# OpenWebuiRoutersOpenaiResponsesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**input** | [**Input1**](Input1.md) |  | [optional] 
**instructions** | **str** |  | [optional] 
**stream** | **bool** |  | [optional] 
**temperature** | **float** |  | [optional] 
**max_output_tokens** | **int** |  | [optional] 
**top_p** | **float** |  | [optional] 
**tools** | **List[object]** |  | [optional] 
**tool_choice** | [**ToolChoice**](ToolChoice.md) |  | [optional] 
**text** | **Dict[str, object]** |  | [optional] 
**truncation** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**store** | **bool** |  | [optional] 
**reasoning** | **Dict[str, object]** |  | [optional] 
**previous_response_id** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.open_webui_routers_openai_responses_form import OpenWebuiRoutersOpenaiResponsesForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWebuiRoutersOpenaiResponsesForm from a JSON string
open_webui_routers_openai_responses_form_instance = OpenWebuiRoutersOpenaiResponsesForm.from_json(json)
# print the JSON string representation of the object
print(OpenWebuiRoutersOpenaiResponsesForm.to_json())

# convert the object into a dict
open_webui_routers_openai_responses_form_dict = open_webui_routers_openai_responses_form_instance.to_dict()
# create an instance of OpenWebuiRoutersOpenaiResponsesForm from a dict
open_webui_routers_openai_responses_form_from_dict = OpenWebuiRoutersOpenaiResponsesForm.from_dict(open_webui_routers_openai_responses_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


