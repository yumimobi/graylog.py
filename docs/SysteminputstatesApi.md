# graylog.SysteminputstatesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](SysteminputstatesApi.md#get) | **GET** /system/inputstates/{inputId} | Get input state for specified input id on this node
[**list**](SysteminputstatesApi.md#list) | **GET** /system/inputstates | Get all input states of this node
[**start**](SysteminputstatesApi.md#start) | **PUT** /system/inputstates/{inputId} | (Re-)Start specified input on this node
[**stop**](SysteminputstatesApi.md#stop) | **DELETE** /system/inputstates/{inputId} | Stop specified input on this node


# **get**
> InputStateSummary get(input_id)

Get input state for specified input id on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstatesApi()
input_id = graylog.Object() # Object | 

try: 
    # Get input state for specified input id on this node
    api_response = api_instance.get(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstatesApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**InputStateSummary**](InputStateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> InputStatesList list()

Get all input states of this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstatesApi()

try: 
    # Get all input states of this node
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstatesApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InputStatesList**](InputStatesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> InputCreated start(input_id)

(Re-)Start specified input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstatesApi()
input_id = graylog.Object() # Object | 

try: 
    # (Re-)Start specified input on this node
    api_response = api_instance.start(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstatesApi->start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**InputCreated**](InputCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> InputDeleted stop(input_id)

Stop specified input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstatesApi()
input_id = graylog.Object() # Object | 

try: 
    # Stop specified input on this node
    api_response = api_instance.stop(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstatesApi->stop: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**InputDeleted**](InputDeleted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

