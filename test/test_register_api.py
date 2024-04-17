# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.api.register_api import RegisterApi


class TestRegisterApi(unittest.TestCase):
    """RegisterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RegisterApi()

    def tearDown(self) -> None:
        pass

    def test_register_put(self) -> None:
        """Test case for register_put

        銘柄登録
        """
        pass

    def test_unregister_all_put(self) -> None:
        """Test case for unregister_all_put

        銘柄登録全解除
        """
        pass

    def test_unregister_put(self) -> None:
        """Test case for unregister_put

        銘柄登録解除
        """
        pass


if __name__ == '__main__':
    unittest.main()