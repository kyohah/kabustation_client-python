# kabustation_client.WalletApi

All URIs are relative to *http://localhost:18080/kabusapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_cash_get**](WalletApi.md#wallet_cash_get) | **GET** /wallet/cash | 取引余力（現物）
[**wallet_cash_symbol_get**](WalletApi.md#wallet_cash_symbol_get) | **GET** /wallet/cash/{symbol} | 取引余力（現物）（銘柄指定）
[**wallet_future_get**](WalletApi.md#wallet_future_get) | **GET** /wallet/future | 取引余力（先物）
[**wallet_future_symbol_get**](WalletApi.md#wallet_future_symbol_get) | **GET** /wallet/future/{symbol} | 取引余力（先物）（銘柄指定）
[**wallet_margin_get**](WalletApi.md#wallet_margin_get) | **GET** /wallet/margin | 取引余力（信用）
[**wallet_margin_symbol_get**](WalletApi.md#wallet_margin_symbol_get) | **GET** /wallet/margin/{symbol} | 取引余力（信用）（銘柄指定）
[**wallet_option_get**](WalletApi.md#wallet_option_get) | **GET** /wallet/option | 取引余力（オプション）
[**wallet_option_symbol_get**](WalletApi.md#wallet_option_symbol_get) | **GET** /wallet/option/{symbol} | 取引余力（オプション）（銘柄指定）


# **wallet_cash_get**
> WalletCashSuccess wallet_cash_get(x_api_key)

取引余力（現物）

口座の取引余力（現物）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_cash_success import WalletCashSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列

    try:
        # 取引余力（現物）
        api_response = api_instance.wallet_cash_get(x_api_key)
        print("The response of WalletApi->wallet_cash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_cash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 

### Return type

[**WalletCashSuccess**](WalletCashSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_cash_symbol_get**
> WalletCashSuccess wallet_cash_symbol_get(x_api_key, symbol)

取引余力（現物）（銘柄指定）

指定した銘柄の取引余力（現物）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_cash_success import WalletCashSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    symbol = 'symbol_example' # str | 銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>     <tr>       <th>定義値</th>       <th>説明</th>     </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>東証</td>     </tr>     <tr>       <td>3</td>       <td>名証</td>     </tr>     <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>   </tbody> </table>

    try:
        # 取引余力（現物）（銘柄指定）
        api_response = api_instance.wallet_cash_symbol_get(x_api_key, symbol)
        print("The response of WalletApi->wallet_cash_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_cash_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **symbol** | **str**| 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 

### Return type

[**WalletCashSuccess**](WalletCashSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_future_get**
> WalletFutureSuccess wallet_future_get(x_api_key)

取引余力（先物）

口座の取引余力（先物）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_future_success import WalletFutureSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列

    try:
        # 取引余力（先物）
        api_response = api_instance.wallet_future_get(x_api_key)
        print("The response of WalletApi->wallet_future_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_future_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 

### Return type

[**WalletFutureSuccess**](WalletFutureSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_future_symbol_get**
> WalletFutureSuccess wallet_future_symbol_get(x_api_key, symbol)

取引余力（先物）（銘柄指定）

指定した銘柄の取引余力（先物）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_future_success import WalletFutureSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    symbol = 'symbol_example' # str | 銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。     ※SOR市場は取扱っておりませんのでご注意ください。<b>市場コード</b><br> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table>

    try:
        # 取引余力（先物）（銘柄指定）
        api_response = api_instance.wallet_future_symbol_get(x_api_key, symbol)
        print("The response of WalletApi->wallet_future_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_future_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **symbol** | **str**| 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。     ※SOR市場は取扱っておりませんのでご注意ください。&lt;b&gt;市場コード&lt;/b&gt;&lt;br&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 

### Return type

[**WalletFutureSuccess**](WalletFutureSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_margin_get**
> WalletMarginSuccess wallet_margin_get(x_api_key)

取引余力（信用）

口座の取引余力（信用）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_margin_success import WalletMarginSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列

    try:
        # 取引余力（信用）
        api_response = api_instance.wallet_margin_get(x_api_key)
        print("The response of WalletApi->wallet_margin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_margin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 

### Return type

[**WalletMarginSuccess**](WalletMarginSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_margin_symbol_get**
> WalletMarginSuccess wallet_margin_symbol_get(x_api_key, symbol)

取引余力（信用）（銘柄指定）

指定した銘柄の取引余力（信用）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_margin_success import WalletMarginSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    symbol = 'symbol_example' # str | 銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>     <tr>       <th>定義値</th>       <th>説明</th>     </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>東証</td>     </tr>     <tr>       <td>3</td>       <td>名証</td>     </tr>   </tbody> </table>

    try:
        # 取引余力（信用）（銘柄指定）
        api_response = api_instance.wallet_margin_symbol_get(x_api_key, symbol)
        print("The response of WalletApi->wallet_margin_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_margin_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **symbol** | **str**| 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 

### Return type

[**WalletMarginSuccess**](WalletMarginSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_option_get**
> WalletOptionSuccess wallet_option_get(x_api_key)

取引余力（オプション）

口座の取引余力（オプション）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_option_success import WalletOptionSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列

    try:
        # 取引余力（オプション）
        api_response = api_instance.wallet_option_get(x_api_key)
        print("The response of WalletApi->wallet_option_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_option_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 

### Return type

[**WalletOptionSuccess**](WalletOptionSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_option_symbol_get**
> WalletOptionSuccess wallet_option_symbol_get(x_api_key, symbol)

取引余力（オプション）（銘柄指定）

指定した銘柄の取引余力（オプション）を取得します

### Example


```python
import kabustation_client
from kabustation_client.models.wallet_option_success import WalletOptionSuccess
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
    api_instance = kabustation_client.WalletApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    symbol = 'symbol_example' # str | 銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table>

    try:
        # 取引余力（オプション）（銘柄指定）
        api_response = api_instance.wallet_option_symbol_get(x_api_key, symbol)
        print("The response of WalletApi->wallet_option_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_option_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **symbol** | **str**| 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 

### Return type

[**WalletOptionSuccess**](WalletOptionSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**405** | MethodNotAllowed |  -  |
**413** | RequestEntityTooLarge |  -  |
**415** | UnsupportedMediaType |  -  |
**429** | TooManyRequests |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

