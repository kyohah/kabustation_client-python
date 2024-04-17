# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.orders_success_details_inner import OrdersSuccessDetailsInner

class TestOrdersSuccessDetailsInner(unittest.TestCase):
    """OrdersSuccessDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrdersSuccessDetailsInner:
        """Test OrdersSuccessDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrdersSuccessDetailsInner`
        """
        model = OrdersSuccessDetailsInner()
        if include_optional:
            return OrdersSuccessDetailsInner(
                seq_num = 56,
                id = '',
                rec_type = 1,
                exchange_id = '',
                state = 56,
                transact_time = '',
                ord_type = 56,
                price = 1.337,
                qty = 1.337,
                execution_id = '',
                execution_day = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deliv_day = 56,
                commission = 1.337,
                commission_tax = 1.337
            )
        else:
            return OrdersSuccessDetailsInner(
        )
        """

    def testOrdersSuccessDetailsInner(self):
        """Test OrdersSuccessDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
