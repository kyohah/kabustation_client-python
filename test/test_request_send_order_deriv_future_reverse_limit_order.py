# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.request_send_order_deriv_future_reverse_limit_order import RequestSendOrderDerivFutureReverseLimitOrder

class TestRequestSendOrderDerivFutureReverseLimitOrder(unittest.TestCase):
    """RequestSendOrderDerivFutureReverseLimitOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestSendOrderDerivFutureReverseLimitOrder:
        """Test RequestSendOrderDerivFutureReverseLimitOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestSendOrderDerivFutureReverseLimitOrder`
        """
        model = RequestSendOrderDerivFutureReverseLimitOrder()
        if include_optional:
            return RequestSendOrderDerivFutureReverseLimitOrder(
                trigger_price = 1.337,
                under_over = 56,
                after_hit_order_type = 56,
                after_hit_price = 1.337
            )
        else:
            return RequestSendOrderDerivFutureReverseLimitOrder(
                trigger_price = 1.337,
                under_over = 56,
                after_hit_order_type = 56,
                after_hit_price = 1.337,
        )
        """

    def testRequestSendOrderDerivFutureReverseLimitOrder(self):
        """Test RequestSendOrderDerivFutureReverseLimitOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
