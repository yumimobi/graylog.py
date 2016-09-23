# graylog.CountApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**total**](CountApi.md#total) | **GET** /count/total | Total number of messages in all your indices.


# **total**
> MessageCountResponse total()

Total number of messages in all your indices.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.CountApi()

try: 
    # Total number of messages in all your indices.
    api_response = api_instance.total()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CountApi->total: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MessageCountResponse**](MessageCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

