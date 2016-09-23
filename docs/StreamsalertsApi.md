# graylog.StreamsalertsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_all**](StreamsalertsApi.md#list_all) | **GET** /streams/alerts | Get the 300 most recent alarms of all streams.


# **list_all**
> AlertListSummary list_all(since=since)

Get the 300 most recent alarms of all streams.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.StreamsalertsApi()
since = graylog.Object() # Object | Optional parameter to define a lower date boundary. (UNIX timestamp) (optional)

try: 
    # Get the 300 most recent alarms of all streams.
    api_response = api_instance.list_all(since=since)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StreamsalertsApi->list_all: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**Object**](.md)| Optional parameter to define a lower date boundary. (UNIX timestamp) | [optional] 

### Return type

[**AlertListSummary**](AlertListSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

