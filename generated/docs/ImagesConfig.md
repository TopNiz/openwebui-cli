# ImagesConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_image_generation** | **bool** |  | 
**enable_image_prompt_generation** | **bool** |  | 
**image_generation_engine** | **str** |  | 
**image_generation_model** | **str** |  | 
**image_size** | **str** |  | 
**image_steps** | **int** |  | 
**images_openai_api_base_url** | **str** |  | 
**images_openai_api_key** | **str** |  | 
**images_openai_api_version** | **str** |  | 
**images_openai_api_params** | [**ImagesOpenaiApiParams**](ImagesOpenaiApiParams.md) |  | 
**automatic1111_base_url** | **str** |  | 
**automatic1111_api_auth** | [**Automatic1111ApiAuth**](Automatic1111ApiAuth.md) |  | 
**automatic1111_params** | [**Automatic1111Params**](Automatic1111Params.md) |  | 
**comfyui_base_url** | **str** |  | 
**comfyui_api_key** | **str** |  | 
**comfyui_workflow** | **str** |  | 
**comfyui_workflow_nodes** | **List[Optional[Dict[str, object]]]** |  | 
**images_gemini_api_base_url** | **str** |  | 
**images_gemini_api_key** | **str** |  | 
**images_gemini_endpoint_method** | **str** |  | 
**enable_image_edit** | **bool** |  | 
**image_edit_engine** | **str** |  | 
**image_edit_model** | **str** |  | 
**image_edit_size** | **str** |  | 
**images_edit_openai_api_base_url** | **str** |  | 
**images_edit_openai_api_key** | **str** |  | 
**images_edit_openai_api_version** | **str** |  | 
**images_edit_gemini_api_base_url** | **str** |  | 
**images_edit_gemini_api_key** | **str** |  | 
**images_edit_comfyui_base_url** | **str** |  | 
**images_edit_comfyui_api_key** | **str** |  | 
**images_edit_comfyui_workflow** | **str** |  | 
**images_edit_comfyui_workflow_nodes** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from openwebui_client.models.images_config import ImagesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesConfig from a JSON string
images_config_instance = ImagesConfig.from_json(json)
# print the JSON string representation of the object
print(ImagesConfig.to_json())

# convert the object into a dict
images_config_dict = images_config_instance.to_dict()
# create an instance of ImagesConfig from a dict
images_config_from_dict = ImagesConfig.from_dict(images_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


