# graylog.StreamsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_stream**](StreamsApi.md#clone_stream) | **POST** /streams/{streamId}/clone | Clone a stream
[**create**](StreamsApi.md#create) | **POST** /streams | Create a stream
[**delete**](StreamsApi.md#delete) | **DELETE** /streams/{streamId} | Delete a stream
[**get**](StreamsApi.md#get) | **GET** /streams | Get a list of all streams
[**get_0**](StreamsApi.md#get_0) | **GET** /streams/{streamId} | Get a single stream
[**get_enabled**](StreamsApi.md#get_enabled) | **GET** /streams/enabled | Get a list of all enabled streams
[**pause**](StreamsApi.md#pause) | **POST** /streams/{streamId}/pause | Pause a stream
[**resume**](StreamsApi.md#resume) | **POST** /streams/{streamId}/resume | Resume a stream
[**test_match**](StreamsApi.md#test_match) | **POST** /streams/{streamId}/testMatch | Test matching of a stream against a supplied message
[**update**](StreamsApi.md#update) | **PUT** /streams/{streamId} | Update a stream


# **clone_stream**
> clone_stream(stream_id, json_body)

Clone a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 
json_body = graylog.CloneStreamRequest() # CloneStreamRequest | 

try: 
    # Clone a stream
    api_instance.clone_stream(stream_id, json_body)
except ApiException as e:
    print "Exception when calling StreamsApi->clone_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 
 **json_body** | [**CloneStreamRequest**](CloneStreamRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> create(json_body)

Create a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
json_body = graylog.CreateStreamRequest() # CreateStreamRequest | 

try: 
    # Create a stream
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling StreamsApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CreateStreamRequest**](CreateStreamRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(stream_id)

Delete a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 

try: 
    # Delete a stream
    api_instance.delete(stream_id)
except ApiException as e:
    print "Exception when calling StreamsApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> StreamListResponse get()

Get a list of all streams



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()

try: 
    # Get a list of all streams
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsApi->get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StreamListResponse**](StreamListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_0**
> StreamResponse get_0(stream_id)

Get a single stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 

try: 
    # Get a single stream
    api_response = api_instance.get_0(stream_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsApi->get_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 

### Return type

[**StreamResponse**](StreamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enabled**
> StreamListResponse get_enabled()

Get a list of all enabled streams



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()

try: 
    # Get a list of all enabled streams
    api_response = api_instance.get_enabled()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsApi->get_enabled: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StreamListResponse**](StreamListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause**
> pause(stream_id)

Pause a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 

try: 
    # Pause a stream
    api_instance.pause(stream_id)
except ApiException as e:
    print "Exception when calling StreamsApi->pause: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume**
> resume(stream_id)

Resume a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 

try: 
    # Resume a stream
    api_instance.resume(stream_id)
except ApiException as e:
    print "Exception when calling StreamsApi->resume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_match**
> TestMatchResponse test_match(stream_id, json_body)

Test matching of a stream against a supplied message



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 
json_body = graylog.Map() # Map | 

try: 
    # Test matching of a stream against a supplied message
    api_response = api_instance.test_match(stream_id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsApi->test_match: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 
 **json_body** | [**Map**](Map.md)|  | 

### Return type

[**TestMatchResponse**](TestMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> StreamResponse update(stream_id, json_body)

Update a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsApi()
stream_id = graylog.Object() # Object | 
json_body = graylog.UpdateStreamRequest() # UpdateStreamRequest | 

try: 
    # Update a stream
    api_response = api_instance.update(stream_id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 
 **json_body** | [**UpdateStreamRequest**](UpdateStreamRequest.md)|  | 

### Return type

[**StreamResponse**](StreamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

