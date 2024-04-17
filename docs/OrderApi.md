# kabustation_client.OrderApi

All URIs are relative to *http://localhost:18080/kabusapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelorder_put**](OrderApi.md#cancelorder_put) | **PUT** /cancelorder | 注文取消
[**sendoder_future_post**](OrderApi.md#sendoder_future_post) | **POST** /sendorder/future | 注文発注（先物）
[**sendorder_option_post**](OrderApi.md#sendorder_option_post) | **POST** /sendorder/option | 注文発注（オプション）
[**sendorder_post**](OrderApi.md#sendorder_post) | **POST** /sendorder | 注文発注（現物・信用）


# **cancelorder_put**
> OrderSuccess cancelorder_put(x_api_key, request_cancel_order)

注文取消

注文を取消します

### Example


```python
import kabustation_client
from kabustation_client.models.order_success import OrderSuccess
from kabustation_client.models.request_cancel_order import RequestCancelOrder
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
    api_instance = kabustation_client.OrderApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_cancel_order = kabustation_client.RequestCancelOrder() # RequestCancelOrder | 

    try:
        # 注文取消
        api_response = api_instance.cancelorder_put(x_api_key, request_cancel_order)
        print("The response of OrderApi->cancelorder_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->cancelorder_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_cancel_order** | [**RequestCancelOrder**](RequestCancelOrder.md)|  | 

### Return type

[**OrderSuccess**](OrderSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **sendoder_future_post**
> OrderSuccess sendoder_future_post(x_api_key, request_send_order_deriv_future)

注文発注（先物）

先物銘柄の注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example


```python
import kabustation_client
from kabustation_client.models.order_success import OrderSuccess
from kabustation_client.models.request_send_order_deriv_future import RequestSendOrderDerivFuture
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
    api_instance = kabustation_client.OrderApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_send_order_deriv_future = kabustation_client.RequestSendOrderDerivFuture() # RequestSendOrderDerivFuture | 

    try:
        # 注文発注（先物）
        api_response = api_instance.sendoder_future_post(x_api_key, request_send_order_deriv_future)
        print("The response of OrderApi->sendoder_future_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->sendoder_future_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_send_order_deriv_future** | [**RequestSendOrderDerivFuture**](RequestSendOrderDerivFuture.md)|  | 

### Return type

[**OrderSuccess**](OrderSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **sendorder_option_post**
> OrderSuccess sendorder_option_post(x_api_key, request_send_order_deriv_option)

注文発注（オプション）

オプション銘柄の注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example


```python
import kabustation_client
from kabustation_client.models.order_success import OrderSuccess
from kabustation_client.models.request_send_order_deriv_option import RequestSendOrderDerivOption
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
    api_instance = kabustation_client.OrderApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_send_order_deriv_option = kabustation_client.RequestSendOrderDerivOption() # RequestSendOrderDerivOption | 

    try:
        # 注文発注（オプション）
        api_response = api_instance.sendorder_option_post(x_api_key, request_send_order_deriv_option)
        print("The response of OrderApi->sendorder_option_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->sendorder_option_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_send_order_deriv_option** | [**RequestSendOrderDerivOption**](RequestSendOrderDerivOption.md)|  | 

### Return type

[**OrderSuccess**](OrderSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **sendorder_post**
> OrderSuccess sendorder_post(x_api_key, request_send_order)

注文発注（現物・信用）

注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example


```python
import kabustation_client
from kabustation_client.models.order_success import OrderSuccess
from kabustation_client.models.request_send_order import RequestSendOrder
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
    api_instance = kabustation_client.OrderApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_send_order = kabustation_client.RequestSendOrder() # RequestSendOrder | 

    try:
        # 注文発注（現物・信用）
        api_response = api_instance.sendorder_post(x_api_key, request_send_order)
        print("The response of OrderApi->sendorder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->sendorder_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_send_order** | [**RequestSendOrder**](RequestSendOrder.md)|  | 

### Return type

[**OrderSuccess**](OrderSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

