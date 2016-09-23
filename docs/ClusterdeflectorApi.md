# graylog.ClusterdeflectorApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cycle**](ClusterdeflectorApi.md#cycle) | **POST** /cluster/deflector/cycle | Finds master node and triggers deflector cycle


# **cycle**
> cycle()

Finds master node and triggers deflector cycle



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterdeflectorApi()

try: 
    # Finds master node and triggers deflector cycle
    api_instance.cycle()
except ApiException as e:
    print "Exception when calling ClusterdeflectorApi->cycle: %s\n" % e
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

