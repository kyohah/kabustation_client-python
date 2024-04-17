# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.margin_premium_response import MarginPremiumResponse

class TestMarginPremiumResponse(unittest.TestCase):
    """MarginPremiumResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginPremiumResponse:
        """Test MarginPremiumResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginPremiumResponse`
        """
        model = MarginPremiumResponse()
        if include_optional:
            return MarginPremiumResponse(
                symbol = '',
                general_margin = kabustation_client.models.margin_premium_response_general_margin.MarginPremiumResponse_GeneralMargin(
                    margin_premium_type = 56, 
                    margin_premium = 1.337, 
                    upper_margin_premium = 1.337, 
                    lower_margin_premium = 1.337, 
                    tick_margin_premium = 1.337, ),
                day_trade = kabustation_client.models.margin_premium_response_day_trade.MarginPremiumResponse_DayTrade(
                    margin_premium_type = 56, 
                    margin_premium = 1.337, 
                    upper_margin_premium = 1.337, 
                    lower_margin_premium = 1.337, 
                    tick_margin_premium = 1.337, )
            )
        else:
            return MarginPremiumResponse(
        )
        """

    def testMarginPremiumResponse(self):
        """Test MarginPremiumResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()