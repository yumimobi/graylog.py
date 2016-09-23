# graylog.ClusterApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ClusterApi.md#get) | **GET** /cluster | Get system overview of all Graylog nodes
[**jvm**](ClusterApi.md#jvm) | **GET** /cluster/{nodeId}/jvm | Get JVM information of the given node
[**thread_dump**](ClusterApi.md#thread_dump) | **GET** /cluster/{nodeId}/threaddump | Get a thread dump of the given node


# **get**
> Map get()

Get system overview of all Graylog nodes



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterApi()

try: 
    # Get system overview of all Graylog nodes
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get: %s\n" % e
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

# **jvm**
> SystemJVMResponse jvm(node_id)

Get JVM information of the given node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterApi()
node_id = graylog.Object() # Object | The id of the node where processing will be paused.

try: 
    # Get JVM information of the given node
    api_response = api_instance.jvm(node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->jvm: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**Object**](.md)| The id of the node where processing will be paused. | 

### Return type

[**SystemJVMResponse**](SystemJVMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thread_dump**
> SystemThreadDumpResponse thread_dump(node_id)

Get a thread dump of the given node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterApi()
node_id = graylog.Object() # Object | The id of the node where processing will be paused.

try: 
    # Get a thread dump of the given node
    api_response = api_instance.thread_dump(node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->thread_dump: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**Object**](.md)| The id of the node where processing will be paused. | 

### Return type

[**SystemThreadDumpResponse**](SystemThreadDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

