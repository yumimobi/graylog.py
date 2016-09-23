# graylog.SystemjournalApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show**](SystemjournalApi.md#show) | **GET** /system/journal | Get current state of the journal on this node.


# **show**
> JournalSummaryResponse show()

Get current state of the journal on this node.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemjournalApi()

try: 
    # Get current state of the journal on this node.
    api_response = api_instance.show()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemjournalApi->show: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JournalSummaryResponse**](JournalSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

