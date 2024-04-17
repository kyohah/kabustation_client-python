# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.board_success_sell2 import BoardSuccessSell2

class TestBoardSuccessSell2(unittest.TestCase):
    """BoardSuccessSell2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoardSuccessSell2:
        """Test BoardSuccessSell2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoardSuccessSell2`
        """
        model = BoardSuccessSell2()
        if include_optional:
            return BoardSuccessSell2(
                price = 1.337,
                qty = 1.337
            )
        else:
            return BoardSuccessSell2(
        )
        """

    def testBoardSuccessSell2(self):
        """Test BoardSuccessSell2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()