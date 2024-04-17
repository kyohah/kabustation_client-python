# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.board_success_sell5 import BoardSuccessSell5

class TestBoardSuccessSell5(unittest.TestCase):
    """BoardSuccessSell5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoardSuccessSell5:
        """Test BoardSuccessSell5
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoardSuccessSell5`
        """
        model = BoardSuccessSell5()
        if include_optional:
            return BoardSuccessSell5(
                price = 1.337,
                qty = 1.337
            )
        else:
            return BoardSuccessSell5(
        )
        """

    def testBoardSuccessSell5(self):
        """Test BoardSuccessSell5"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
