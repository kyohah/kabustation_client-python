# RequestRegisterSymbolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード | [optional] 
**exchange** | **int** | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 

## Example

```python
from kabustation_client.models.request_register_symbols_inner import RequestRegisterSymbolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRegisterSymbolsInner from a JSON string
request_register_symbols_inner_instance = RequestRegisterSymbolsInner.from_json(json)
# print the JSON string representation of the object
print(RequestRegisterSymbolsInner.to_json())

# convert the object into a dict
request_register_symbols_inner_dict = request_register_symbols_inner_instance.to_dict()
# create an instance of RequestRegisterSymbolsInner from a dict
request_register_symbols_inner_form_dict = request_register_symbols_inner.from_dict(request_register_symbols_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


