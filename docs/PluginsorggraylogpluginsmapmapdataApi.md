# graylog.PluginsorggraylogpluginsmapmapdataApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**map_data**](PluginsorggraylogpluginsmapmapdataApi.md#map_data) | **POST** /plugins/org.graylog.plugins.map/mapdata | Get map data


# **map_data**
> MapDataSearchResult map_data(json_body)

Get map data



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsmapmapdataApi()
json_body = graylog.MapDataSearchRequest() # MapDataSearchRequest | 

try: 
    # Get map data
    api_response = api_instance.map_data(json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsmapmapdataApi->map_data: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**MapDataSearchRequest**](MapDataSearchRequest.md)|  | 

### Return type

[**MapDataSearchResult**](MapDataSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

