# SymbolNameSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード | [optional] 
**symbol_name** | **str** | 銘柄名称 | [optional] 

## Example

```python
from kabustation_client.models.symbol_name_success import SymbolNameSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolNameSuccess from a JSON string
symbol_name_success_instance = SymbolNameSuccess.from_json(json)
# print the JSON string representation of the object
print(SymbolNameSuccess.to_json())

# convert the object into a dict
symbol_name_success_dict = symbol_name_success_instance.to_dict()
# create an instance of SymbolNameSuccess from a dict
symbol_name_success_form_dict = symbol_name_success.from_dict(symbol_name_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


