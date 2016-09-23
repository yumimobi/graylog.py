# graylog.SystemgettingstartedApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss_getting_started**](SystemgettingstartedApi.md#dismiss_getting_started) | **POST** /system/gettingstarted/dismiss | Dismiss auto-showing getting started guide for this version
[**display_getting_started**](SystemgettingstartedApi.md#display_getting_started) | **GET** /system/gettingstarted | Check whether to display the Getting started guide for this version


# **dismiss_getting_started**
> dismiss_getting_started()

Dismiss auto-showing getting started guide for this version



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgettingstartedApi()

try: 
    # Dismiss auto-showing getting started guide for this version
    api_instance.dismiss_getting_started()
except ApiException as e:
    print "Exception when calling SystemgettingstartedApi->dismiss_getting_started: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_getting_started**
> DisplayGettingStarted display_getting_started()

Check whether to display the Getting started guide for this version



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgettingstartedApi()

try: 
    # Check whether to display the Getting started guide for this version
    api_response = api_instance.display_getting_started()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemgettingstartedApi->display_getting_started: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplayGettingStarted**](DisplayGettingStarted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

