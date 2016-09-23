# graylog.SystemcodecstypesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all**](SystemcodecstypesApi.md#get_all) | **GET** /system/codecs/types/all | Get all codec types


# **get_all**
> Map get_all()

Get all codec types



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemcodecstypesApi()

try: 
    # Get all codec types
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemcodecstypesApi->get_all: %s\n" % e
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

