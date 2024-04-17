# RankingByTradeVolumeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 種別 | [optional] 
**exchange_division** | **str** | 市場 | [optional] 
**ranking** | [**List[RankingByTradeVolumeResponseRankingInner]**](RankingByTradeVolumeResponseRankingInner.md) | ランキング | [optional] 

## Example

```python
from kabustation_client.models.ranking_by_trade_volume_response import RankingByTradeVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RankingByTradeVolumeResponse from a JSON string
ranking_by_trade_volume_response_instance = RankingByTradeVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(RankingByTradeVolumeResponse.to_json())

# convert the object into a dict
ranking_by_trade_volume_response_dict = ranking_by_trade_volume_response_instance.to_dict()
# create an instance of RankingByTradeVolumeResponse from a dict
ranking_by_trade_volume_response_form_dict = ranking_by_trade_volume_response.from_dict(ranking_by_trade_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


