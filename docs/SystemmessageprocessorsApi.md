# graylog.SystemmessageprocessorsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](SystemmessageprocessorsApi.md#config) | **GET** /system/messageprocessors/config | Get message processor configuration
[**update_config**](SystemmessageprocessorsApi.md#update_config) | **PUT** /system/messageprocessors/config | Update message processor configuration


# **config**
> MessageProcessorsConfigWithDescriptors config()

Get message processor configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmessageprocessorsApi()

try: 
    # Get message processor configuration
    api_response = api_instance.config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmessageprocessorsApi->config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MessageProcessorsConfigWithDescriptors**](MessageProcessorsConfigWithDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config**
> MessageProcessorsConfigWithDescriptors update_config(config)

Update message processor configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmessageprocessorsApi()
config = graylog.MessageProcessorsConfigWithDescriptors() # MessageProcessorsConfigWithDescriptors | 

try: 
    # Update message processor configuration
    api_response = api_instance.update_config(config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmessageprocessorsApi->update_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**MessageProcessorsConfigWithDescriptors**](MessageProcessorsConfigWithDescriptors.md)|  | 

### Return type

[**MessageProcessorsConfigWithDescriptors**](MessageProcessorsConfigWithDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

