# graylog.SystemshutdownApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shutdown**](SystemshutdownApi.md#shutdown) | **POST** /system/shutdown/shutdown | Shutdown this node gracefully.


# **shutdown**
> shutdown()

Shutdown this node gracefully.

Attempts to process all buffered and cached messages before exiting, shuts down inputs first to make sure that no new messages are accepted.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemshutdownApi()

try: 
    # Shutdown this node gracefully.
    api_instance.shutdown()
except ApiException as e:
    print "Exception when calling SystemshutdownApi->shutdown: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

