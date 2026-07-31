# ChatTitleIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **int** |  | 
**created_at** | **int** |  | 
**last_read_at** | **int** |  | [optional] 
**snippet** | **str** |  | [optional] 
**active** | **bool** |  | [optional] [default to False]

## Example

```python
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatTitleIdResponse from a JSON string
chat_title_id_response_instance = ChatTitleIdResponse.from_json(json)
# print the JSON string representation of the object
print(ChatTitleIdResponse.to_json())

# convert the object into a dict
chat_title_id_response_dict = chat_title_id_response_instance.to_dict()
# create an instance of ChatTitleIdResponse from a dict
chat_title_id_response_from_dict = ChatTitleIdResponse.from_dict(chat_title_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


