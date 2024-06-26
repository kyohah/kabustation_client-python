# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)

    The version of the OpenAPI document: 1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kabustation_client.models.regulations_response import RegulationsResponse

class TestRegulationsResponse(unittest.TestCase):
    """RegulationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegulationsResponse:
        """Test RegulationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegulationsResponse`
        """
        model = RegulationsResponse()
        if include_optional:
            return RegulationsResponse(
                symbol = '',
                regulations_info = [
                    kabustation_client.models.regulations_response_regulations_info_inner.RegulationsResponse_RegulationsInfo_inner(
                        exchange = 56, 
                        product = 56, 
                        side = '', 
                        reason = '', 
                        limit_start_day = '', 
                        limit_end_day = '', 
                        level = 56, )
                    ]
            )
        else:
            return RegulationsResponse(
        )
        """

    def testRegulationsResponse(self):
        """Test RegulationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
