# graylog.SystemconfigurationApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_relevant**](SystemconfigurationApi.md#get_relevant) | **GET** /system/configuration | Get relevant configuration settings and their values


# **get_relevant**
> ExposedConfiguration get_relevant()

Get relevant configuration settings and their values



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemconfigurationApi()

try: 
    # Get relevant configuration settings and their values
    api_response = api_instance.get_relevant()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemconfigurationApi->get_relevant: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExposedConfiguration**](ExposedConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

