# BoardSuccessBuy8

買気配数量8本目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**qty** | **float** | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 

## Example

```python
from kabustation_client.models.board_success_buy8 import BoardSuccessBuy8

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSuccessBuy8 from a JSON string
board_success_buy8_instance = BoardSuccessBuy8.from_json(json)
# print the JSON string representation of the object
print(BoardSuccessBuy8.to_json())

# convert the object into a dict
board_success_buy8_dict = board_success_buy8_instance.to_dict()
# create an instance of BoardSuccessBuy8 from a dict
board_success_buy8_form_dict = board_success_buy8.from_dict(board_success_buy8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


