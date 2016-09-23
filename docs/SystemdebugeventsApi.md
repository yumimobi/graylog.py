# graylog.SystemdebugeventsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cluster_debug_event**](SystemdebugeventsApi.md#generate_cluster_debug_event) | **POST** /system/debug/events/cluster | Create and send a cluster debug event.
[**generate_debug_event**](SystemdebugeventsApi.md#generate_debug_event) | **POST** /system/debug/events/local | Create and send a local debug event.
[**show_last_cluster_debug_event**](SystemdebugeventsApi.md#show_last_cluster_debug_event) | **GET** /system/debug/events/cluster | Show last received cluster debug event.
[**show_last_debug_event**](SystemdebugeventsApi.md#show_last_debug_event) | **GET** /system/debug/events/local | Show last received local debug event.


# **generate_cluster_debug_event**
> generate_cluster_debug_event(text=text)

Create and send a cluster debug event.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdebugeventsApi()
text = 'text_example' # String |  (optional)

try: 
    # Create and send a cluster debug event.
    api_instance.generate_cluster_debug_event(text=text)
except ApiException as e:
    print "Exception when calling SystemdebugeventsApi->generate_cluster_debug_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**String**](String.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_debug_event**
> generate_debug_event(text=text)

Create and send a local debug event.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdebugeventsApi()
text = 'text_example' # String |  (optional)

try: 
    # Create and send a local debug event.
    api_instance.generate_debug_event(text=text)
except ApiException as e:
    print "Exception when calling SystemdebugeventsApi->generate_debug_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**String**](String.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_last_cluster_debug_event**
> DebugEvent show_last_cluster_debug_event()

Show last received cluster debug event.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdebugeventsApi()

try: 
    # Show last received cluster debug event.
    api_response = api_instance.show_last_cluster_debug_event()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemdebugeventsApi->show_last_cluster_debug_event: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DebugEvent**](DebugEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_last_debug_event**
> DebugEvent show_last_debug_event()

Show last received local debug event.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemdebugeventsApi()

try: 
    # Show last received local debug event.
    api_response = api_instance.show_last_debug_event()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemdebugeventsApi->show_last_debug_event: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DebugEvent**](DebugEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

