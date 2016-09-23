# graylog.SystemdeflectorApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cycle**](SystemdeflectorApi.md#cycle) | **POST** /system/deflector/cycle | Cycle deflector to new/next index
[**deflector**](SystemdeflectorApi.md#deflector) | **GET** /system/deflector | Get current deflector status


# **cycle**
> cycle()

Cycle deflector to new/next index



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdeflectorApi()

try: 
    # Cycle deflector to new/next index
    api_instance.cycle()
except ApiException as e:
    print "Exception when calling SystemdeflectorApi->cycle: %s\n" % e
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

# **deflector**
> DeflectorSummary deflector()

Get current deflector status



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdeflectorApi()

try: 
    # Get current deflector status
    api_response = api_instance.deflector()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemdeflectorApi->deflector: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeflectorSummary**](DeflectorSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

