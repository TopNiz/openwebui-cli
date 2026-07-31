# SigninResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 
**profile_image_url** | **str** |  | 
**token** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from openwebui_client.models.signin_response import SigninResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SigninResponse from a JSON string
signin_response_instance = SigninResponse.from_json(json)
# print the JSON string representation of the object
print(SigninResponse.to_json())

# convert the object into a dict
signin_response_dict = signin_response_instance.to_dict()
# create an instance of SigninResponse from a dict
signin_response_from_dict = SigninResponse.from_dict(signin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


