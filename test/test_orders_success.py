# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.orders_success import OrdersSuccess

class TestOrdersSuccess(unittest.TestCase):
    """OrdersSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrdersSuccess:
        """Test OrdersSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrdersSuccess`
        """
        model = OrdersSuccess()
        if include_optional:
            return OrdersSuccess(
                id = '',
                state = 56,
                order_state = 56,
                ord_type = 56,
                recv_time = '',
                symbol = '',
                symbol_name = '',
                exchange = 56,
                exchange_name = '',
                time_in_force = 56,
                price = 1.337,
                order_qty = 1.337,
                cum_qty = 1.337,
                side = '',
                cash_margin = 56,
                account_type = 56,
                deliv_type = 56,
                expire_day = 56,
                margin_trade_type = 56,
                margin_premium = 1.337,
                details = [
                    kabustation_client.models.orders_success_details_inner.OrdersSuccess_Details_inner(
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
                        commission_tax = 1.337, )
                    ]
            )
        else:
            return OrdersSuccess(
        )
        """

    def testOrdersSuccess(self):
        """Test OrdersSuccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
