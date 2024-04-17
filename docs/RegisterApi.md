# kabustation_client.RegisterApi

All URIs are relative to *http://localhost:18080/kabusapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_put**](RegisterApi.md#register_put) | **PUT** /register | 銘柄登録
[**unregister_all_put**](RegisterApi.md#unregister_all_put) | **PUT** /unregister/all | 銘柄登録全解除
[**unregister_put**](RegisterApi.md#unregister_put) | **PUT** /unregister | 銘柄登録解除


# **register_put**
> RegistSuccess register_put(x_api_key, request_register)

銘柄登録

PUSH配信する銘柄を登録します。<br> API登録銘柄リストを開くには、kabuステーションAPIインジケーターを右クリックし「API登録銘柄リスト」を選択してください。

### Example


```python
import kabustation_client
from kabustation_client.models.regist_success import RegistSuccess
from kabustation_client.models.request_register import RequestRegister
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
    api_instance = kabustation_client.RegisterApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_register = kabustation_client.RequestRegister() # RequestRegister | 登録する銘柄のリスト

    try:
        # 銘柄登録
        api_response = api_instance.register_put(x_api_key, request_register)
        print("The response of RegisterApi->register_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegisterApi->register_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_register** | [**RequestRegister**](RequestRegister.md)| 登録する銘柄のリスト | 

### Return type

[**RegistSuccess**](RegistSuccess.md)

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

# **unregister_all_put**
> UnregisterAllSuccess unregister_all_put(x_api_key)

銘柄登録全解除

API登録銘柄リストに登録されている銘柄をすべて解除します

### Example


```python
import kabustation_client
from kabustation_client.models.unregister_all_success import UnregisterAllSuccess
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
    api_instance = kabustation_client.RegisterApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列

    try:
        # 銘柄登録全解除
        api_response = api_instance.unregister_all_put(x_api_key)
        print("The response of RegisterApi->unregister_all_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegisterApi->unregister_all_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 

### Return type

[**UnregisterAllSuccess**](UnregisterAllSuccess.md)

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

# **unregister_put**
> RegistSuccess unregister_put(x_api_key, request_unregister)

銘柄登録解除

API登録銘柄リストに登録されている銘柄を解除します

### Example


```python
import kabustation_client
from kabustation_client.models.regist_success import RegistSuccess
from kabustation_client.models.request_unregister import RequestUnregister
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
    api_instance = kabustation_client.RegisterApi(api_client)
    x_api_key = 'x_api_key_example' # str | トークン発行メソッドで取得した文字列
    request_unregister = kabustation_client.RequestUnregister() # RequestUnregister | 登録解除する銘柄のリスト

    try:
        # 銘柄登録解除
        api_response = api_instance.unregister_put(x_api_key, request_unregister)
        print("The response of RegisterApi->unregister_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegisterApi->unregister_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| トークン発行メソッドで取得した文字列 | 
 **request_unregister** | [**RequestUnregister**](RequestUnregister.md)| 登録解除する銘柄のリスト | 

### Return type

[**RegistSuccess**](RegistSuccess.md)

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

