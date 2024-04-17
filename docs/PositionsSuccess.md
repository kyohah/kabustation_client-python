# PositionsSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | 約定番号&lt;br&gt;※現物取引では、nullが返ります。 | [optional] 
**account_type** | **int** | 口座種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;特定&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;法人&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**symbol** | **str** | 銘柄コード | [optional] 
**symbol_name** | **str** | 銘柄名 | [optional] 
**exchange** | **int** | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**exchange_name** | **str** | 市場名 | [optional] 
**security_type** | **int** | 銘柄種別&lt;br&gt;※先物・オプション銘柄の場合のみ | [optional] 
**execution_day** | **int** | 約定日（建玉日）&lt;br&gt;※信用・先物・オプションの場合のみ&lt;br&gt;※現物取引では、nullが返ります。 | [optional] 
**price** | **float** | 値段 | [optional] 
**leaves_qty** | **float** | 残数量（保有数量） | [optional] 
**hold_qty** | **float** | 拘束数量（返済のために拘束されている数量） | [optional] 
**side** | **str** | 売買区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**expenses** | **float** | 諸経費&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] 
**commission** | **float** | 手数料&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] 
**commission_tax** | **float** | 手数料消費税&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] 
**expire_day** | **int** | 返済期日&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] 
**margin_trade_type** | **int** | 信用取引区分&lt;br&gt;※信用の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;制度信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般信用（長期）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**current_price** | **float** | 現在値&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] 
**valuation** | **float** | 評価金額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] 
**profit_loss** | **float** | 評価損益額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] 
**profit_loss_rate** | **float** | 評価損益率&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] 

## Example

```python
from kabustation_client.models.positions_success import PositionsSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of PositionsSuccess from a JSON string
positions_success_instance = PositionsSuccess.from_json(json)
# print the JSON string representation of the object
print(PositionsSuccess.to_json())

# convert the object into a dict
positions_success_dict = positions_success_instance.to_dict()
# create an instance of PositionsSuccess from a dict
positions_success_form_dict = positions_success.from_dict(positions_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


