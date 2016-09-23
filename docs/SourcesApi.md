# graylog.SourcesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SourcesApi.md#list) | **GET** /sources | Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.


# **list**
> SourcesList list(range, size=size)

Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.

Range: The parameter is in seconds relative to the current time. 86400 means 'in the last day',0 is special and means 'across all indices'

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SourcesApi()
range = graylog.Object() # Object | Relative timeframe to search in. See method description.
size = graylog.Object() # Object | Maximum size of the result set. (optional) (default to 5000)

try: 
    # Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.
    api_response = api_instance.list(range, size=size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SourcesApi->list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | [**Object**](.md)| Relative timeframe to search in. See method description. | 
 **size** | [**Object**](.md)| Maximum size of the result set. | [optional] [default to 5000]

### Return type

[**SourcesList**](SourcesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

