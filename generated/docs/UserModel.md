# UserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**username** | **str** |  | [optional] 
**role** | **str** |  | [optional] [default to 'pending']
**name** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 
**profile_banner_image_url** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**timezone** | **str** |  | [optional] 
**presence_state** | **str** |  | [optional] 
**status_emoji** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**status_expires_at** | **int** |  | [optional] 
**info** | **Dict[str, object]** |  | [optional] 
**settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**oauth** | **Dict[str, object]** |  | [optional] 
**scim** | **Dict[str, object]** |  | [optional] 
**last_active_at** | **int** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from openwebui_client.models.user_model import UserModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserModel from a JSON string
user_model_instance = UserModel.from_json(json)
# print the JSON string representation of the object
print(UserModel.to_json())

# convert the object into a dict
user_model_dict = user_model_instance.to_dict()
# create an instance of UserModel from a dict
user_model_from_dict = UserModel.from_dict(user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


