# SessionUserInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 
**profile_image_url** | **str** |  | 
**token** | **str** |  | 
**token_type** | **str** |  | 
**expires_at** | **int** |  | [optional] 
**permissions** | **Dict[str, object]** |  | [optional] 
**bio** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 

## Example

```python
from openwebui_client.models.session_user_info_response import SessionUserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionUserInfoResponse from a JSON string
session_user_info_response_instance = SessionUserInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SessionUserInfoResponse.to_json())

# convert the object into a dict
session_user_info_response_dict = session_user_info_response_instance.to_dict()
# create an instance of SessionUserInfoResponse from a dict
session_user_info_response_from_dict = SessionUserInfoResponse.from_dict(session_user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


