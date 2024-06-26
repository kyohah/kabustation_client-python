# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.ranking_by_trade_value_response import RankingByTradeValueResponse

class TestRankingByTradeValueResponse(unittest.TestCase):
    """RankingByTradeValueResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RankingByTradeValueResponse:
        """Test RankingByTradeValueResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RankingByTradeValueResponse`
        """
        model = RankingByTradeValueResponse()
        if include_optional:
            return RankingByTradeValueResponse(
                type = '',
                exchange_division = '',
                ranking = [
                    kabustation_client.models.ranking_by_trade_value_response_ranking_inner.RankingByTradeValueResponse_Ranking_inner(
                        false = 56, 
                        trend = '', 
                        average_ranking = 1.337, 
                        symbol = '', 
                        symbol_name = '', 
                        current_price = 1.337, 
                        change_ratio = 1.337, 
                        rapid_payment_percentage = 1.337, 
                        turnover = 1.337, 
                        current_price_time = '', 
                        change_percentage = 1.337, 
                        exchange_name = '', 
                        category_name = '', )
                    ]
            )
        else:
            return RankingByTradeValueResponse(
        )
        """

    def testRankingByTradeValueResponse(self):
        """Test RankingByTradeValueResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
