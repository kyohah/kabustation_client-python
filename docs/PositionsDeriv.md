# PositionsDeriv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hold_id** | **str** | 返済建玉ID | [optional] 
**qty** | **int** | 返済建玉数量 | [optional] 

## Example

```python
from kabustation_client.models.positions_deriv import PositionsDeriv

# TODO update the JSON string below
json = "{}"
# create an instance of PositionsDeriv from a JSON string
positions_deriv_instance = PositionsDeriv.from_json(json)
# print the JSON string representation of the object
print(PositionsDeriv.to_json())

# convert the object into a dict
positions_deriv_dict = positions_deriv_instance.to_dict()
# create an instance of PositionsDeriv from a dict
positions_deriv_form_dict = positions_deriv.from_dict(positions_deriv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


