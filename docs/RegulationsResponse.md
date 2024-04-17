# RegulationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | 銘柄コード&lt;br&gt; ※対象商品は、株式のみ | [optional] 
**regulations_info** | [**List[RegulationsResponseRegulationsInfoInner]**](RegulationsResponseRegulationsInfoInner.md) | 規制情報 | [optional] 

## Example

```python
from kabustation_client.models.regulations_response import RegulationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegulationsResponse from a JSON string
regulations_response_instance = RegulationsResponse.from_json(json)
# print the JSON string representation of the object
print(RegulationsResponse.to_json())

# convert the object into a dict
regulations_response_dict = regulations_response_instance.to_dict()
# create an instance of RegulationsResponse from a dict
regulations_response_form_dict = regulations_response.from_dict(regulations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


