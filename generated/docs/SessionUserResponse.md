# SessionUserResponse


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
**expires_at** | **int** |  | [optional] 
**permissions** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openwebui_client.models.session_user_response import SessionUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionUserResponse from a JSON string
session_user_response_instance = SessionUserResponse.from_json(json)
# print the JSON string representation of the object
print(SessionUserResponse.to_json())

# convert the object into a dict
session_user_response_dict = session_user_response_instance.to_dict()
# create an instance of SessionUserResponse from a dict
session_user_response_from_dict = SessionUserResponse.from_dict(session_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


