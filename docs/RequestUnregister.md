# RequestUnregister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbols** | [**List[RequestRegisterSymbolsInner]**](RequestRegisterSymbolsInner.md) | ※為替銘柄を登録する場合、銘柄名は\&quot;通貨A\&quot; + \&quot;/\&quot; + \&quot;通貨B\&quot;、市場コードは\&quot;300\&quot;で指定してください。 例：&#39;Symbol&#39;: &#39;EUR/USD&#39;, \&quot;Exchange\&quot;: 300 | [optional] 

## Example

```python
from kabustation_client.models.request_unregister import RequestUnregister

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUnregister from a JSON string
request_unregister_instance = RequestUnregister.from_json(json)
# print the JSON string representation of the object
print(RequestUnregister.to_json())

# convert the object into a dict
request_unregister_dict = request_unregister_instance.to_dict()
# create an instance of RequestUnregister from a dict
request_unregister_form_dict = request_unregister.from_dict(request_unregister_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


