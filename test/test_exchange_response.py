# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.exchange_response import ExchangeResponse

class TestExchangeResponse(unittest.TestCase):
    """ExchangeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeResponse:
        """Test ExchangeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeResponse`
        """
        model = ExchangeResponse()
        if include_optional:
            return ExchangeResponse(
                symbol = '',
                bid_price = 1.337,
                spread = 1.337,
                ask_price = 1.337,
                change = 1.337,
                time = ''
            )
        else:
            return ExchangeResponse(
        )
        """

    def testExchangeResponse(self):
        """Test ExchangeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()