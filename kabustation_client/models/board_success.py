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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from kabustation_client.models.board_success_buy1 import BoardSuccessBuy1
from kabustation_client.models.board_success_buy10 import BoardSuccessBuy10
from kabustation_client.models.board_success_buy2 import BoardSuccessBuy2
from kabustation_client.models.board_success_buy3 import BoardSuccessBuy3
from kabustation_client.models.board_success_buy4 import BoardSuccessBuy4
from kabustation_client.models.board_success_buy5 import BoardSuccessBuy5
from kabustation_client.models.board_success_buy6 import BoardSuccessBuy6
from kabustation_client.models.board_success_buy7 import BoardSuccessBuy7
from kabustation_client.models.board_success_buy8 import BoardSuccessBuy8
from kabustation_client.models.board_success_buy9 import BoardSuccessBuy9
from kabustation_client.models.board_success_sell1 import BoardSuccessSell1
from kabustation_client.models.board_success_sell10 import BoardSuccessSell10
from kabustation_client.models.board_success_sell2 import BoardSuccessSell2
from kabustation_client.models.board_success_sell3 import BoardSuccessSell3
from kabustation_client.models.board_success_sell4 import BoardSuccessSell4
from kabustation_client.models.board_success_sell5 import BoardSuccessSell5
from kabustation_client.models.board_success_sell6 import BoardSuccessSell6
from kabustation_client.models.board_success_sell7 import BoardSuccessSell7
from kabustation_client.models.board_success_sell8 import BoardSuccessSell8
from kabustation_client.models.board_success_sell9 import BoardSuccessSell9
from typing import Optional, Set
from typing_extensions import Self

