# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.api.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthApi()

    def tearDown(self) -> None:
        pass

    def test_token_post(self) -> None:
        """Test case for token_post

        トークン発行
        """
        pass


if __name__ == '__main__':
    unittest.main()
