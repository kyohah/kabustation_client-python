# ExchangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 通貨 | [optional] 
**bid_price** | **float** | BID | [optional] 
**spread** | **float** | SP | [optional] 
**ask_price** | **float** | ASK | [optional] 
**change** | **float** | 前日比 | [optional] 
**time** | **str** | 時刻 &lt;br&gt;※HH:mm:ss形式 | [optional] 

## Example

```python
from kabustation_client.models.exchange_response import ExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeResponse from a JSON string
exchange_response_instance = ExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeResponse.to_json())

# convert the object into a dict
exchange_response_dict = exchange_response_instance.to_dict()
# create an instance of ExchangeResponse from a dict
exchange_response_form_dict = exchange_response.from_dict(exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


