# RequestCancelOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | 注文番号&lt;br&gt;sendorderのレスポンスで受け取るOrderID。 | 
**password** | **str** | 注文パスワード | 

## Example

```python
from kabustation_client.models.request_cancel_order import RequestCancelOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCancelOrder from a JSON string
request_cancel_order_instance = RequestCancelOrder.from_json(json)
# print the JSON string representation of the object
print(RequestCancelOrder.to_json())

# convert the object into a dict
request_cancel_order_dict = request_cancel_order_instance.to_dict()
# create an instance of RequestCancelOrder from a dict
request_cancel_order_form_dict = request_cancel_order.from_dict(request_cancel_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


