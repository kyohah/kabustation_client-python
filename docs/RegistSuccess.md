# RegistSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regist_list** | [**List[RequestRegisterSymbolsInner]**](RequestRegisterSymbolsInner.md) | 現在登録されている銘柄のリスト | [optional] 

## Example

```python
from kabustation_client.models.regist_success import RegistSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of RegistSuccess from a JSON string
regist_success_instance = RegistSuccess.from_json(json)
# print the JSON string representation of the object
print(RegistSuccess.to_json())

# convert the object into a dict
regist_success_dict = regist_success_instance.to_dict()
# create an instance of RegistSuccess from a dict
regist_success_form_dict = regist_success.from_dict(regist_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


