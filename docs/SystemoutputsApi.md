# graylog.SystemoutputsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available**](SystemoutputsApi.md#available) | **GET** /system/outputs/available | Get all available output modules
[**create**](SystemoutputsApi.md#create) | **POST** /system/outputs | Create an output
[**delete**](SystemoutputsApi.md#delete) | **DELETE** /system/outputs/{outputId} | Delete output
[**get**](SystemoutputsApi.md#get) | **GET** /system/outputs | Get a list of all outputs
[**get_0**](SystemoutputsApi.md#get_0) | **GET** /system/outputs/{outputId} | Get specific output
[**update**](SystemoutputsApi.md#update) | **PUT** /system/outputs/{outputId} | Update output


# **available**
> Map available()

Get all available output modules



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()

try: 
    # Get all available output modules
    api_response = api_instance.available()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->available: %s\n" % e
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

# **create**
> create(json_body)

Create an output



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()
json_body = graylog.CreateOutputRequest() # CreateOutputRequest | 

try: 
    # Create an output
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CreateOutputRequest**](CreateOutputRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(output_id)

Delete output



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()
output_id = graylog.Object() # Object | The id of the output that should be deleted

try: 
    # Delete output
    api_instance.delete(output_id)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_id** | [**Object**](.md)| The id of the output that should be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> OutputListResponse get()

Get a list of all outputs



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()

try: 
    # Get a list of all outputs
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OutputListResponse**](OutputListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_0**
> OutputSummary get_0(output_id)

Get specific output



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()
output_id = graylog.Object() # Object | The id of the output we want.

try: 
    # Get specific output
    api_response = api_instance.get_0(output_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->get_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_id** | [**Object**](.md)| The id of the output we want. | 

### Return type

[**OutputSummary**](OutputSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Output update(output_id, json_body)

Update output



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemoutputsApi()
output_id = graylog.Object() # Object | The id of the output that should be deleted
json_body = graylog.Map() # Map | 

try: 
    # Update output
    api_response = api_instance.update(output_id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemoutputsApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_id** | [**Object**](.md)| The id of the output that should be deleted | 
 **json_body** | [**Map**](Map.md)|  | 

### Return type

[**Output**](Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

