# graylog.SystemauthenticationApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SystemauthenticationApi.md#create) | **PUT** /system/authentication/config | Update authentication providers configuration
[**get_authenticators**](SystemauthenticationApi.md#get_authenticators) | **GET** /system/authentication/config | Retrieve authentication providers configuration


# **create**
> AuthenticationConfig create(config)

Update authentication providers configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemauthenticationApi()
config = graylog.AuthenticationConfig() # AuthenticationConfig | 

try: 
    # Update authentication providers configuration
    api_response = api_instance.create(config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemauthenticationApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**AuthenticationConfig**](AuthenticationConfig.md)|  | 

### Return type

[**AuthenticationConfig**](AuthenticationConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticators**
> AuthenticationConfig get_authenticators()

Retrieve authentication providers configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemauthenticationApi()

try: 
    # Retrieve authentication providers configuration
    api_response = api_instance.get_authenticators()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemauthenticationApi->get_authenticators: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationConfig**](AuthenticationConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

