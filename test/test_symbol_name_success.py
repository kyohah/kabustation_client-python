# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.symbol_name_success import SymbolNameSuccess

class TestSymbolNameSuccess(unittest.TestCase):
    """SymbolNameSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SymbolNameSuccess:
        """Test SymbolNameSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SymbolNameSuccess`
        """
        model = SymbolNameSuccess()
        if include_optional:
            return SymbolNameSuccess(
                symbol = '136091318',
                symbol_name = '日経平均オプション 21/09 プット 31375'
            )
        else:
            return SymbolNameSuccess(
        )
        """

    def testSymbolNameSuccess(self):
        """Test SymbolNameSuccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
