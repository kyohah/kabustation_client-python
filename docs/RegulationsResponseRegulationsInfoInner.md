# RegulationsResponseRegulationsInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | **int** | 規制市場 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;5&lt;/td&gt;       &lt;td&gt;福証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;6&lt;/td&gt;       &lt;td&gt;札証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;9&lt;/td&gt;       &lt;td&gt;SOR&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;10&lt;/td&gt;       &lt;td&gt;CXJ&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;21&lt;/td&gt;       &lt;td&gt;JNX&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**product** | **int** | 規制取引区分&lt;br&gt; ※空売り規制の場合、「4：新規」 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;現物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;信用新規（制度）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;信用新規（一般）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;4&lt;/td&gt;       &lt;td&gt;新規&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;5&lt;/td&gt;       &lt;td&gt;信用返済（制度）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;6&lt;/td&gt;       &lt;td&gt;信用返済（一般）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;7&lt;/td&gt;       &lt;td&gt;返済&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;8&lt;/td&gt;       &lt;td&gt;品受&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;9&lt;/td&gt;       &lt;td&gt;品渡&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**side** | **str** | 規制売買&lt;br&gt; ※空売り規制の場合、「1：売」 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;売&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;買&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**reason** | **str** | 理由&lt;br&gt;※空売り規制の場合、「空売り規制」 | [optional] 
**limit_start_day** | **str** | 制限開始日&lt;br&gt;yyyy/MM/dd HH:mm形式  &lt;br&gt;※空売り規制の場合、null | [optional] 
**limit_end_day** | **str** | 制限終了日&lt;br&gt;yyyy/MM/dd HH:mm形式  &lt;br&gt;※空売り規制の場合、null | [optional] 
**level** | **int** | コンプライアンスレベル&lt;br&gt; ※空売り規制の場合、null &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;０&lt;/td&gt;       &lt;td&gt;規制無し&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;１&lt;/td&gt;       &lt;td&gt;ワーニング&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;２&lt;/td&gt;       &lt;td&gt;エラー&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 

## Example

```python
from kabustation_client.models.regulations_response_regulations_info_inner import RegulationsResponseRegulationsInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of RegulationsResponseRegulationsInfoInner from a JSON string
regulations_response_regulations_info_inner_instance = RegulationsResponseRegulationsInfoInner.from_json(json)
# print the JSON string representation of the object
print(RegulationsResponseRegulationsInfoInner.to_json())

# convert the object into a dict
regulations_response_regulations_info_inner_dict = regulations_response_regulations_info_inner_instance.to_dict()
# create an instance of RegulationsResponseRegulationsInfoInner from a dict
regulations_response_regulations_info_inner_form_dict = regulations_response_regulations_info_inner.from_dict(regulations_response_regulations_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


