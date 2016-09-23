# graylog.SystemApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jvm**](SystemApi.md#jvm) | **GET** /system/jvm | Get JVM information
[**system**](SystemApi.md#system) | **GET** /system | Get system overview
[**threaddump**](SystemApi.md#threaddump) | **GET** /system/threaddump | Get a thread dump


# **jvm**
> SystemJVMResponse jvm()

Get JVM information



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemApi()

try: 
    # Get JVM information
    api_response = api_instance.jvm()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemApi->jvm: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemJVMResponse**](SystemJVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system**
> SystemOverviewResponse system()

Get system overview



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemApi()

try: 
    # Get system overview
    api_response = api_instance.system()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemApi->system: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemOverviewResponse**](SystemOverviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **threaddump**
> SystemThreadDumpResponse threaddump()

Get a thread dump



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemApi()

try: 
    # Get a thread dump
    api_response = api_instance.threaddump()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemApi->threaddump: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemThreadDumpResponse**](SystemThreadDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

