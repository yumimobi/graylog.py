# graylog.SystemindexerfailuresApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count**](SystemindexerfailuresApi.md#count) | **GET** /system/indexer/failures/count | Total count of failed index operations since the given date.
[**single**](SystemindexerfailuresApi.md#single) | **GET** /system/indexer/failures | Get a list of failed index operations.


# **count**
> FailureCount count(since)

Total count of failed index operations since the given date.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerfailuresApi()
since = graylog.Object() # Object | ISO8601 date

try: 
    # Total count of failed index operations since the given date.
    api_response = api_instance.count(since)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerfailuresApi->count: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**Object**](.md)| ISO8601 date | 

### Return type

[**FailureCount**](FailureCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **single**
> Map single(limit, offset)

Get a list of failed index operations.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerfailuresApi()
limit = graylog.Object() # Object | Limit
offset = graylog.Object() # Object | Offset

try: 
    # Get a list of failed index operations.
    api_response = api_instance.single(limit, offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerfailuresApi->single: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**Object**](.md)| Limit | 
 **offset** | [**Object**](.md)| Offset | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

