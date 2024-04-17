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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kabustation_client.models.ranking_by_tick_count_response_ranking_inner import RankingByTickCountResponseRankingInner
from typing import Optional, Set
from typing_extensions import Self

class RankingByTickCountResponse(BaseModel):
    """
    RankingByTickCountResponse
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="種別", alias="Type")
    exchange_division: Optional[StrictStr] = Field(default=None, description="市場", alias="ExchangeDivision")
    ranking: Optional[List[RankingByTickCountResponseRankingInner]] = Field(default=None, description="ランキング", alias="Ranking")
    __properties: ClassVar[List[str]] = ["Type", "ExchangeDivision", "Ranking"]

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
        """Create an instance of RankingByTickCountResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ranking (list)
        _items = []
        if self.ranking:
            for _item in self.ranking:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Ranking'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RankingByTickCountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "ExchangeDivision": obj.get("ExchangeDivision"),
            "Ranking": [RankingByTickCountResponseRankingInner.from_dict(_item) for _item in obj["Ranking"]] if obj.get("Ranking") is not None else None
        })
        return _obj


