# BoardSuccessSell9

売気配数量9本目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**qty** | **float** | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 

## Example

```python
from kabustation_client.models.board_success_sell9 import BoardSuccessSell9

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSuccessSell9 from a JSON string
board_success_sell9_instance = BoardSuccessSell9.from_json(json)
# print the JSON string representation of the object
print(BoardSuccessSell9.to_json())

# convert the object into a dict
board_success_sell9_dict = board_success_sell9_instance.to_dict()
# create an instance of BoardSuccessSell9 from a dict
board_success_sell9_form_dict = board_success_sell9.from_dict(board_success_sell9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

