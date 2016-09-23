# graylog.SystemserviceManagerApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SystemserviceManagerApi.md#list) | **GET** /system/serviceManager | List current status of ServiceManager


# **list**
> Map list()

List current status of ServiceManager



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemserviceManagerApi()

try: 
    # List current status of ServiceManager
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemserviceManagerApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

