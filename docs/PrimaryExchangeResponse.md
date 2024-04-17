# PrimaryExchangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード&lt;br&gt;※対象商品は、株式のみ | [optional] 
**primary_exchange** | **int** | 優先市場 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 

## Example

```python
from kabustation_client.models.primary_exchange_response import PrimaryExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryExchangeResponse from a JSON string
primary_exchange_response_instance = PrimaryExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(PrimaryExchangeResponse.to_json())

# convert the object into a dict
primary_exchange_response_dict = primary_exchange_response_instance.to_dict()
# create an instance of PrimaryExchangeResponse from a dict
primary_exchange_response_form_dict = primary_exchange_response.from_dict(primary_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


