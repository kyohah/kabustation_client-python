# MarginPremiumResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード | [optional] 
**general_margin** | [**MarginPremiumResponseGeneralMargin**](MarginPremiumResponseGeneralMargin.md) |  | [optional] 
**day_trade** | [**MarginPremiumResponseDayTrade**](MarginPremiumResponseDayTrade.md) |  | [optional] 

## Example

```python
from kabustation_client.models.margin_premium_response import MarginPremiumResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarginPremiumResponse from a JSON string
margin_premium_response_instance = MarginPremiumResponse.from_json(json)
# print the JSON string representation of the object
print(MarginPremiumResponse.to_json())

# convert the object into a dict
margin_premium_response_dict = margin_premium_response_instance.to_dict()
# create an instance of MarginPremiumResponse from a dict
margin_premium_response_form_dict = margin_premium_response.from_dict(margin_premium_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


