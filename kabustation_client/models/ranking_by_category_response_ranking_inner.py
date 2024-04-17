# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RankingByCategoryResponseRankingInner(BaseModel):
    """
    RankingByCategoryResponseRankingInner
    """ # noqa: E501
    var_false: Optional[StrictInt] = Field(default=None, description="順位<br>※ランキング内で同じ順位が返却される場合があります（10位が2件など）", alias="false")
    trend: Optional[StrictStr] = Field(default=None, description="トレンド <table>   <thead>       <tr>           <th>定義値</th>           <th>内容</th>       </tr>   </thead>   <tbody>       <tr>           <td>0</td>           <td>対象データ無し</td>       </tr>       <tr>           <td>1</td>           <td>過去10営業日より20位以上上昇</td>       </tr>       <tr>           <td>2</td>           <td>過去10営業日より1～19位上昇</td>       </tr>       <tr>           <td>3</td>           <td>過去10営業日と変わらず</td>       </tr>       <tr>           <td>4</td>           <td>過去10営業日より1～19位下落</td>       </tr>       <tr>           <td>5</td>           <td>過去10営業日より20位以上下落</td>       </tr>   </tbody> </table>", alias="Trend")
    average_ranking: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="平均順位<br>※100位以下は「999」となります", alias="AverageRanking")
    category: Optional[StrictStr] = Field(default=None, description="業種コード", alias="Category")
    category_name: Optional[StrictStr] = Field(default=None, description="業種名", alias="CategoryName")
    current_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="現在値", alias="CurrentPrice")
    change_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="前日比", alias="ChangeRatio")
    current_price_time: Optional[StrictStr] = Field(default=None, description="時刻<br>HH:mm<br>※日付は返しません", alias="CurrentPriceTime")
    change_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="騰落率（%）", alias="ChangePercentage")
    __properties: ClassVar[List[str]] = ["false", "Trend", "AverageRanking", "Category", "CategoryName", "CurrentPrice", "ChangeRatio", "CurrentPriceTime", "ChangePercentage"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RankingByCategoryResponseRankingInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RankingByCategoryResponseRankingInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "false": obj.get("false"),
            "Trend": obj.get("Trend"),
            "AverageRanking": obj.get("AverageRanking"),
            "Category": obj.get("Category"),
            "CategoryName": obj.get("CategoryName"),
            "CurrentPrice": obj.get("CurrentPrice"),
            "ChangeRatio": obj.get("ChangeRatio"),
            "CurrentPriceTime": obj.get("CurrentPriceTime"),
            "ChangePercentage": obj.get("ChangePercentage")
        })
        return _obj

