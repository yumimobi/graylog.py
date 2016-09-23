# graylog.SystemindicesrangesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SystemindicesrangesApi.md#list) | **GET** /system/indices/ranges | Get a list of all index ranges
[**rebuild**](SystemindicesrangesApi.md#rebuild) | **POST** /system/indices/ranges/rebuild | Rebuild/sync index range information.
[**rebuild_index**](SystemindicesrangesApi.md#rebuild_index) | **POST** /system/indices/ranges/{index: [a-z_0-9]+}/rebuild | Rebuild/sync index range information.
[**show**](SystemindicesrangesApi.md#show) | **GET** /system/indices/ranges/{index: [a-z_0-9]+} | Show single index range


# **list**
> IndexRangesResponse list()

Get a list of all index ranges



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrangesApi()

try: 
    # Get a list of all index ranges
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrangesApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexRangesResponse**](IndexRangesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> rebuild()

Rebuild/sync index range information.

This triggers a systemjob that scans every index and stores meta information about what indices contain messages in what timeranges. It atomically overwrites already existing meta information.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrangesApi()

try: 
    # Rebuild/sync index range information.
    api_instance.rebuild()
except ApiException as e:
    print "Exception when calling SystemindicesrangesApi->rebuild: %s\n" % e
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

# **rebuild_index**
> rebuild_index(index)

Rebuild/sync index range information.

This triggers a system job that scans an index and stores meta information about what indices contain messages in what time ranges. It atomically overwrites already existing meta information.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrangesApi()
index = graylog.Object() # Object | The name of the Graylog-managed Elasticsearch index

try: 
    # Rebuild/sync index range information.
    api_instance.rebuild_index(index)
except ApiException as e:
    print "Exception when calling SystemindicesrangesApi->rebuild_index: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)| The name of the Graylog-managed Elasticsearch index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> IndexRangeSummary show(index)

Show single index range



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrangesApi()
index = graylog.Object() # Object | The name of the Graylog-managed Elasticsearch index

try: 
    # Show single index range
    api_response = api_instance.show(index)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrangesApi->show: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)| The name of the Graylog-managed Elasticsearch index | 

### Return type

[**IndexRangeSummary**](IndexRangeSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

