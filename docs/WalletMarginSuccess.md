# WalletMarginSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin_account_wallet** | **float** | 信用新規可能額 | [optional] 
**depositkeep_rate** | **float** | 保証金維持率&lt;br&gt;※銘柄指定の場合のみ&lt;br&gt;※銘柄が指定されなかった場合、0.0を返す。 | [optional] 
**consignment_deposit_rate** | **float** | 委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] 
**cash_of_consignment_deposit_rate** | **float** | 現金委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] 

## Example

```python
from kabustation_client.models.wallet_margin_success import WalletMarginSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of WalletMarginSuccess from a JSON string
wallet_margin_success_instance = WalletMarginSuccess.from_json(json)
# print the JSON string representation of the object
print(WalletMarginSuccess.to_json())

# convert the object into a dict
wallet_margin_success_dict = wallet_margin_success_instance.to_dict()
# create an instance of WalletMarginSuccess from a dict
wallet_margin_success_form_dict = wallet_margin_success.from_dict(wallet_margin_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


