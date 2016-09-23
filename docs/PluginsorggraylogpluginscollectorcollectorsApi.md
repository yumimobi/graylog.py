# graylog.PluginsorggraylogpluginscollectorcollectorsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](PluginsorggraylogpluginscollectorcollectorsApi.md#get) | **GET** /plugins/org.graylog.plugins.collector/collectors/{collectorId} | Returns at most one collector summary for the specified collector id
[**list**](PluginsorggraylogpluginscollectorcollectorsApi.md#list) | **GET** /plugins/org.graylog.plugins.collector/collectors | Lists all existing collector registrations
[**register**](PluginsorggraylogpluginscollectorcollectorsApi.md#register) | **PUT** /plugins/org.graylog.plugins.collector/collectors/{collectorId} | Create/update a collector registration


# **get**
> CollectorSummary get(collector_id)

Returns at most one collector summary for the specified collector id



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorcollectorsApi()
collector_id = graylog.Object() # Object | 

try: 
    # Returns at most one collector summary for the specified collector id
    api_response = api_instance.get(collector_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorcollectorsApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | [**Object**](.md)|  | 

### Return type

[**CollectorSummary**](CollectorSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> CollectorList list()

Lists all existing collector registrations



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorcollectorsApi()

try: 
    # Lists all existing collector registrations
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorcollectorsApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectorList**](CollectorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> register(collector_id, json_body)

Create/update a collector registration

This is a stateless method which upserts a collector registration

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorcollectorsApi()
collector_id = graylog.Object() # Object | The collector id this collector is registering as.
json_body = graylog.CollectorRegistrationRequest() # CollectorRegistrationRequest | 

try: 
    # Create/update a collector registration
    api_instance.register(collector_id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorcollectorsApi->register: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | [**Object**](.md)| The collector id this collector is registering as. | 
 **json_body** | [**CollectorRegistrationRequest**](CollectorRegistrationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

