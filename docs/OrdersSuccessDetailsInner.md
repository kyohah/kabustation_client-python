# OrdersSuccessDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seq_num** | **int** | ※注文明細レコードの生成順序です。&lt;br&gt;※通番であるとは限りませんが、大小による順序は保たれています。 | [optional] 
**id** | **str** | 注文詳細番号 | [optional] 
**rec_type** | **int** | 明細種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;受付&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;繰越&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;期限切れ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;発注&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;訂正&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;取消&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;失効&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;8&lt;/td&gt;           &lt;td&gt;約定&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**exchange_id** | **str** | 取引所番号 | [optional] 
**state** | **int** | 状態 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;待機（発注待機）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;処理中（発注送信中・訂正送信中・取消送信中）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;処理済（発注済・訂正済・取消済・全約定・期限切れ）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;エラー&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;削除済み&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**transact_time** | **str** | 処理時刻 | [optional] 
**ord_type** | **int** | 執行条件 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;RecType&#x3D;[6] 取消 の場合&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;RecType&#x3D;[3] 期限切れ, [7] 失効, [8] 約定 の場合&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;ザラバ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;寄り&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;不成&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;対当指値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;IOC&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**price** | **float** | 値段 | [optional] 
**qty** | **float** | 数量 | [optional] 
**execution_id** | **str** | 約定番号 | [optional] 
**execution_day** | **datetime** | 約定日時 | [optional] 
**deliv_day** | **int** | 受渡日 | [optional] 
**commission** | **float** | 手数料&lt;br&gt;※注文詳細の明細種別が約定（RecType&#x3D;8)の場合に設定。 | [optional] 
**commission_tax** | **float** | 手数料消費税&lt;br&gt;※明細種別は約定（RecType&#x3D;8）の場合にのみ表示されます。 | [optional] 

## Example

```python
from kabustation_client.models.orders_success_details_inner import OrdersSuccessDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSuccessDetailsInner from a JSON string
orders_success_details_inner_instance = OrdersSuccessDetailsInner.from_json(json)
# print the JSON string representation of the object
print(OrdersSuccessDetailsInner.to_json())

# convert the object into a dict
orders_success_details_inner_dict = orders_success_details_inner_instance.to_dict()
# create an instance of OrdersSuccessDetailsInner from a dict
orders_success_details_inner_form_dict = orders_success_details_inner.from_dict(orders_success_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


