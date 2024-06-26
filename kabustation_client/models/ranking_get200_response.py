# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from kabustation_client.models.ranking_by_category_response import RankingByCategoryResponse
from kabustation_client.models.ranking_by_margin_response import RankingByMarginResponse
from kabustation_client.models.ranking_by_tick_count_response import RankingByTickCountResponse
from kabustation_client.models.ranking_by_trade_value_response import RankingByTradeValueResponse
from kabustation_client.models.ranking_by_trade_volume_response import RankingByTradeVolumeResponse
from kabustation_client.models.ranking_default_response import RankingDefaultResponse
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

RANKINGGET200RESPONSE_ONE_OF_SCHEMAS = ["RankingByCategoryResponse", "RankingByMarginResponse", "RankingByTickCountResponse", "RankingByTradeValueResponse", "RankingByTradeVolumeResponse", "RankingDefaultResponse"]

class RankingGet200Response(BaseModel):
    """
    RankingGet200Response
    """
    # data type: RankingDefaultResponse
    oneof_schema_1_validator: Optional[RankingDefaultResponse] = None
    # data type: RankingByTickCountResponse
    oneof_schema_2_validator: Optional[RankingByTickCountResponse] = None
    # data type: RankingByTradeVolumeResponse
    oneof_schema_3_validator: Optional[RankingByTradeVolumeResponse] = None
    # data type: RankingByTradeValueResponse
    oneof_schema_4_validator: Optional[RankingByTradeValueResponse] = None
    # data type: RankingByMarginResponse
    oneof_schema_5_validator: Optional[RankingByMarginResponse] = None
    # data type: RankingByCategoryResponse
    oneof_schema_6_validator: Optional[RankingByCategoryResponse] = None
    actual_instance: Optional[Union[RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse]] = None
    one_of_schemas: List[str] = Field(default=Literal["RankingByCategoryResponse", "RankingByMarginResponse", "RankingByTickCountResponse", "RankingByTradeValueResponse", "RankingByTradeVolumeResponse", "RankingDefaultResponse"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = RankingGet200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: RankingDefaultResponse
        if not isinstance(v, RankingDefaultResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingDefaultResponse`")
        else:
            match += 1
        # validate data type: RankingByTickCountResponse
        if not isinstance(v, RankingByTickCountResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingByTickCountResponse`")
        else:
            match += 1
        # validate data type: RankingByTradeVolumeResponse
        if not isinstance(v, RankingByTradeVolumeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingByTradeVolumeResponse`")
        else:
            match += 1
        # validate data type: RankingByTradeValueResponse
        if not isinstance(v, RankingByTradeValueResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingByTradeValueResponse`")
        else:
            match += 1
        # validate data type: RankingByMarginResponse
        if not isinstance(v, RankingByMarginResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingByMarginResponse`")
        else:
            match += 1
        # validate data type: RankingByCategoryResponse
        if not isinstance(v, RankingByCategoryResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingByCategoryResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RankingGet200Response with oneOf schemas: RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RankingGet200Response with oneOf schemas: RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into RankingDefaultResponse
        try:
            instance.actual_instance = RankingDefaultResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingByTickCountResponse
        try:
            instance.actual_instance = RankingByTickCountResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingByTradeVolumeResponse
        try:
            instance.actual_instance = RankingByTradeVolumeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingByTradeValueResponse
        try:
            instance.actual_instance = RankingByTradeValueResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingByMarginResponse
        try:
            instance.actual_instance = RankingByMarginResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingByCategoryResponse
        try:
            instance.actual_instance = RankingByCategoryResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RankingGet200Response with oneOf schemas: RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RankingGet200Response with oneOf schemas: RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], RankingByCategoryResponse, RankingByMarginResponse, RankingByTickCountResponse, RankingByTradeValueResponse, RankingByTradeVolumeResponse, RankingDefaultResponse]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


