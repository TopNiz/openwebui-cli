# MessageWithReactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**reply_to_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_pinned** | **bool** |  | [optional] [default to False]
**pinned_by** | **str** |  | [optional] 
**pinned_at** | **int** |  | [optional] 
**content** | **str** |  | 
**data** | **bool** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**user** | [**UserNameResponse**](UserNameResponse.md) |  | [optional] 
**reactions** | [**List[Reactions]**](Reactions.md) |  | 

## Example

```python
from openwebui_client.models.message_with_reactions_response import MessageWithReactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageWithReactionsResponse from a JSON string
message_with_reactions_response_instance = MessageWithReactionsResponse.from_json(json)
# print the JSON string representation of the object
print(MessageWithReactionsResponse.to_json())

# convert the object into a dict
message_with_reactions_response_dict = message_with_reactions_response_instance.to_dict()
# create an instance of MessageWithReactionsResponse from a dict
message_with_reactions_response_from_dict = MessageWithReactionsResponse.from_dict(message_with_reactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


