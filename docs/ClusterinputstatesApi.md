# graylog.ClusterinputstatesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ClusterinputstatesApi.md#get) | **GET** /cluster/inputstates | Get all input states
[**start**](ClusterinputstatesApi.md#start) | **PUT** /cluster/inputstates/{inputId} | Start or restart specified input in all nodes
[**stop**](ClusterinputstatesApi.md#stop) | **DELETE** /cluster/inputstates/{inputId} | Stop specified input in all nodes


# **get**
> Map get()

Get all input states



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterinputstatesApi()

try: 
    # Get all input states
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterinputstatesApi->get: %s\n" % e
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

# **start**
> Map start(input_id)

Start or restart specified input in all nodes



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterinputstatesApi()
input_id = graylog.Object() # Object | 

try: 
    # Start or restart specified input in all nodes
    api_response = api_instance.start(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterinputstatesApi->start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> Map stop(input_id)

Stop specified input in all nodes



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterinputstatesApi()
input_id = graylog.Object() # Object | 

try: 
    # Stop specified input in all nodes
    api_response = api_instance.stop(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterinputstatesApi->stop: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

