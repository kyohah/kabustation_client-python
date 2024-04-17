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
from kabustation_client.models.positions import Positions
from kabustation_client.models.request_send_order_reverse_limit_order import RequestSendOrderReverseLimitOrder
from typing import Optional, Set
from typing_extensions import Self

class RequestSendOrder(BaseModel):
    """
    RequestSendOrder
    """ # noqa: E501
    password: StrictStr = Field(description="注文パスワード", alias="Password")
    symbol: StrictStr = Field(description="銘柄コード", alias="Symbol")
    exchange: StrictInt = Field(description="市場コード <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>東証</td>       </tr>       <tr>           <td>3</td>           <td>名証</td>       </tr>       <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>   </tbody> </table>", alias="Exchange")
    security_type: StrictInt = Field(description="商品種別 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>株式</td>       </tr>   </tbody> </table>", alias="SecurityType")
    side: StrictStr = Field(description="売買区分 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>売</td>       </tr>       <tr>           <td>2</td>           <td>買</td>       </tr>   </tbody> </table>", alias="Side")
    cash_margin: StrictInt = Field(description="信用区分 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>現物</td>       </tr>       <tr>           <td>2</td>           <td>新規</td>       </tr>       <tr>           <td>3</td>           <td>返済</td>       </tr>   </tbody> </table>", alias="CashMargin")
    margin_trade_type: Optional[StrictInt] = Field(default=None, description="信用取引区分<br>※現物取引の場合は指定不要。<br>※信用取引の場合、必須。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>制度信用</td>       </tr>       <tr>           <td>2</td>           <td>一般信用（長期）</td>       </tr>       <tr>           <td>3</td>           <td>一般信用（デイトレ）</td>       </tr>   </tbody> </table>", alias="MarginTradeType")
    margin_premium_unit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="１株あたりのプレミアム料(円)<br>  ※プレミアム料の刻値は、プレミアム料取得APIのレスポンスにある\"TickMarginPremium\"にてご確認ください。<br> ※入札受付中(19:30～20:30)プレミアム料入札可能銘柄の場合、「MarginPremiumUnit」は必須となります。<br> ※入札受付中(19:30～20:30)のプレミアム料入札可能銘柄以外の場合は、「MarginPremiumUnit」の記載は無視されます。<br> ※入札受付中以外の時間帯では、「MarginPremiumUnit」の記載は無視されます。", alias="MarginPremiumUnit")
    deliv_type: StrictInt = Field(description="受渡区分<br>※現物買は指定必須。<br>※現物売は「0(指定なし)」を設定<br>※信用新規は「0(指定なし)」を設定<br>※信用返済は指定必須 <br>※auマネーコネクトが有効の場合にのみ、「3」を設定可能 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0</td>           <td>指定なし</td>       </tr>       <tr>           <td>2</td>           <td>お預り金</td>       </tr>       <tr>           <td>3</td>           <td>auマネーコネクト</td>       </tr>   </tbody> </table>", alias="DelivType")
    fund_type: Optional[StrictStr] = Field(default=None, description="資産区分（預り区分）<br>※現物買は、指定必須。<br>※現物売は、「'  '」 半角スペース2つを指定必須。<br>※信用新規と信用返済は、「11」を指定するか、または指定なしでも可。指定しない場合は「11」が自動的にセットされます。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>(半角スペース2つ)</td>           <td>現物売の場合</td>       </tr>       <tr>           <td>02</td>           <td>保護</td>       </tr>       <tr>           <td>AA</td>           <td>信用代用</td>       </tr>       <tr>           <td>11</td>           <td>信用取引</td>       </tr>   </tbody> </table>", alias="FundType")
    account_type: StrictInt = Field(description="口座種別 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>一般</td>       </tr>       <tr>           <td>4</td>           <td>特定</td>       </tr>       <tr>           <td>12</td>           <td>法人</td>       </tr>   </tbody> </table>", alias="AccountType")
    qty: StrictInt = Field(description="注文数量<br>※信用一括返済の場合、返済したい合計数量を入力してください。", alias="Qty")
    close_position_order: Optional[StrictInt] = Field(default=None, description="決済順序<br>※信用返済の場合、必須。<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0</td>           <td>日付（古い順）、損益（高い順）</td>       </tr>       <tr>           <td>1</td>           <td>日付（古い順）、損益（低い順）</td>       </tr>       <tr>           <td>2</td>           <td>日付（新しい順）、損益（高い順）</td>       </tr>       <tr>           <td>3</td>           <td>日付（新しい順）、損益（低い順）</td>       </tr>       <tr>           <td>4</td>           <td>損益（高い順）、日付（古い順）</td>       </tr>       <tr>           <td>5</td>           <td>損益（高い順）、日付（新しい順）</td>       </tr>       <tr>           <td>6</td>           <td>損益（低い順）、日付（古い順）</td>       </tr>       <tr>           <td>7</td>           <td>損益（低い順）、日付（新しい順）</td>       </tr>   </tbody> </table>", alias="ClosePositionOrder")
    close_positions: Optional[List[Positions]] = Field(default=None, description="返済建玉指定<br>※信用返済の場合、必須。<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。<br>※信用一括返済の場合、各建玉IDと返済したい数量を入力してください。<br>※建玉IDは「E」から始まる番号です。", alias="ClosePositions")
    front_order_type: StrictInt = Field(description="執行条件 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>           <th>”Price\"の指定</th>       </tr>   </thead>   <tbody>       <tr>           <td>10</td>           <td>成行</td>           <td>0</td>       </tr>       <tr>           <td>13</td>           <td>寄成（前場）</td>           <td>0</td>       </tr>       <tr>           <td>14</td>           <td>寄成（後場）</td>           <td>0</td>       </tr>       <tr>           <td>15</td>           <td>引成（前場）</td>           <td>0</td>       </tr>       <tr>           <td>16</td>           <td>引成（後場）</td>           <td>0</td>       </tr>       <tr>           <td>17</td>           <td>IOC成行</td>           <td>0</td>       </tr>       <tr>           <td>20</td>           <td>指値</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>21</td>           <td>寄指（前場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>22</td>           <td>寄指（後場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>23</td>           <td>引指（前場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>24</td>           <td>引指（後場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>25</td>           <td>不成（前場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>26</td>           <td>不成（後場）</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>27</td>           <td>IOC指値</td>           <td>発注したい金額</td>       </tr>       <tr>           <td>30</td>           <td>逆指値</td>           <td>指定なし<br>※AfterHitPriceで指定ください</td>       </tr>   </tbody> </table>", alias="FrontOrderType")
    price: Union[StrictFloat, StrictInt] = Field(description="注文価格<br>※FrontOrderTypeで成行を指定した場合、0を指定する。<br>※詳細について、”FrontOrderType”をご確認ください。", alias="Price")
    expire_day: StrictInt = Field(description="注文有効期限<br> yyyyMMdd形式。<br> 「0」を指定すると、kabuステーション上の発注画面の「本日」に対応する日付として扱います。<br> 「本日」は直近の注文可能日となり、以下のように設定されます。<br> 引けまでの間 : 当日<br> 引け後       : 翌取引所営業日<br> 休前日       : 休日明けの取引所営業日<br> ※ 日替わりはkabuステーションが日付変更通知を受信したタイミングです。", alias="ExpireDay")
    reverse_limit_order: Optional[RequestSendOrderReverseLimitOrder] = Field(default=None, alias="ReverseLimitOrder")
    __properties: ClassVar[List[str]] = ["Password", "Symbol", "Exchange", "SecurityType", "Side", "CashMargin", "MarginTradeType", "MarginPremiumUnit", "DelivType", "FundType", "AccountType", "Qty", "ClosePositionOrder", "ClosePositions", "FrontOrderType", "Price", "ExpireDay", "ReverseLimitOrder"]

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
        """Create an instance of RequestSendOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in close_positions (list)
        _items = []
        if self.close_positions:
            for _item in self.close_positions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ClosePositions'] = _items
        # override the default output from pydantic by calling `to_dict()` of reverse_limit_order
        if self.reverse_limit_order:
            _dict['ReverseLimitOrder'] = self.reverse_limit_order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RequestSendOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Password": obj.get("Password"),
            "Symbol": obj.get("Symbol"),
            "Exchange": obj.get("Exchange"),
            "SecurityType": obj.get("SecurityType"),
            "Side": obj.get("Side"),
            "CashMargin": obj.get("CashMargin"),
            "MarginTradeType": obj.get("MarginTradeType"),
            "MarginPremiumUnit": obj.get("MarginPremiumUnit"),
            "DelivType": obj.get("DelivType"),
            "FundType": obj.get("FundType"),
            "AccountType": obj.get("AccountType"),
            "Qty": obj.get("Qty"),
            "ClosePositionOrder": obj.get("ClosePositionOrder"),
            "ClosePositions": [Positions.from_dict(_item) for _item in obj["ClosePositions"]] if obj.get("ClosePositions") is not None else None,
            "FrontOrderType": obj.get("FrontOrderType"),
            "Price": obj.get("Price"),
            "ExpireDay": obj.get("ExpireDay"),
            "ReverseLimitOrder": RequestSendOrderReverseLimitOrder.from_dict(obj["ReverseLimitOrder"]) if obj.get("ReverseLimitOrder") is not None else None
        })
        return _obj


