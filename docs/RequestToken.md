# RequestToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_password** | **str** | APIパスワード | 

## Example

```python
from kabustation_client.models.request_token import RequestToken

# TODO update the JSON string below
json = "{}"
# create an instance of RequestToken from a JSON string
request_token_instance = RequestToken.from_json(json)
# print the JSON string representation of the object
print(RequestToken.to_json())

# convert the object into a dict
request_token_dict = request_token_instance.to_dict()
# create an instance of RequestToken from a dict
request_token_form_dict = request_token.from_dict(request_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


