# graylog.SystemindexerindicesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SystemindexerindicesApi.md#all) | **GET** /system/indexer/indices | List all open, closed and reopened indices.
[**close**](SystemindexerindicesApi.md#close) | **POST** /system/indexer/indices/{index}/close | Close an index. This will also trigger an index ranges rebuild job.
[**closed**](SystemindexerindicesApi.md#closed) | **GET** /system/indexer/indices/closed | Get a list of closed indices that can be reopened.
[**delete**](SystemindexerindicesApi.md#delete) | **DELETE** /system/indexer/indices/{index} | Delete an index. This will also trigger an index ranges rebuild job.
[**multiple**](SystemindexerindicesApi.md#multiple) | **POST** /system/indexer/indices/multiple | Get information of all specified indices and their shards.
[**open**](SystemindexerindicesApi.md#open) | **GET** /system/indexer/indices/open | Get information of all open indices managed by Graylog and their shards.
[**reopen**](SystemindexerindicesApi.md#reopen) | **POST** /system/indexer/indices/{index}/reopen | Reopen a closed index. This will also trigger an index ranges rebuild job.
[**reopened**](SystemindexerindicesApi.md#reopened) | **GET** /system/indexer/indices/reopened | Get a list of reopened indices, which will not be cleaned by retention cleaning
[**single**](SystemindexerindicesApi.md#single) | **GET** /system/indexer/indices/{index} | Get information of an index and its shards.


# **all**
> AllIndices all()

List all open, closed and reopened indices.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()

try: 
    # List all open, closed and reopened indices.
    api_response = api_instance.all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllIndices**](AllIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close**
> close(index)

Close an index. This will also trigger an index ranges rebuild job.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()
index = graylog.Object() # Object | 

try: 
    # Close an index. This will also trigger an index ranges rebuild job.
    api_instance.close(index)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->close: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **closed**
> ClosedIndices closed()

Get a list of closed indices that can be reopened.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()

try: 
    # Get a list of closed indices that can be reopened.
    api_response = api_instance.closed()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->closed: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClosedIndices**](ClosedIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(index)

Delete an index. This will also trigger an index ranges rebuild job.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()
index = graylog.Object() # Object | 

try: 
    # Delete an index. This will also trigger an index ranges rebuild job.
    api_instance.delete(index)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multiple**
> Map multiple(requested_indices)

Get information of all specified indices and their shards.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()
requested_indices = graylog.IndicesReadRequest() # IndicesReadRequest | 

try: 
    # Get information of all specified indices and their shards.
    api_response = api_instance.multiple(requested_indices)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->multiple: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_indices** | [**IndicesReadRequest**](IndicesReadRequest.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open**
> OpenIndicesInfo open()

Get information of all open indices managed by Graylog and their shards.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()

try: 
    # Get information of all open indices managed by Graylog and their shards.
    api_response = api_instance.open()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->open: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenIndicesInfo**](OpenIndicesInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen**
> reopen(index)

Reopen a closed index. This will also trigger an index ranges rebuild job.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()
index = graylog.Object() # Object | 

try: 
    # Reopen a closed index. This will also trigger an index ranges rebuild job.
    api_instance.reopen(index)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->reopen: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopened**
> ClosedIndices reopened()

Get a list of reopened indices, which will not be cleaned by retention cleaning



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()

try: 
    # Get a list of reopened indices, which will not be cleaned by retention cleaning
    api_response = api_instance.reopened()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->reopened: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClosedIndices**](ClosedIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **single**
> IndexInfo single(index)

Get information of an index and its shards.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerindicesApi()
index = graylog.Object() # Object | 

try: 
    # Get information of an index and its shards.
    api_response = api_instance.single(index)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerindicesApi->single: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)|  | 

### Return type

[**IndexInfo**](IndexInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

