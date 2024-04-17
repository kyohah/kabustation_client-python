# TokenSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_code** | **int** | 結果コード&lt;br&gt;0が成功。それ以外はエラーコード。 | [optional] 
**token** | **str** | APIトークン | [optional] 

## Example

```python
from kabustation_client.models.token_success import TokenSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of TokenSuccess from a JSON string
token_success_instance = TokenSuccess.from_json(json)
# print the JSON string representation of the object
print(TokenSuccess.to_json())

# convert the object into a dict
token_success_dict = token_success_instance.to_dict()
# create an instance of TokenSuccess from a dict
token_success_form_dict = token_success.from_dict(token_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


