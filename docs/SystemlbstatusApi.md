# graylog.SystemlbstatusApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**override**](SystemlbstatusApi.md#override) | **PUT** /system/lbstatus/override/{status} | Override load balancer status of this Graylog server node. Next lifecycle change will override it again to its default. Set to ALIVE, DEAD, or THROTTLED.
[**status**](SystemlbstatusApi.md#status) | **GET** /system/lbstatus | Get status of this Graylog server node for load balancers. Returns ALIVE with HTTP 200, DEAD with HTTP 503, or THROTTLED with HTTP 429.


# **override**
> override(status)

Override load balancer status of this Graylog server node. Next lifecycle change will override it again to its default. Set to ALIVE, DEAD, or THROTTLED.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemlbstatusApi()
status = graylog.Object() # Object | 

try: 
    # Override load balancer status of this Graylog server node. Next lifecycle change will override it again to its default. Set to ALIVE, DEAD, or THROTTLED.
    api_instance.override(status)
except ApiException as e:
    print "Exception when calling SystemlbstatusApi->override: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> status()

Get status of this Graylog server node for load balancers. Returns ALIVE with HTTP 200, DEAD with HTTP 503, or THROTTLED with HTTP 429.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemlbstatusApi()

try: 
    # Get status of this Graylog server node for load balancers. Returns ALIVE with HTTP 200, DEAD with HTTP 503, or THROTTLED with HTTP 429.
    api_instance.status()
except ApiException as e:
    print "Exception when calling SystemlbstatusApi->status: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

