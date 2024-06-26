# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.wallet_option_success import WalletOptionSuccess

class TestWalletOptionSuccess(unittest.TestCase):
    """WalletOptionSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletOptionSuccess:
        """Test WalletOptionSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletOptionSuccess`
        """
        model = WalletOptionSuccess()
        if include_optional:
            return WalletOptionSuccess(
                option_buy_trade_limit = 1.337,
                option_sell_trade_limit = 1.337,
                margin_requirement = 1.337
            )
        else:
            return WalletOptionSuccess(
        )
        """

    def testWalletOptionSuccess(self):
        """Test WalletOptionSuccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
