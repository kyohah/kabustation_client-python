# WalletCashSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_account_wallet** | **float** | 現物買付可能額&lt;br&gt; ※auマネーコネクトが有効の場合、auじぶん銀行の残高を含めた合計可能額を表示する&lt;br&gt; ※auマネーコネクトが無効の場合、auカブコム証券の可能額のみを表示する | [optional] 
**au_kc_stock_account_wallet** | **float** | うち、auカブコム証券可能額 | [optional] 
**au_jbn_stock_account_wallet** | **float** | うち、auじぶん銀行残高&lt;br&gt;※auマネーコネクトが無効の場合、「0」を表示する | [optional] 

## Example

```python
from kabustation_client.models.wallet_cash_success import WalletCashSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCashSuccess from a JSON string
wallet_cash_success_instance = WalletCashSuccess.from_json(json)
# print the JSON string representation of the object
print(WalletCashSuccess.to_json())

# convert the object into a dict
wallet_cash_success_dict = wallet_cash_success_instance.to_dict()
# create an instance of WalletCashSuccess from a dict
wallet_cash_success_form_dict = wallet_cash_success.from_dict(wallet_cash_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


