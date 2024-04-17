# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.positions_deriv import PositionsDeriv

class TestPositionsDeriv(unittest.TestCase):
    """PositionsDeriv unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PositionsDeriv:
        """Test PositionsDeriv
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PositionsDeriv`
        """
        model = PositionsDeriv()
        if include_optional:
            return PositionsDeriv(
                hold_id = '',
                qty = 56
            )
        else:
            return PositionsDeriv(
        )
        """

    def testPositionsDeriv(self):
        """Test PositionsDeriv"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
