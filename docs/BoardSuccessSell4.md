# BoardSuccessSell4

売気配数量4本目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**qty** | **float** | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 

## Example

```python
from kabustation_client.models.board_success_sell4 import BoardSuccessSell4

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSuccessSell4 from a JSON string
board_success_sell4_instance = BoardSuccessSell4.from_json(json)
# print the JSON string representation of the object
print(BoardSuccessSell4.to_json())

# convert the object into a dict
board_success_sell4_dict = board_success_sell4_instance.to_dict()
# create an instance of BoardSuccessSell4 from a dict
board_success_sell4_form_dict = board_success_sell4.from_dict(board_success_sell4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


