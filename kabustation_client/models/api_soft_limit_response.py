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

class ApiSoftLimitResponse(BaseModel):
    """
    ApiSoftLimitResponse
    """ # noqa: E501
    stock: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="現物のワンショット上限<br>※単位は万円", alias="Stock")
    margin: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="信用のワンショット上限<br>※単位は万円", alias="Margin")
    future: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="先物のワンショット上限<br>※単位は枚", alias="Future")
    future_mini: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ミニ先物のワンショット上限<br>※単位は枚", alias="FutureMini")
    future_micro: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="マイクロ先物のワンショット上限<br>※単位は枚", alias="FutureMicro")
    option: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="オプションのワンショット上限<br>※単位は枚", alias="Option")
    mini_option: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ミニオプションのワンショット上限<br>※単位は枚", alias="MiniOption")
    kabu_s_version: Optional[StrictStr] = Field(default=None, description="kabuステーションのバージョン", alias="KabuSVersion")
    __properties: ClassVar[List[str]] = ["Stock", "Margin", "Future", "FutureMini", "FutureMicro", "Option", "MiniOption", "KabuSVersion"]

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
        """Create an instance of ApiSoftLimitResponse from a JSON string"""
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
        """Create an instance of ApiSoftLimitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Stock": obj.get("Stock"),
            "Margin": obj.get("Margin"),
            "Future": obj.get("Future"),
            "FutureMini": obj.get("FutureMini"),
            "FutureMicro": obj.get("FutureMicro"),
            "Option": obj.get("Option"),
            "MiniOption": obj.get("MiniOption"),
            "KabuSVersion": obj.get("KabuSVersion")
        })
        return _obj

