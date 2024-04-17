# MarginPremiumResponseDayTrade

一般信用（デイトレ）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin_premium_type** | **int** | プレミアム料入力区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）非対応銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;プレミアム料がない銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;プレミアム料が固定の銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;プレミアム料が入札で決定する銘柄&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**margin_premium** | **float** | 確定プレミアム料&lt;br&gt; ※入札銘柄の場合、入札受付中は随時更新します。受付時間外は、確定したプレミアム料を返します。&lt;br&gt; ※非入札銘柄の場合、常に固定値を返します。&lt;br&gt; ※信用取引不可の場合、nullを返します。&lt;br&gt; ※19:30~翌営業日のプレミアム料になります。 | [optional] 
**upper_margin_premium** | **float** | 上限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] 
**lower_margin_premium** | **float** | 下限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] 
**tick_margin_premium** | **float** | プレミアム料刻値&lt;br&gt; ※入札可能銘柄以外は、nullを返します。 | [optional] 

## Example

```python
from kabustation_client.models.margin_premium_response_day_trade import MarginPremiumResponseDayTrade

# TODO update the JSON string below
json = "{}"
# create an instance of MarginPremiumResponseDayTrade from a JSON string
margin_premium_response_day_trade_instance = MarginPremiumResponseDayTrade.from_json(json)
# print the JSON string representation of the object
print(MarginPremiumResponseDayTrade.to_json())

# convert the object into a dict
margin_premium_response_day_trade_dict = margin_premium_response_day_trade_instance.to_dict()
# create an instance of MarginPremiumResponseDayTrade from a dict
margin_premium_response_day_trade_form_dict = margin_premium_response_day_trade.from_dict(margin_premium_response_day_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


