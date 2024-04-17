# RequestSendOrderReverseLimitOrder

逆指値条件<br> ※FrontOrderTypeで逆指値を指定した場合のみ必須。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_sec** | **int** | トリガ銘柄&lt;br&gt; ※未設定の場合はエラーになります。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;発注銘柄&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;NK225指数&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;TOPIX指数&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 
**trigger_price** | **float** | トリガ価格&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※数字以外が設定された場合はエラーになります。 | 
**under_over** | **int** | 以上／以下&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※1、2以外が指定された場合はエラーになります。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;以下&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;以上&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 
**after_hit_order_type** | **int** | ヒット後執行条件&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※1、2、3以外が指定された場合はエラーになります。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;成行&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;指値&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;不成&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 
**after_hit_price** | **float** | ヒット後注文価格&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※数字以外が設定された場合はエラーになります。&lt;br&gt;&lt;br&gt; ヒット後執行条件に従い、下記のようにヒット後注文価格を設定してください。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;ヒット後執行条件&lt;/th&gt;           &lt;th&gt;設定価格&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;成行&lt;/td&gt;       &lt;td&gt;0&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;指値&lt;/td&gt;       &lt;td&gt;指値の単価&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;不成&lt;/td&gt;       &lt;td&gt;不成の単価&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 

## Example

```python
from kabustation_client.models.request_send_order_reverse_limit_order import RequestSendOrderReverseLimitOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSendOrderReverseLimitOrder from a JSON string
request_send_order_reverse_limit_order_instance = RequestSendOrderReverseLimitOrder.from_json(json)
# print the JSON string representation of the object
print(RequestSendOrderReverseLimitOrder.to_json())

# convert the object into a dict
request_send_order_reverse_limit_order_dict = request_send_order_reverse_limit_order_instance.to_dict()
# create an instance of RequestSendOrderReverseLimitOrder from a dict
request_send_order_reverse_limit_order_form_dict = request_send_order_reverse_limit_order.from_dict(request_send_order_reverse_limit_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


