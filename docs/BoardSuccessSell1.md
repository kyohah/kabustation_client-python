# BoardSuccessSell1

売気配数量1本目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | 時刻&lt;br&gt;※株式銘柄の場合のみ | [optional] 
**sign** | **str** | 気配フラグ&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**price** | **float** | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**qty** | **float** | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 

## Example

```python
from kabustation_client.models.board_success_sell1 import BoardSuccessSell1

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSuccessSell1 from a JSON string
board_success_sell1_instance = BoardSuccessSell1.from_json(json)
# print the JSON string representation of the object
print(BoardSuccessSell1.to_json())

# convert the object into a dict
board_success_sell1_dict = board_success_sell1_instance.to_dict()
# create an instance of BoardSuccessSell1 from a dict
board_success_sell1_form_dict = board_success_sell1.from_dict(board_success_sell1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


