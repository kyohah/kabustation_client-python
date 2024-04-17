# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.board_success_buy4 import BoardSuccessBuy4

class TestBoardSuccessBuy4(unittest.TestCase):
    """BoardSuccessBuy4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoardSuccessBuy4:
        """Test BoardSuccessBuy4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoardSuccessBuy4`
        """
        model = BoardSuccessBuy4()
        if include_optional:
            return BoardSuccessBuy4(
                price = 1.337,
                qty = 1.337
            )
        else:
            return BoardSuccessBuy4(
        )
        """

    def testBoardSuccessBuy4(self):
        """Test BoardSuccessBuy4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
