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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class WalletOptionSuccess(BaseModel):
    """
    WalletOptionSuccess
    """ # noqa: E501
    option_buy_trade_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="買新規建玉可能額", alias="OptionBuyTradeLimit")
    option_sell_trade_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="売新規建玉可能額", alias="OptionSellTradeLimit")
    margin_requirement: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="必要証拠金額<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、空を返す。", alias="MarginRequirement")
    __properties: ClassVar[List[str]] = ["OptionBuyTradeLimit", "OptionSellTradeLimit", "MarginRequirement"]

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
        """Create an instance of WalletOptionSuccess from a JSON string"""
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
        """Create an instance of WalletOptionSuccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OptionBuyTradeLimit": obj.get("OptionBuyTradeLimit"),
            "OptionSellTradeLimit": obj.get("OptionSellTradeLimit"),
            "MarginRequirement": obj.get("MarginRequirement")
        })
        return _obj


