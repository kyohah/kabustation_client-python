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
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class RequestSendOrderDerivFutureReverseLimitOrder(BaseModel):
    """
    逆指値条件<br> ※FrontOrderTypeで逆指値を指定した場合のみ必須。
    """ # noqa: E501
    trigger_price: Union[StrictFloat, StrictInt] = Field(description="トリガ価格<br> ※未設定の場合はエラーになります。<br> ※数字以外が設定された場合はエラーになります。", alias="TriggerPrice")
    under_over: StrictInt = Field(description="以上／以下<br> ※未設定の場合はエラーになります。<br> ※1、2以外が指定された場合はエラーになります。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>以下</td>     </tr>     <tr>       <td>2</td>       <td>以上</td>     </tr>   </tbody> </table>", alias="UnderOver")
    after_hit_order_type: StrictInt = Field(description="ヒット後執行条件<br> ※未設定の場合はエラーになります。<br> ※日通の注文で2以外が指定された場合はエラーになります。<br> ※日中、夜間の注文で1、2以外が指定された場合はエラーになります。<br> ※逆指値（成行）で有効期間条件(TimeInForce)にFAK以外を指定された場合はエラーになります。<br> ※逆指値（指値）で有効期間条件(TimeInForce)にFAS以外を指定された場合はエラーになります。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>成行</td>     </tr>     <tr>       <td>2</td>       <td>指値</td>     </tr>   </tbody> </table>", alias="AfterHitOrderType")
    after_hit_price: Union[StrictFloat, StrictInt] = Field(description="ヒット後注文価格<br> ※未設定の場合はエラーになります。<br> ※数字以外が設定された場合はエラーになります。<br><br> ヒット後執行条件に従い、下記のようにヒット後注文価格を設定してください。 <table>   <thead>       <tr>           <th>ヒット後執行条件</th>           <th>設定価格</th>       </tr>   </thead>   <tbody>     <tr>       <td>成行</td>       <td>0</td>     </tr>     <tr>       <td>指値</td>       <td>指値の単価</td>     </tr>   </tbody> </table>", alias="AfterHitPrice")
    __properties: ClassVar[List[str]] = ["TriggerPrice", "UnderOver", "AfterHitOrderType", "AfterHitPrice"]

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
        """Create an instance of RequestSendOrderDerivFutureReverseLimitOrder from a JSON string"""
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
        """Create an instance of RequestSendOrderDerivFutureReverseLimitOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TriggerPrice": obj.get("TriggerPrice"),
            "UnderOver": obj.get("UnderOver"),
            "AfterHitOrderType": obj.get("AfterHitOrderType"),
            "AfterHitPrice": obj.get("AfterHitPrice")
        })
        return _obj


