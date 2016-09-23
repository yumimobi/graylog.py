# graylog.SysteminputsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SysteminputsApi.md#create) | **POST** /system/inputs | Launch input on this node
[**get**](SysteminputsApi.md#get) | **GET** /system/inputs/{inputId} | Get information of a single input on this node
[**list**](SysteminputsApi.md#list) | **GET** /system/inputs | Get all inputs
[**terminate**](SysteminputsApi.md#terminate) | **DELETE** /system/inputs/{inputId} | Terminate input on this node
[**update**](SysteminputsApi.md#update) | **PUT** /system/inputs/{inputId} | Update input on this node


# **create**
> create(json_body)

Launch input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputsApi()
json_body = graylog.InputCreateRequest() # InputCreateRequest | 

try: 
    # Launch input on this node
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling SysteminputsApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**InputCreateRequest**](InputCreateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> InputSummary get(input_id)

Get information of a single input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputsApi()
input_id = graylog.Object() # Object | 

try: 
    # Get information of a single input on this node
    api_response = api_instance.get(input_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputsApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

[**InputSummary**](InputSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> InputsList list()

Get all inputs



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputsApi()

try: 
    # Get all inputs
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputsApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InputsList**](InputsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate**
> terminate(input_id)

Terminate input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputsApi()
input_id = graylog.Object() # Object | 

try: 
    # Terminate input on this node
    api_instance.terminate(input_id)
except ApiException as e:
    print "Exception when calling SysteminputsApi->terminate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(json_body, input_id)

Update input on this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputsApi()
json_body = graylog.InputCreateRequest() # InputCreateRequest | 
input_id = graylog.Object() # Object | 

try: 
    # Update input on this node
    api_instance.update(json_body, input_id)
except ApiException as e:
    print "Exception when calling SysteminputsApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**InputCreateRequest**](InputCreateRequest.md)|  | 
 **input_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

