# OrderSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **int** | 結果コード&lt;br&gt;0が成功。それ以外はエラーコード。 | [optional] 
**order_id** | **str** | 受付注文番号 | [optional] 

## Example

```python
from kabustation_client.models.order_success import OrderSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSuccess from a JSON string
order_success_instance = OrderSuccess.from_json(json)
# print the JSON string representation of the object
print(OrderSuccess.to_json())

# convert the object into a dict
order_success_dict = order_success_instance.to_dict()
# create an instance of OrderSuccess from a dict
order_success_form_dict = order_success.from_dict(order_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


