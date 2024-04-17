# RankingByMarginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 種別 | [optional] 
**exchange_division** | **str** | 市場 | [optional] 
**ranking** | [**List[RankingByMarginResponseRankingInner]**](RankingByMarginResponseRankingInner.md) | ランキング | [optional] 

## Example

```python
from kabustation_client.models.ranking_by_margin_response import RankingByMarginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RankingByMarginResponse from a JSON string
ranking_by_margin_response_instance = RankingByMarginResponse.from_json(json)
# print the JSON string representation of the object
print(RankingByMarginResponse.to_json())

# convert the object into a dict
ranking_by_margin_response_dict = ranking_by_margin_response_instance.to_dict()
# create an instance of RankingByMarginResponse from a dict
ranking_by_margin_response_form_dict = ranking_by_margin_response.from_dict(ranking_by_margin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