class BoardSuccess(BaseModel):
    """
    下記にあるBIDとASKとは、トレーダー目線から見た場合の値であるため、BidPrice=Sell1のPrice、AskPrice=Buy1のPriceという数値となります。
    """ # noqa: E501
    symbol: Optional[StrictStr] = Field(default=None, description="銘柄コード", alias="Symbol")
    symbol_name: Optional[StrictStr] = Field(default=None, description="銘柄名", alias="SymbolName")
    exchange: Optional[StrictInt] = Field(default=None, description="市場コード<br>※株式・先物・オプション銘柄の場合のみ <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>東証</td>       </tr>       <tr>           <td>3</td>           <td>名証</td>       </tr>       <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table>", alias="Exchange")
    exchange_name: Optional[StrictStr] = Field(default=None, description="市場名称<br>※株式・先物・オプション銘柄の場合のみ", alias="ExchangeName")
    current_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="現値", alias="CurrentPrice")
    current_price_time: Optional[datetime] = Field(default=None, description="現値時刻", alias="CurrentPriceTime")
    current_price_change_status: Optional[StrictStr] = Field(default=None, description="現値前値比較 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0000</td>           <td>事象なし</td>       </tr>       <tr>           <td>0056</td>           <td>変わらず</td>       </tr>       <tr>           <td>0057</td>           <td>UP</td>       </tr>       <tr>           <td>0058</td>           <td>DOWN</td>       </tr>       <tr>           <td>0059</td>           <td>中断板寄り後の初値</td>       </tr>       <tr>           <td>0060</td>           <td>ザラバ引け</td>       </tr>       <tr>           <td>0061</td>           <td>板寄り引け</td>       </tr>       <tr>           <td>0062</td>           <td>中断引け</td>       </tr>       <tr>           <td>0063</td>           <td>ダウン引け</td>       </tr>       <tr>           <td>0064</td>           <td>逆転終値</td>       </tr>       <tr>           <td>0066</td>           <td>特別気配引け</td>       </tr>       <tr>           <td>0067</td>           <td>一時留保引け</td>       </tr>       <tr>           <td>0068</td>           <td>売買停止引け</td>       </tr>       <tr>           <td>0069</td>           <td>サーキットブレーカ引け</td>       </tr>       <tr>           <td>0431</td>           <td>ダイナミックサーキットブレーカ引け</td>       </tr>   </tbody> </table>", alias="CurrentPriceChangeStatus")
    current_price_status: Optional[StrictInt] = Field(default=None, description="現値ステータス <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>現値</td>       </tr>       <tr>           <td>2</td>           <td>不連続歩み</td>       </tr>       <tr>           <td>3</td>           <td>板寄せ</td>       </tr>       <tr>           <td>4</td>           <td>システム障害</td>       </tr>       <tr>           <td>5</td>           <td>中断</td>       </tr>       <tr>           <td>6</td>           <td>売買停止</td>       </tr>       <tr>           <td>7</td>           <td>売買停止・システム停止解除</td>       </tr>       <tr>           <td>8</td>           <td>終値</td>       </tr>       <tr>           <td>9</td>           <td>システム停止</td>       </tr>       <tr>           <td>10</td>           <td>概算値</td>       </tr>       <tr>           <td>11</td>           <td>参考値</td>       </tr>       <tr>           <td>12</td>           <td>サーキットブレイク実施中</td>       </tr>       <tr>           <td>13</td>           <td>システム障害解除</td>       </tr>       <tr>           <td>14</td>           <td>サーキットブレイク解除</td>       </tr>       <tr>           <td>15</td>           <td>中断解除</td>       </tr>       <tr>           <td>16</td>           <td>一時留保中</td>       </tr>       <tr>           <td>17</td>           <td>一時留保解除</td>       </tr>       <tr>           <td>18</td>           <td>ファイル障害</td>       </tr>       <tr>           <td>19</td>           <td>ファイル障害解除</td>       </tr>       <tr>           <td>20</td>           <td>Spread/Strategy</td>       </tr>       <tr>           <td>21</td>           <td>ダイナミックサーキットブレイク発動</td>       </tr>       <tr>           <td>22</td>           <td>ダイナミックサーキットブレイク解除</td>       </tr>       <tr>           <td>23</td>           <td>板寄せ約定</td>       </tr>   </tbody> </table>", alias="CurrentPriceStatus")
    calc_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="計算用現値", alias="CalcPrice")
    previous_close: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="前日終値", alias="PreviousClose")
    previous_close_time: Optional[datetime] = Field(default=None, description="前日終値日付", alias="PreviousCloseTime")
    change_previous_close: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="前日比", alias="ChangePreviousClose")
    change_previous_close_per: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="騰落率", alias="ChangePreviousClosePer")
    opening_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="始値", alias="OpeningPrice")
    opening_price_time: Optional[datetime] = Field(default=None, description="始値時刻", alias="OpeningPriceTime")
    high_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="高値", alias="HighPrice")
    high_price_time: Optional[datetime] = Field(default=None, description="高値時刻", alias="HighPriceTime")
    low_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="安値", alias="LowPrice")
    low_price_time: Optional[datetime] = Field(default=None, description="安値時刻", alias="LowPriceTime")
    trading_volume: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="売買高<br>※株式・先物・オプション銘柄の場合のみ", alias="TradingVolume")
    trading_volume_time: Optional[datetime] = Field(default=None, description="売買高時刻<br>※株式・先物・オプション銘柄の場合のみ", alias="TradingVolumeTime")
    vwap: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="売買高加重平均価格（VWAP）<br>※株式・先物・オプション銘柄の場合のみ", alias="VWAP")
    trading_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="売買代金<br>※株式・先物・オプション銘柄の場合のみ", alias="TradingValue")
    bid_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="最良売気配数量 ※①<br>※株式・先物・オプション銘柄の場合のみ", alias="BidQty")
    bid_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="最良売気配値段 ※①<br>※株式・先物・オプション銘柄の場合のみ", alias="BidPrice")
    bid_time: Optional[datetime] = Field(default=None, description="最良売気配時刻 ※①<br>※株式銘柄の場合のみ", alias="BidTime")
    bid_sign: Optional[StrictStr] = Field(default=None, description="最良売気配フラグ ※①<br>※株式・先物・オプション銘柄の場合のみ <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0000</td>           <td>事象なし</td>       </tr>       <tr>           <td>0101</td>           <td>一般気配</td>       </tr>       <tr>           <td>0102</td>           <td>特別気配</td>       </tr>       <tr>           <td>0103</td>           <td>注意気配</td>       </tr>       <tr>           <td>0107</td>           <td>寄前気配</td>       </tr>       <tr>           <td>0108</td>           <td>停止前特別気配</td>       </tr>       <tr>           <td>0109</td>           <td>引け後気配</td>       </tr>       <tr>           <td>0116</td>           <td>寄前気配約定成立ポイントなし</td>       </tr>       <tr>           <td>0117</td>           <td>寄前気配約定成立ポイントあり</td>       </tr>       <tr>           <td>0118</td>           <td>連続約定気配</td>       </tr>       <tr>           <td>0119</td>           <td>停止前の連続約定気配</td>       </tr>       <tr>           <td>0120</td>           <td>買い上がり売り下がり中</td>       </tr>   </tbody> </table>", alias="BidSign")
    market_order_sell_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="売成行数量<br>※株式銘柄の場合のみ", alias="MarketOrderSellQty")
    sell1: Optional[BoardSuccessSell1] = Field(default=None, alias="Sell1")
    sell2: Optional[BoardSuccessSell2] = Field(default=None, alias="Sell2")
    sell3: Optional[BoardSuccessSell3] = Field(default=None, alias="Sell3")
    sell4: Optional[BoardSuccessSell4] = Field(default=None, alias="Sell4")
    sell5: Optional[BoardSuccessSell5] = Field(default=None, alias="Sell5")
    sell6: Optional[BoardSuccessSell6] = Field(default=None, alias="Sell6")
    sell7: Optional[BoardSuccessSell7] = Field(default=None, alias="Sell7")
    sell8: Optional[BoardSuccessSell8] = Field(default=None, alias="Sell8")
    sell9: Optional[BoardSuccessSell9] = Field(default=None, alias="Sell9")
    sell10: Optional[BoardSuccessSell10] = Field(default=None, alias="Sell10")
    ask_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="最良買気配数量 ※①<br>※株式・先物・オプション銘柄の場合のみ", alias="AskQty")
    ask_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="最良買気配値段 ※①<br>※株式・先物・オプション銘柄の場合のみ", alias="AskPrice")
    ask_time: Optional[datetime] = Field(default=None, description="最良買気配時刻 ※①<br>※株式銘柄の場合のみ", alias="AskTime")
    ask_sign: Optional[StrictStr] = Field(default=None, description="最良買気配フラグ ※①<br>※株式・先物・オプション銘柄の場合のみ <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0000</td>           <td>事象なし</td>       </tr>       <tr>           <td>0101</td>           <td>一般気配</td>       </tr>       <tr>           <td>0102</td>           <td>特別気配</td>       </tr>       <tr>           <td>0103</td>           <td>注意気配</td>       </tr>       <tr>           <td>0107</td>           <td>寄前気配</td>       </tr>       <tr>           <td>0108</td>           <td>停止前特別気配</td>       </tr>       <tr>           <td>0109</td>           <td>引け後気配</td>       </tr>       <tr>           <td>0116</td>           <td>寄前気配約定成立ポイントなし</td>       </tr>       <tr>           <td>0117</td>           <td>寄前気配約定成立ポイントあり</td>       </tr>       <tr>           <td>0118</td>           <td>連続約定気配</td>       </tr>       <tr>           <td>0119</td>           <td>停止前の連続約定気配</td>       </tr>       <tr>           <td>0120</td>           <td>買い上がり売り下がり中</td>       </tr>   </tbody> </table>", alias="AskSign")
    market_order_buy_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="買成行数量<br>※株式銘柄の場合のみ", alias="MarketOrderBuyQty")
    buy1: Optional[BoardSuccessBuy1] = Field(default=None, alias="Buy1")
    buy2: Optional[BoardSuccessBuy2] = Field(default=None, alias="Buy2")
    buy3: Optional[BoardSuccessBuy3] = Field(default=None, alias="Buy3")
    buy4: Optional[BoardSuccessBuy4] = Field(default=None, alias="Buy4")
    buy5: Optional[BoardSuccessBuy5] = Field(default=None, alias="Buy5")
    buy6: Optional[BoardSuccessBuy6] = Field(default=None, alias="Buy6")
    buy7: Optional[BoardSuccessBuy7] = Field(default=None, alias="Buy7")
    buy8: Optional[BoardSuccessBuy8] = Field(default=None, alias="Buy8")
    buy9: Optional[BoardSuccessBuy9] = Field(default=None, alias="Buy9")
    buy10: Optional[BoardSuccessBuy10] = Field(default=None, alias="Buy10")
    over_sell_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="OVER気配数量<br>※株式銘柄の場合のみ", alias="OverSellQty")
    under_buy_qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="UNDER気配数量<br>※株式銘柄の場合のみ", alias="UnderBuyQty")
    total_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="時価総額<br>※株式銘柄の場合のみ", alias="TotalMarketValue")
    clearing_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="清算値<br>※先物銘柄の場合のみ", alias="ClearingPrice")
    iv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="インプライド・ボラティリティ<br>※オプション銘柄かつ日通しの場合のみ", alias="IV")
    gamma: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ガンマ<br>※オプション銘柄かつ日通しの場合のみ", alias="Gamma")
    theta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="セータ<br>※オプション銘柄かつ日通しの場合のみ", alias="Theta")
    vega: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ベガ<br>※オプション銘柄かつ日通しの場合のみ", alias="Vega")
    delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="デルタ<br>※オプション銘柄かつ日通しの場合のみ", alias="Delta")
    security_type: Optional[StrictInt] = Field(default=None, description="銘柄種別 <table>   <thead>     <tr>       <th>定義値</th>       <th>説明</th>     </tr>   </thead>   <tbody>     <tr>       <td>0</td>       <td>指数</td>     </tr>     <tr>       <td>1</td>       <td>現物</td>     </tr>     <tr>       <td>101</td>       <td>日経225先物</td>     </tr>     <tr>       <td>103</td>       <td>日経225OP</td>     </tr>     <tr>       <td>107</td>       <td>TOPIX先物</td>     </tr>     <tr>       <td>121</td>       <td>JPX400先物</td>     </tr>     <tr>       <td>144</td>       <td>NYダウ</td>     </tr>     <tr>       <td>145</td>       <td>日経平均VI</td>     </tr>     <tr>       <td>154</td>       <td>グロース250先物</td>     </tr>     <tr>       <td>155</td>       <td>TOPIX_REIT</td>     </tr>     <tr>       <td>171</td>       <td>TOPIX CORE30</td>     </tr>     <tr>       <td>901</td>       <td>日経平均225ミニ先物</td>     </tr>     <tr>       <td>907</td>       <td>TOPIXミニ先物</td>     </tr>   </tbody> </table>", alias="SecurityType")
    __properties: ClassVar[List[str]] = ["Symbol", "SymbolName", "Exchange", "ExchangeName", "CurrentPrice", "CurrentPriceTime", "CurrentPriceChangeStatus", "CurrentPriceStatus", "CalcPrice", "PreviousClose", "PreviousCloseTime", "ChangePreviousClose", "ChangePreviousClosePer", "OpeningPrice", "OpeningPriceTime", "HighPrice", "HighPriceTime", "LowPrice", "LowPriceTime", "TradingVolume", "TradingVolumeTime", "VWAP", "TradingValue", "BidQty", "BidPrice", "BidTime", "BidSign", "MarketOrderSellQty", "Sell1", "Sell2", "Sell3", "Sell4", "Sell5", "Sell6", "Sell7", "Sell8", "Sell9", "Sell10", "AskQty", "AskPrice", "AskTime", "AskSign", "MarketOrderBuyQty", "Buy1", "Buy2", "Buy3", "Buy4", "Buy5", "Buy6", "Buy7", "Buy8", "Buy9", "Buy10", "OverSellQty", "UnderBuyQty", "TotalMarketValue", "ClearingPrice", "IV", "Gamma", "Theta", "Vega", "Delta", "SecurityType"]

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
        """Create an instance of BoardSuccess from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sell1
        if self.sell1:
            _dict['Sell1'] = self.sell1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell2
        if self.sell2:
            _dict['Sell2'] = self.sell2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell3
        if self.sell3:
            _dict['Sell3'] = self.sell3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell4
        if self.sell4:
            _dict['Sell4'] = self.sell4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell5
        if self.sell5:
            _dict['Sell5'] = self.sell5.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell6
        if self.sell6:
            _dict['Sell6'] = self.sell6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell7
        if self.sell7:
            _dict['Sell7'] = self.sell7.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell8
        if self.sell8:
            _dict['Sell8'] = self.sell8.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell9
        if self.sell9:
            _dict['Sell9'] = self.sell9.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sell10
        if self.sell10:
            _dict['Sell10'] = self.sell10.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy1
        if self.buy1:
            _dict['Buy1'] = self.buy1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy2
        if self.buy2:
            _dict['Buy2'] = self.buy2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy3
        if self.buy3:
            _dict['Buy3'] = self.buy3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy4
        if self.buy4:
            _dict['Buy4'] = self.buy4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy5
        if self.buy5:
            _dict['Buy5'] = self.buy5.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy6
        if self.buy6:
            _dict['Buy6'] = self.buy6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy7
        if self.buy7:
            _dict['Buy7'] = self.buy7.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy8
        if self.buy8:
            _dict['Buy8'] = self.buy8.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy9
        if self.buy9:
            _dict['Buy9'] = self.buy9.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buy10
        if self.buy10:
            _dict['Buy10'] = self.buy10.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BoardSuccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Symbol": obj.get("Symbol"),
            "SymbolName": obj.get("SymbolName"),
            "Exchange": obj.get("Exchange"),
            "ExchangeName": obj.get("ExchangeName"),
            "CurrentPrice": obj.get("CurrentPrice"),
            "CurrentPriceTime": obj.get("CurrentPriceTime"),
            "CurrentPriceChangeStatus": obj.get("CurrentPriceChangeStatus"),
            "CurrentPriceStatus": obj.get("CurrentPriceStatus"),
            "CalcPrice": obj.get("CalcPrice"),
            "PreviousClose": obj.get("PreviousClose"),
            "PreviousCloseTime": obj.get("PreviousCloseTime"),
            "ChangePreviousClose": obj.get("ChangePreviousClose"),
            "ChangePreviousClosePer": obj.get("ChangePreviousClosePer"),
            "OpeningPrice": obj.get("OpeningPrice"),
            "OpeningPriceTime": obj.get("OpeningPriceTime"),
            "HighPrice": obj.get("HighPrice"),
            "HighPriceTime": obj.get("HighPriceTime"),
            "LowPrice": obj.get("LowPrice"),
            "LowPriceTime": obj.get("LowPriceTime"),
            "TradingVolume": obj.get("TradingVolume"),
            "TradingVolumeTime": obj.get("TradingVolumeTime"),
            "VWAP": obj.get("VWAP"),
            "TradingValue": obj.get("TradingValue"),
            "BidQty": obj.get("BidQty"),
            "BidPrice": obj.get("BidPrice"),
            "BidTime": obj.get("BidTime"),
            "BidSign": obj.get("BidSign"),
            "MarketOrderSellQty": obj.get("MarketOrderSellQty"),
            "Sell1": BoardSuccessSell1.from_dict(obj["Sell1"]) if obj.get("Sell1") is not None else None,
            "Sell2": BoardSuccessSell2.from_dict(obj["Sell2"]) if obj.get("Sell2") is not None else None,
            "Sell3": BoardSuccessSell3.from_dict(obj["Sell3"]) if obj.get("Sell3") is not None else None,
            "Sell4": BoardSuccessSell4.from_dict(obj["Sell4"]) if obj.get("Sell4") is not None else None,
            "Sell5": BoardSuccessSell5.from_dict(obj["Sell5"]) if obj.get("Sell5") is not None else None,
            "Sell6": BoardSuccessSell6.from_dict(obj["Sell6"]) if obj.get("Sell6") is not None else None,
            "Sell7": BoardSuccessSell7.from_dict(obj["Sell7"]) if obj.get("Sell7") is not None else None,
            "Sell8": BoardSuccessSell8.from_dict(obj["Sell8"]) if obj.get("Sell8") is not None else None,
            "Sell9": BoardSuccessSell9.from_dict(obj["Sell9"]) if obj.get("Sell9") is not None else None,
            "Sell10": BoardSuccessSell10.from_dict(obj["Sell10"]) if obj.get("Sell10") is not None else None,
            "AskQty": obj.get("AskQty"),
            "AskPrice": obj.get("AskPrice"),
            "AskTime": obj.get("AskTime"),
            "AskSign": obj.get("AskSign"),
            "MarketOrderBuyQty": obj.get("MarketOrderBuyQty"),
            "Buy1": BoardSuccessBuy1.from_dict(obj["Buy1"]) if obj.get("Buy1") is not None else None,
            "Buy2": BoardSuccessBuy2.from_dict(obj["Buy2"]) if obj.get("Buy2") is not None else None,
            "Buy3": BoardSuccessBuy3.from_dict(obj["Buy3"]) if obj.get("Buy3") is not None else None,
            "Buy4": BoardSuccessBuy4.from_dict(obj["Buy4"]) if obj.get("Buy4") is not None else None,
            "Buy5": BoardSuccessBuy5.from_dict(obj["Buy5"]) if obj.get("Buy5") is not None else None,
            "Buy6": BoardSuccessBuy6.from_dict(obj["Buy6"]) if obj.get("Buy6") is not None else None,
            "Buy7": BoardSuccessBuy7.from_dict(obj["Buy7"]) if obj.get("Buy7") is not None else None,
            "Buy8": BoardSuccessBuy8.from_dict(obj["Buy8"]) if obj.get("Buy8") is not None else None,
            "Buy9": BoardSuccessBuy9.from_dict(obj["Buy9"]) if obj.get("Buy9") is not None else None,
            "Buy10": BoardSuccessBuy10.from_dict(obj["Buy10"]) if obj.get("Buy10") is not None else None,
            "OverSellQty": obj.get("OverSellQty"),
            "UnderBuyQty": obj.get("UnderBuyQty"),
            "TotalMarketValue": obj.get("TotalMarketValue"),
            "ClearingPrice": obj.get("ClearingPrice"),
            "IV": obj.get("IV"),
            "Gamma": obj.get("Gamma"),
            "Theta": obj.get("Theta"),
            "Vega": obj.get("Vega"),
            "Delta": obj.get("Delta"),
            "SecurityType": obj.get("SecurityType")
        })
        return _obj

