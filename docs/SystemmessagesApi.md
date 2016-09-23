# graylog.SystemmessagesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SystemmessagesApi.md#all) | **GET** /system/messages | Get internal Graylog system messages


# **all**
> Map all(page=page)

Get internal Graylog system messages



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmessagesApi()
page = graylog.Object() # Object | Page (optional)

try: 
    # Get internal Graylog system messages
    api_response = api_instance.all(page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmessagesApi->all: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**Object**](.md)| Page | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

