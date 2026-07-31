# AdminConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_admin_details** | **bool** |  | 
**admin_email** | **str** |  | [optional] 
**webui_url** | **str** |  | 
**enable_signup** | **bool** |  | 
**enable_api_keys** | **bool** |  | 
**enable_api_keys_endpoint_restrictions** | **bool** |  | 
**api_keys_allowed_endpoints** | **str** |  | 
**default_user_role** | **str** |  | 
**default_group_id** | **str** |  | 
**jwt_expires_in** | **str** |  | 
**enable_community_sharing** | **bool** |  | 
**enable_message_rating** | **bool** |  | 
**enable_folders** | **bool** |  | 
**folder_max_file_count** | [**FolderMaxFileCount**](FolderMaxFileCount.md) |  | [optional] 
**automation_max_count** | [**AutomationMaxCount**](AutomationMaxCount.md) |  | [optional] 
**automation_min_interval** | [**AutomationMinInterval**](AutomationMinInterval.md) |  | [optional] 
**enable_automations** | **bool** |  | 
**enable_channels** | **bool** |  | 
**channel_model_response_mode** | **str** |  | [optional] [default to 'thread']
**enable_calendar** | **bool** |  | 
**enable_memories** | **bool** |  | 
**enable_memory_system_context** | **bool** |  | 
**enable_notes** | **bool** |  | 
**enable_user_webhooks** | **bool** |  | 
**enable_user_status** | **bool** |  | 
**pending_user_overlay_title** | **str** |  | [optional] 
**pending_user_overlay_content** | **str** |  | [optional] 
**response_watermark** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.admin_config import AdminConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConfig from a JSON string
admin_config_instance = AdminConfig.from_json(json)
# print the JSON string representation of the object
print(AdminConfig.to_json())

# convert the object into a dict
admin_config_dict = admin_config_instance.to_dict()
# create an instance of AdminConfig from a dict
admin_config_from_dict = AdminConfig.from_dict(admin_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


