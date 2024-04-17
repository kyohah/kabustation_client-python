# RankingByCategoryResponseRankingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_false** | **int** | 順位&lt;br&gt;※ランキング内で同じ順位が返却される場合があります（10位が2件など） | [optional] 
**trend** | **str** | トレンド &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;内容&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;対象データ無し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;過去10営業日より20位以上上昇&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;過去10営業日より1～19位上昇&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;過去10営業日と変わらず&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;過去10営業日より1～19位下落&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;過去10営業日より20位以上下落&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**average_ranking** | **float** | 平均順位&lt;br&gt;※100位以下は「999」となります | [optional] 
**category** | **str** | 業種コード | [optional] 
**category_name** | **str** | 業種名 | [optional] 
**current_price** | **float** | 現在値 | [optional] 
**change_ratio** | **float** | 前日比 | [optional] 
**current_price_time** | **str** | 時刻&lt;br&gt;HH:mm&lt;br&gt;※日付は返しません | [optional] 
**change_percentage** | **float** | 騰落率（%） | [optional] 

## Example

```python
from kabustation_client.models.ranking_by_category_response_ranking_inner import RankingByCategoryResponseRankingInner

# TODO update the JSON string below
json = "{}"
# create an instance of RankingByCategoryResponseRankingInner from a JSON string
ranking_by_category_response_ranking_inner_instance = RankingByCategoryResponseRankingInner.from_json(json)
# print the JSON string representation of the object
print(RankingByCategoryResponseRankingInner.to_json())

# convert the object into a dict
ranking_by_category_response_ranking_inner_dict = ranking_by_category_response_ranking_inner_instance.to_dict()
# create an instance of RankingByCategoryResponseRankingInner from a dict
ranking_by_category_response_ranking_inner_form_dict = ranking_by_category_response_ranking_inner.from_dict(ranking_by_category_response_ranking_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


