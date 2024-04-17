# RankingDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 種別 | [optional] 
**exchange_division** | **str** | 市場 | [optional] 
**ranking** | [**List[RankingDefaultResponseRankingInner]**](RankingDefaultResponseRankingInner.md) | ランキング | [optional] 

## Example

```python
from kabustation_client.models.ranking_default_response import RankingDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RankingDefaultResponse from a JSON string
ranking_default_response_instance = RankingDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(RankingDefaultResponse.to_json())

# convert the object into a dict
ranking_default_response_dict = ranking_default_response_instance.to_dict()
# create an instance of RankingDefaultResponse from a dict
ranking_default_response_form_dict = ranking_default_response.from_dict(ranking_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


