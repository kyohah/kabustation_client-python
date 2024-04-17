# RankingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 種別&lt;br&gt; ※業種別値上がり率、業種別値下がり率の場合、市場は「null」になります | [optional] 
**exchange_division** | **str** | 市場 | [optional] 
**ranking** | [**List[RankingByCategoryResponseRankingInner]**](RankingByCategoryResponseRankingInner.md) | ランキング | [optional] 

## Example

```python
from kabustation_client.models.ranking_get200_response import RankingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RankingGet200Response from a JSON string
ranking_get200_response_instance = RankingGet200Response.from_json(json)
# print the JSON string representation of the object
print(RankingGet200Response.to_json())

# convert the object into a dict
ranking_get200_response_dict = ranking_get200_response_instance.to_dict()
# create an instance of RankingGet200Response from a dict
ranking_get200_response_form_dict = ranking_get200_response.from_dict(ranking_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


