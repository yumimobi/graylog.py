# graylog.SysteminputstypesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SysteminputstypesApi.md#all) | **GET** /system/inputs/types/all | Get information about all input types
[**info**](SysteminputstypesApi.md#info) | **GET** /system/inputs/types/{inputType} | Get information about a single input type
[**types**](SysteminputstypesApi.md#types) | **GET** /system/inputs/types | Get all available input types of this node


# **all**
> Map all()

Get information about all input types



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstypesApi()

try: 
    # Get information about all input types
    api_response = api_instance.all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstypesApi->all: %s\n" % e
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

# **info**
> InputTypeInfo info(input_type)

Get information about a single input type



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstypesApi()
input_type = graylog.Object() # Object | 

try: 
    # Get information about a single input type
    api_response = api_instance.info(input_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstypesApi->info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_type** | [**Object**](.md)|  | 

### Return type

[**InputTypeInfo**](InputTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **types**
> InputTypesSummary types()

Get all available input types of this node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SysteminputstypesApi()

try: 
    # Get all available input types of this node
    api_response = api_instance.types()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SysteminputstypesApi->types: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InputTypesSummary**](InputTypesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

