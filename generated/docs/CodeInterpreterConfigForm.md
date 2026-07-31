# CodeInterpreterConfigForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_code_execution** | **bool** |  | 
**code_execution_engine** | **str** |  | 
**code_execution_jupyter_url** | **str** |  | 
**code_execution_jupyter_auth** | **str** |  | 
**code_execution_jupyter_auth_token** | **str** |  | 
**code_execution_jupyter_auth_password** | **str** |  | 
**code_execution_jupyter_timeout** | **int** |  | 
**enable_code_interpreter** | **bool** |  | 
**code_interpreter_engine** | **str** |  | 
**code_interpreter_prompt_template** | **str** |  | 
**code_interpreter_jupyter_url** | **str** |  | 
**code_interpreter_jupyter_auth** | **str** |  | 
**code_interpreter_jupyter_auth_token** | **str** |  | 
**code_interpreter_jupyter_auth_password** | **str** |  | 
**code_interpreter_jupyter_timeout** | **int** |  | 

## Example

```python
from openwebui_client.models.code_interpreter_config_form import CodeInterpreterConfigForm

# TODO update the JSON string below
json = "{}"
# create an instance of CodeInterpreterConfigForm from a JSON string
code_interpreter_config_form_instance = CodeInterpreterConfigForm.from_json(json)
# print the JSON string representation of the object
print(CodeInterpreterConfigForm.to_json())

# convert the object into a dict
code_interpreter_config_form_dict = code_interpreter_config_form_instance.to_dict()
# create an instance of CodeInterpreterConfigForm from a dict
code_interpreter_config_form_from_dict = CodeInterpreterConfigForm.from_dict(code_interpreter_config_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


