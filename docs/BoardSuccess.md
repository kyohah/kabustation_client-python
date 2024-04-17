# BoardSuccess

下記にあるBIDとASKとは、トレーダー目線から見た場合の値であるため、BidPrice=Sell1のPrice、AskPrice=Buy1のPriceという数値となります。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード | [optional] 
**symbol_name** | **str** | 銘柄名 | [optional] 
**exchange** | **int** | 市場コード&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**exchange_name** | **str** | 市場名称&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**current_price** | **float** | 現値 | [optional] 
**current_price_time** | **datetime** | 現値時刻 | [optional] 
**current_price_change_status** | **str** | 現値前値比較 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0056&lt;/td&gt;           &lt;td&gt;変わらず&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0057&lt;/td&gt;           &lt;td&gt;UP&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0058&lt;/td&gt;           &lt;td&gt;DOWN&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0059&lt;/td&gt;           &lt;td&gt;中断板寄り後の初値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0060&lt;/td&gt;           &lt;td&gt;ザラバ引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0061&lt;/td&gt;           &lt;td&gt;板寄り引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0062&lt;/td&gt;           &lt;td&gt;中断引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0063&lt;/td&gt;           &lt;td&gt;ダウン引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0064&lt;/td&gt;           &lt;td&gt;逆転終値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0066&lt;/td&gt;           &lt;td&gt;特別気配引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0067&lt;/td&gt;           &lt;td&gt;一時留保引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0068&lt;/td&gt;           &lt;td&gt;売買停止引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0069&lt;/td&gt;           &lt;td&gt;サーキットブレーカ引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0431&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレーカ引け&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**current_price_status** | **int** | 現値ステータス &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;現値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;不連続歩み&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;板寄せ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;システム障害&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;中断&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;売買停止&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;売買停止・システム停止解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;8&lt;/td&gt;           &lt;td&gt;終値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;システム停止&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;10&lt;/td&gt;           &lt;td&gt;概算値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;11&lt;/td&gt;           &lt;td&gt;参考値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;サーキットブレイク実施中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;13&lt;/td&gt;           &lt;td&gt;システム障害解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;14&lt;/td&gt;           &lt;td&gt;サーキットブレイク解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;15&lt;/td&gt;           &lt;td&gt;中断解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;16&lt;/td&gt;           &lt;td&gt;一時留保中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;17&lt;/td&gt;           &lt;td&gt;一時留保解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;18&lt;/td&gt;           &lt;td&gt;ファイル障害&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;19&lt;/td&gt;           &lt;td&gt;ファイル障害解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;20&lt;/td&gt;           &lt;td&gt;Spread/Strategy&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;21&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレイク発動&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;22&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレイク解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;板寄せ約定&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**calc_price** | **float** | 計算用現値 | [optional] 
**previous_close** | **float** | 前日終値 | [optional] 
**previous_close_time** | **datetime** | 前日終値日付 | [optional] 
**change_previous_close** | **float** | 前日比 | [optional] 
**change_previous_close_per** | **float** | 騰落率 | [optional] 
**opening_price** | **float** | 始値 | [optional] 
**opening_price_time** | **datetime** | 始値時刻 | [optional] 
**high_price** | **float** | 高値 | [optional] 
**high_price_time** | **datetime** | 高値時刻 | [optional] 
**low_price** | **float** | 安値 | [optional] 
**low_price_time** | **datetime** | 安値時刻 | [optional] 
**trading_volume** | **float** | 売買高&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**trading_volume_time** | **datetime** | 売買高時刻&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**vwap** | **float** | 売買高加重平均価格（VWAP）&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**trading_value** | **float** | 売買代金&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**bid_qty** | **float** | 最良売気配数量 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**bid_price** | **float** | 最良売気配値段 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**bid_time** | **datetime** | 最良売気配時刻 ※①&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**bid_sign** | **str** | 最良売気配フラグ ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**market_order_sell_qty** | **float** | 売成行数量&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**sell1** | [**BoardSuccessSell1**](BoardSuccessSell1.md) |  | [optional] 
**sell2** | [**BoardSuccessSell2**](BoardSuccessSell2.md) |  | [optional] 
**sell3** | [**BoardSuccessSell3**](BoardSuccessSell3.md) |  | [optional] 
**sell4** | [**BoardSuccessSell4**](BoardSuccessSell4.md) |  | [optional] 
**sell5** | [**BoardSuccessSell5**](BoardSuccessSell5.md) |  | [optional] 
**sell6** | [**BoardSuccessSell6**](BoardSuccessSell6.md) |  | [optional] 
**sell7** | [**BoardSuccessSell7**](BoardSuccessSell7.md) |  | [optional] 
**sell8** | [**BoardSuccessSell8**](BoardSuccessSell8.md) |  | [optional] 
**sell9** | [**BoardSuccessSell9**](BoardSuccessSell9.md) |  | [optional] 
**sell10** | [**BoardSuccessSell10**](BoardSuccessSell10.md) |  | [optional] 
**ask_qty** | **float** | 最良買気配数量 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**ask_price** | **float** | 最良買気配値段 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**ask_time** | **datetime** | 最良買気配時刻 ※①&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**ask_sign** | **str** | 最良買気配フラグ ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**market_order_buy_qty** | **float** | 買成行数量&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**buy1** | [**BoardSuccessBuy1**](BoardSuccessBuy1.md) |  | [optional] 
**buy2** | [**BoardSuccessBuy2**](BoardSuccessBuy2.md) |  | [optional] 
**buy3** | [**BoardSuccessBuy3**](BoardSuccessBuy3.md) |  | [optional] 
**buy4** | [**BoardSuccessBuy4**](BoardSuccessBuy4.md) |  | [optional] 
**buy5** | [**BoardSuccessBuy5**](BoardSuccessBuy5.md) |  | [optional] 
**buy6** | [**BoardSuccessBuy6**](BoardSuccessBuy6.md) |  | [optional] 
**buy7** | [**BoardSuccessBuy7**](BoardSuccessBuy7.md) |  | [optional] 
**buy8** | [**BoardSuccessBuy8**](BoardSuccessBuy8.md) |  | [optional] 
**buy9** | [**BoardSuccessBuy9**](BoardSuccessBuy9.md) |  | [optional] 
**buy10** | [**BoardSuccessBuy10**](BoardSuccessBuy10.md) |  | [optional] 
**over_sell_qty** | **float** | OVER気配数量&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**under_buy_qty** | **float** | UNDER気配数量&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**total_market_value** | **float** | 時価総額&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**clearing_price** | **float** | 清算値&lt;br&gt;※先物銘柄の場合のみ | [optional] 
**iv** | **float** | インプライド・ボラティリティ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] 
**gamma** | **float** | ガンマ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] 
**theta** | **float** | セータ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] 
**vega** | **float** | ベガ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] 
**delta** | **float** | デルタ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] 
**security_type** | **int** | 銘柄種別 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;指数&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;現物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;101&lt;/td&gt;       &lt;td&gt;日経225先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;103&lt;/td&gt;       &lt;td&gt;日経225OP&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;107&lt;/td&gt;       &lt;td&gt;TOPIX先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;121&lt;/td&gt;       &lt;td&gt;JPX400先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;144&lt;/td&gt;       &lt;td&gt;NYダウ&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;145&lt;/td&gt;       &lt;td&gt;日経平均VI&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;154&lt;/td&gt;       &lt;td&gt;グロース250先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;155&lt;/td&gt;       &lt;td&gt;TOPIX_REIT&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;171&lt;/td&gt;       &lt;td&gt;TOPIX CORE30&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;901&lt;/td&gt;       &lt;td&gt;日経平均225ミニ先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;907&lt;/td&gt;       &lt;td&gt;TOPIXミニ先物&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 

## Example

```python
from kabustation_client.models.board_success import BoardSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSuccess from a JSON string
board_success_instance = BoardSuccess.from_json(json)
# print the JSON string representation of the object
print(BoardSuccess.to_json())

# convert the object into a dict
board_success_dict = board_success_instance.to_dict()
# create an instance of BoardSuccess from a dict
board_success_form_dict = board_success.from_dict(board_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


