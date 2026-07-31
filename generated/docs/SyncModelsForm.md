# SyncModelsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[ModelModel]**](ModelModel.md) |  | [optional] [default to []]

## Example

```python
from openwebui_client.models.sync_models_form import SyncModelsForm

# TODO update the JSON string below
json = "{}"
# create an instance of SyncModelsForm from a JSON string
sync_models_form_instance = SyncModelsForm.from_json(json)
# print the JSON string representation of the object
print(SyncModelsForm.to_json())

# convert the object into a dict
sync_models_form_dict = sync_models_form_instance.to_dict()
# create an instance of SyncModelsForm from a dict
sync_models_form_from_dict = SyncModelsForm.from_dict(sync_models_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


