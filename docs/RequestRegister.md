# RequestRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbols** | [**List[RequestRegisterSymbolsInner]**](RequestRegisterSymbolsInner.md) |  | [optional] 

## Example

```python
from kabustation_client.models.request_register import RequestRegister

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRegister from a JSON string
request_register_instance = RequestRegister.from_json(json)
# print the JSON string representation of the object
print(RequestRegister.to_json())

# convert the object into a dict
request_register_dict = request_register_instance.to_dict()
# create an instance of RequestRegister from a dict
request_register_form_dict = request_register.from_dict(request_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


