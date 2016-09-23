# graylog.SystempluginsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SystempluginsApi.md#list) | **GET** /system/plugins | List all installed plugins on this node.


# **list**
> PluginList list()

List all installed plugins on this node.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystempluginsApi()

try: 
    # List all installed plugins on this node.
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystempluginsApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PluginList**](PluginList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

