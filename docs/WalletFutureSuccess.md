# WalletFutureSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_trade_limit** | **float** | 新規建玉可能額 | [optional] 
**margin_requirement** | **float** | 買い必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] 
**margin_requirement_sell** | **float** | 売り必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] 

## Example

```python
from kabustation_client.models.wallet_future_success import WalletFutureSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of WalletFutureSuccess from a JSON string
wallet_future_success_instance = WalletFutureSuccess.from_json(json)
# print the JSON string representation of the object
print(WalletFutureSuccess.to_json())

# convert the object into a dict
wallet_future_success_dict = wallet_future_success_instance.to_dict()
# create an instance of WalletFutureSuccess from a dict
wallet_future_success_form_dict = wallet_future_success.from_dict(wallet_future_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


