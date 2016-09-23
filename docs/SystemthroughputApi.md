# graylog.SystemthroughputApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**total**](SystemthroughputApi.md#total) | **GET** /system/throughput | Current throughput of this node in messages per second


# **total**
> Throughput total()

Current throughput of this node in messages per second



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemthroughputApi()

try: 
    # Current throughput of this node in messages per second
    api_response = api_instance.total()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemthroughputApi->total: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Throughput**](Throughput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

