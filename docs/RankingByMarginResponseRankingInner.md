# RankingByMarginResponseRankingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_false** | **int** | 順位&lt;br&gt;※ランキング内で同じ順位が返却される場合があります（10位が2件など） | [optional] 
**symbol** | **str** | 銘柄コード | [optional] 
**symbol_name** | **str** | 銘柄名称 | [optional] 
**sell_rapid_payment_percentage** | **float** | 売残（千株） | [optional] 
**sell_last_week_ratio** | **float** | 売残前週比 | [optional] 
**buy_rapid_payment_percentage** | **float** | 買残（千株） | [optional] 
**buy_last_week_ratio** | **float** | 買残前週比 | [optional] 
**ratio** | **float** | 倍率 | [optional] 
**exchange_name** | **str** | 市場名 | [optional] 
**category_name** | **str** | 業種名 | [optional] 

## Example

```python
from kabustation_client.models.ranking_by_margin_response_ranking_inner import RankingByMarginResponseRankingInner

# TODO update the JSON string below
json = "{}"
# create an instance of RankingByMarginResponseRankingInner from a JSON string
ranking_by_margin_response_ranking_inner_instance = RankingByMarginResponseRankingInner.from_json(json)
# print the JSON string representation of the object
print(RankingByMarginResponseRankingInner.to_json())

# convert the object into a dict
ranking_by_margin_response_ranking_inner_dict = ranking_by_margin_response_ranking_inner_instance.to_dict()
# create an instance of RankingByMarginResponseRankingInner from a dict
ranking_by_margin_response_ranking_inner_form_dict = ranking_by_margin_response_ranking_inner.from_dict(ranking_by_margin_response_ranking_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


