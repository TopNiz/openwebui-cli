# ChannelModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**type** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**access_grants** | [**List[AccessGrantModel]**](AccessGrantModel.md) |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**updated_by** | **str** |  | [optional] 
**archived_at** | **int** |  | [optional] 
**archived_by** | **str** |  | [optional] 
**deleted_at** | **int** |  | [optional] 
**deleted_by** | **str** |  | [optional] 

## Example

```python
from openwebui_client.models.channel_model import ChannelModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelModel from a JSON string
channel_model_instance = ChannelModel.from_json(json)
# print the JSON string representation of the object
print(ChannelModel.to_json())

# convert the object into a dict
channel_model_dict = channel_model_instance.to_dict()
# create an instance of ChannelModel from a dict
channel_model_from_dict = ChannelModel.from_dict(channel_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


