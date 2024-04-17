# kabustation_client.AuthApi

All URIs are relative to *http://localhost:18080/kabusapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_post**](AuthApi.md#token_post) | **POST** /token | トークン発行


# **token_post**
> TokenSuccess token_post(request_token)

トークン発行

APIトークンを発行します。<br> 発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br> 発行されたAPIトークンは以下のタイミングで無効となります。<br> ・kabuステーションを終了した時<br> ・kabuステーションからログアウトした時<br> ・別のトークンが新たに発行された時<br> ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

### Example


```python
import kabustation_client
from kabustation_client.models.request_token import RequestToken
from kabustation_client.models.token_success import TokenSuccess
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
    except Exception as e:
        print("Exception when calling AuthApi->token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_token** | [**RequestToken**](RequestToken.md)|  | 

### Return type

[**TokenSuccess**](TokenSuccess.md)

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

