# MessageStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**model** | **str** |  | [optional] 
**content_length** | **int** |  | 
**token_count** | **int** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**rating** | **int** |  | [optional] 
**tags** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from openwebui_client.models.message_stats import MessageStats

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStats from a JSON string
message_stats_instance = MessageStats.from_json(json)
# print the JSON string representation of the object
print(MessageStats.to_json())

# convert the object into a dict
message_stats_dict = message_stats_instance.to_dict()
# create an instance of MessageStats from a dict
message_stats_from_dict = MessageStats.from_dict(message_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


