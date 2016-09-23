# graylog.ApidocsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**overview**](ApidocsApi.md#overview) | **GET** /api-docs | Get API documentation
[**route**](ApidocsApi.md#route) | **GET** /api-docs/{route: .+} | Get detailed API documentation of a single resource


# **overview**
> overview()

Get API documentation



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ApidocsApi()

try: 
    # Get API documentation
    api_instance.overview()
except ApiException as e:
    print "Exception when calling ApidocsApi->overview: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route**
> route(route)

Get detailed API documentation of a single resource



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ApidocsApi()
route = graylog.Object() # Object | Route to fetch. For example /system

try: 
    # Get detailed API documentation of a single resource
    api_instance.route(route)
except ApiException as e:
    print "Exception when calling ApidocsApi->route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**Object**](.md)| Route to fetch. For example /system | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

