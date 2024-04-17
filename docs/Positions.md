# Positions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hold_id** | **str** | 返済建玉ID | [optional] 
**qty** | **int** | 返済建玉数量 | [optional] 

## Example

```python
from kabustation_client.models.positions import Positions

# TODO update the JSON string below
json = "{}"
# create an instance of Positions from a JSON string
positions_instance = Positions.from_json(json)
# print the JSON string representation of the object
print(Positions.to_json())

# convert the object into a dict
positions_dict = positions_instance.to_dict()
# create an instance of Positions from a dict
positions_form_dict = positions.from_dict(positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


