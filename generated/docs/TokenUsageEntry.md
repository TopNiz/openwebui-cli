# TokenUsageEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**input_tokens** | **int** |  | 
**output_tokens** | **int** |  | 
**total_tokens** | **int** |  | 
**message_count** | **int** |  | 

## Example

```python
from openwebui_client.models.token_usage_entry import TokenUsageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TokenUsageEntry from a JSON string
token_usage_entry_instance = TokenUsageEntry.from_json(json)
# print the JSON string representation of the object
print(TokenUsageEntry.to_json())

# convert the object into a dict
token_usage_entry_dict = token_usage_entry_instance.to_dict()
# create an instance of TokenUsageEntry from a dict
token_usage_entry_from_dict = TokenUsageEntry.from_dict(token_usage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


