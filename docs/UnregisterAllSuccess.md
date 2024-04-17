# UnregisterAllSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regist_list** | **object** | 現在登録されている銘柄のリスト&lt;br&gt;※銘柄登録解除が正常に行われれば、空リストを返します。&lt;br&gt;　登録解除でエラー等が発生した場合、現在登録されている銘柄のリストを返します | [optional] 

## Example

```python
from kabustation_client.models.unregister_all_success import UnregisterAllSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterAllSuccess from a JSON string
unregister_all_success_instance = UnregisterAllSuccess.from_json(json)
# print the JSON string representation of the object
print(UnregisterAllSuccess.to_json())

# convert the object into a dict
unregister_all_success_dict = unregister_all_success_instance.to_dict()
# create an instance of UnregisterAllSuccess from a dict
unregister_all_success_form_dict = unregister_all_success.from_dict(unregister_all_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


