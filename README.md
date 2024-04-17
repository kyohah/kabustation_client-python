# kabustation-client
# 定義情報 
 REST APIのコード一覧、エンドポイントは下記リンク参照  
  - [REST APIコード一覧](../ptal/error.html)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.5
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://kabucom.github.io/kabusapi/ptal/index.html](https://kabucom.github.io/kabusapi/ptal/index.html)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/kyohah/kabustation_client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kabustation_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kabustation_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import kabustation_client
from kabustation_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18080/kabusapi
# See configuration.py for a list of all supported configuration parameters.
configuration = kabustation_client.Configuration(
    host = "http://localhost:18080/kabusapi"
)



# Enter a context with an instance of the API client
with kabustation_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kabustation_client.AuthApi(api_client)
    request_token = kabustation_client.RequestToken() # RequestToken | 

    try:
        # トークン発行
        api_response = api_instance.token_post(request_token)
        print("The response of AuthApi->token_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->token_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:18080/kabusapi*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**token_post**](docs/AuthApi.md#token_post) | **POST** /token | トークン発行
*InfoApi* | [**apisoftlimit_get**](docs/InfoApi.md#apisoftlimit_get) | **GET** /apisoftlimit | ソフトリミット
*InfoApi* | [**board_get**](docs/InfoApi.md#board_get) | **GET** /board/{symbol} | 時価情報・板情報
*InfoApi* | [**exchange_get**](docs/InfoApi.md#exchange_get) | **GET** /exchange/{symbol} | 為替情報
*InfoApi* | [**marginpremium_get**](docs/InfoApi.md#marginpremium_get) | **GET** /margin/marginpremium/{symbol} | プレミアム料取得
*InfoApi* | [**orders_get**](docs/InfoApi.md#orders_get) | **GET** /orders | 注文約定照会
*InfoApi* | [**positions_get**](docs/InfoApi.md#positions_get) | **GET** /positions | 残高照会
*InfoApi* | [**primary_exchange_get**](docs/InfoApi.md#primary_exchange_get) | **GET** /primaryexchange/{symbol} | 優先市場
*InfoApi* | [**ranking_get**](docs/InfoApi.md#ranking_get) | **GET** /ranking | 詳細ランキング
*InfoApi* | [**regulations_get**](docs/InfoApi.md#regulations_get) | **GET** /regulations/{symbol} | 規制情報
*InfoApi* | [**symbol_get**](docs/InfoApi.md#symbol_get) | **GET** /symbol/{symbol} | 銘柄情報
*InfoApi* | [**symbolname_future_get**](docs/InfoApi.md#symbolname_future_get) | **GET** /symbolname/future | 先物銘柄コード取得
*InfoApi* | [**symbolname_option_get**](docs/InfoApi.md#symbolname_option_get) | **GET** /symbolname/option | オプション銘柄コード取得
*InfoApi* | [**symbolname_option_mini_get**](docs/InfoApi.md#symbolname_option_mini_get) | **GET** /symbolname/minioptionweekly | ミニオプション（限週）銘柄コード取得
*OrderApi* | [**cancelorder_put**](docs/OrderApi.md#cancelorder_put) | **PUT** /cancelorder | 注文取消
*OrderApi* | [**sendoder_future_post**](docs/OrderApi.md#sendoder_future_post) | **POST** /sendorder/future | 注文発注（先物）
*OrderApi* | [**sendorder_option_post**](docs/OrderApi.md#sendorder_option_post) | **POST** /sendorder/option | 注文発注（オプション）
*OrderApi* | [**sendorder_post**](docs/OrderApi.md#sendorder_post) | **POST** /sendorder | 注文発注（現物・信用）
*RegisterApi* | [**register_put**](docs/RegisterApi.md#register_put) | **PUT** /register | 銘柄登録
*RegisterApi* | [**unregister_all_put**](docs/RegisterApi.md#unregister_all_put) | **PUT** /unregister/all | 銘柄登録全解除
*RegisterApi* | [**unregister_put**](docs/RegisterApi.md#unregister_put) | **PUT** /unregister | 銘柄登録解除
*WalletApi* | [**wallet_cash_get**](docs/WalletApi.md#wallet_cash_get) | **GET** /wallet/cash | 取引余力（現物）
*WalletApi* | [**wallet_cash_symbol_get**](docs/WalletApi.md#wallet_cash_symbol_get) | **GET** /wallet/cash/{symbol} | 取引余力（現物）（銘柄指定）
*WalletApi* | [**wallet_future_get**](docs/WalletApi.md#wallet_future_get) | **GET** /wallet/future | 取引余力（先物）
*WalletApi* | [**wallet_future_symbol_get**](docs/WalletApi.md#wallet_future_symbol_get) | **GET** /wallet/future/{symbol} | 取引余力（先物）（銘柄指定）
*WalletApi* | [**wallet_margin_get**](docs/WalletApi.md#wallet_margin_get) | **GET** /wallet/margin | 取引余力（信用）
*WalletApi* | [**wallet_margin_symbol_get**](docs/WalletApi.md#wallet_margin_symbol_get) | **GET** /wallet/margin/{symbol} | 取引余力（信用）（銘柄指定）
*WalletApi* | [**wallet_option_get**](docs/WalletApi.md#wallet_option_get) | **GET** /wallet/option | 取引余力（オプション）
*WalletApi* | [**wallet_option_symbol_get**](docs/WalletApi.md#wallet_option_symbol_get) | **GET** /wallet/option/{symbol} | 取引余力（オプション）（銘柄指定）


## Documentation For Models

 - [ApiSoftLimitResponse](docs/ApiSoftLimitResponse.md)
 - [BoardSuccess](docs/BoardSuccess.md)
 - [BoardSuccessBuy1](docs/BoardSuccessBuy1.md)
 - [BoardSuccessBuy10](docs/BoardSuccessBuy10.md)
 - [BoardSuccessBuy2](docs/BoardSuccessBuy2.md)
 - [BoardSuccessBuy3](docs/BoardSuccessBuy3.md)
 - [BoardSuccessBuy4](docs/BoardSuccessBuy4.md)
 - [BoardSuccessBuy5](docs/BoardSuccessBuy5.md)
 - [BoardSuccessBuy6](docs/BoardSuccessBuy6.md)
 - [BoardSuccessBuy7](docs/BoardSuccessBuy7.md)
 - [BoardSuccessBuy8](docs/BoardSuccessBuy8.md)
 - [BoardSuccessBuy9](docs/BoardSuccessBuy9.md)
 - [BoardSuccessSell1](docs/BoardSuccessSell1.md)
 - [BoardSuccessSell10](docs/BoardSuccessSell10.md)
 - [BoardSuccessSell2](docs/BoardSuccessSell2.md)
 - [BoardSuccessSell3](docs/BoardSuccessSell3.md)
 - [BoardSuccessSell4](docs/BoardSuccessSell4.md)
 - [BoardSuccessSell5](docs/BoardSuccessSell5.md)
 - [BoardSuccessSell6](docs/BoardSuccessSell6.md)
 - [BoardSuccessSell7](docs/BoardSuccessSell7.md)
 - [BoardSuccessSell8](docs/BoardSuccessSell8.md)
 - [BoardSuccessSell9](docs/BoardSuccessSell9.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExchangeResponse](docs/ExchangeResponse.md)
 - [MarginPremiumResponse](docs/MarginPremiumResponse.md)
 - [MarginPremiumResponseDayTrade](docs/MarginPremiumResponseDayTrade.md)
 - [MarginPremiumResponseGeneralMargin](docs/MarginPremiumResponseGeneralMargin.md)
 - [OrderSuccess](docs/OrderSuccess.md)
 - [OrdersSuccess](docs/OrdersSuccess.md)
 - [OrdersSuccessDetailsInner](docs/OrdersSuccessDetailsInner.md)
 - [Positions](docs/Positions.md)
 - [PositionsDeriv](docs/PositionsDeriv.md)
 - [PositionsSuccess](docs/PositionsSuccess.md)
 - [PrimaryExchangeResponse](docs/PrimaryExchangeResponse.md)
 - [RankingByCategoryResponse](docs/RankingByCategoryResponse.md)
 - [RankingByCategoryResponseRankingInner](docs/RankingByCategoryResponseRankingInner.md)
 - [RankingByMarginResponse](docs/RankingByMarginResponse.md)
 - [RankingByMarginResponseRankingInner](docs/RankingByMarginResponseRankingInner.md)
 - [RankingByTickCountResponse](docs/RankingByTickCountResponse.md)
 - [RankingByTickCountResponseRankingInner](docs/RankingByTickCountResponseRankingInner.md)
 - [RankingByTradeValueResponse](docs/RankingByTradeValueResponse.md)
 - [RankingByTradeValueResponseRankingInner](docs/RankingByTradeValueResponseRankingInner.md)
 - [RankingByTradeVolumeResponse](docs/RankingByTradeVolumeResponse.md)
 - [RankingByTradeVolumeResponseRankingInner](docs/RankingByTradeVolumeResponseRankingInner.md)
 - [RankingDefaultResponse](docs/RankingDefaultResponse.md)
 - [RankingDefaultResponseRankingInner](docs/RankingDefaultResponseRankingInner.md)
 - [RankingGet200Response](docs/RankingGet200Response.md)
 - [RegistSuccess](docs/RegistSuccess.md)
 - [RegulationsResponse](docs/RegulationsResponse.md)
 - [RegulationsResponseRegulationsInfoInner](docs/RegulationsResponseRegulationsInfoInner.md)
 - [RequestCancelOrder](docs/RequestCancelOrder.md)
 - [RequestRegister](docs/RequestRegister.md)
 - [RequestRegisterSymbolsInner](docs/RequestRegisterSymbolsInner.md)
 - [RequestSendOrder](docs/RequestSendOrder.md)
 - [RequestSendOrderDerivFuture](docs/RequestSendOrderDerivFuture.md)
 - [RequestSendOrderDerivFutureReverseLimitOrder](docs/RequestSendOrderDerivFutureReverseLimitOrder.md)
 - [RequestSendOrderDerivOption](docs/RequestSendOrderDerivOption.md)
 - [RequestSendOrderReverseLimitOrder](docs/RequestSendOrderReverseLimitOrder.md)
 - [RequestToken](docs/RequestToken.md)
 - [RequestUnregister](docs/RequestUnregister.md)
 - [SymbolNameSuccess](docs/SymbolNameSuccess.md)
 - [SymbolSuccess](docs/SymbolSuccess.md)
 - [TokenSuccess](docs/TokenSuccess.md)
 - [UnregisterAllSuccess](docs/UnregisterAllSuccess.md)
 - [WalletCashSuccess](docs/WalletCashSuccess.md)
 - [WalletFutureSuccess](docs/WalletFutureSuccess.md)
 - [WalletMarginSuccess](docs/WalletMarginSuccess.md)
 - [WalletOptionSuccess](docs/WalletOptionSuccess.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




