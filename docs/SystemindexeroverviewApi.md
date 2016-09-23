# graylog.SystemindexeroverviewApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index**](SystemindexeroverviewApi.md#index) | **GET** /system/indexer/overview | Get overview of current indexing state, including deflector config, cluster state, index ranges &amp; message counts.


# **index**
> IndexerOverview index()

Get overview of current indexing state, including deflector config, cluster state, index ranges & message counts.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexeroverviewApi()

try: 
    # Get overview of current indexing state, including deflector config, cluster state, index ranges & message counts.
    api_response = api_instance.index()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexeroverviewApi->index: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexerOverview**](IndexerOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

