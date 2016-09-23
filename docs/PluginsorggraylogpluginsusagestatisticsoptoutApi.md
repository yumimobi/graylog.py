# graylog.PluginsorggraylogpluginsusagestatisticsoptoutApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_opt_out_state**](PluginsorggraylogpluginsusagestatisticsoptoutApi.md#get_opt_out_state) | **GET** /plugins/org.graylog.plugins.usagestatistics/opt-out | Get opt-out status
[**set_opt_out_state**](PluginsorggraylogpluginsusagestatisticsoptoutApi.md#set_opt_out_state) | **POST** /plugins/org.graylog.plugins.usagestatistics/opt-out | Disable sending anonymous usage stats


# **get_opt_out_state**
> UsageStatsOptOutState get_opt_out_state()

Get opt-out status



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsusagestatisticsoptoutApi()

try: 
    # Get opt-out status
    api_response = api_instance.get_opt_out_state()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsusagestatisticsoptoutApi->get_opt_out_state: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UsageStatsOptOutState**](UsageStatsOptOutState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_opt_out_state**
> set_opt_out_state()

Disable sending anonymous usage stats



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsusagestatisticsoptoutApi()

try: 
    # Disable sending anonymous usage stats
    api_instance.set_opt_out_state()
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsusagestatisticsoptoutApi->set_opt_out_state: %s\n" % e
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

