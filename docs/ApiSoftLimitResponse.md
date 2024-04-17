# ApiSoftLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock** | **float** | 現物のワンショット上限&lt;br&gt;※単位は万円 | [optional] 
**margin** | **float** | 信用のワンショット上限&lt;br&gt;※単位は万円 | [optional] 
**future** | **float** | 先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] 
**future_mini** | **float** | ミニ先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] 
**future_micro** | **float** | マイクロ先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] 
**option** | **float** | オプションのワンショット上限&lt;br&gt;※単位は枚 | [optional] 
**mini_option** | **float** | ミニオプションのワンショット上限&lt;br&gt;※単位は枚 | [optional] 
**kabu_s_version** | **str** | kabuステーションのバージョン | [optional] 

## Example

```python
from kabustation_client.models.api_soft_limit_response import ApiSoftLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSoftLimitResponse from a JSON string
api_soft_limit_response_instance = ApiSoftLimitResponse.from_json(json)
# print the JSON string representation of the object
print(ApiSoftLimitResponse.to_json())

# convert the object into a dict
api_soft_limit_response_dict = api_soft_limit_response_instance.to_dict()
# create an instance of ApiSoftLimitResponse from a dict
api_soft_limit_response_form_dict = api_soft_limit_response.from_dict(api_soft_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


