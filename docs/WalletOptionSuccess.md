# WalletOptionSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_buy_trade_limit** | **float** | 買新規建玉可能額 | [optional] 
**option_sell_trade_limit** | **float** | 売新規建玉可能額 | [optional] 
**margin_requirement** | **float** | 必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] 

## Example

```python
from kabustation_client.models.wallet_option_success import WalletOptionSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of WalletOptionSuccess from a JSON string
wallet_option_success_instance = WalletOptionSuccess.from_json(json)
# print the JSON string representation of the object
print(WalletOptionSuccess.to_json())

# convert the object into a dict
wallet_option_success_dict = wallet_option_success_instance.to_dict()
# create an instance of WalletOptionSuccess from a dict
wallet_option_success_form_dict = wallet_option_success.from_dict(wallet_option_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


