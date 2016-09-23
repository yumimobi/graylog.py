# graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_pipelines**](PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi.md#connect_pipelines) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections | Connect processing pipelines to a stream
[**get_all**](PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi.md#get_all) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections | Get all pipeline connections
[**get_pipelines_for_stream**](PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi.md#get_pipelines_for_stream) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections/{streamId} | Get pipeline connections for the given stream


# **connect_pipelines**
> PipelineConnections connect_pipelines(json_body)

Connect processing pipelines to a stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi()
json_body = graylog.PipelineConnections() # PipelineConnections | 

try: 
    # Connect processing pipelines to a stream
    api_response = api_instance.connect_pipelines(json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi->connect_pipelines: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**PipelineConnections**](PipelineConnections.md)|  | 

### Return type

[**PipelineConnections**](PipelineConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> Set get_all()

Get all pipeline connections



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi()

try: 
    # Get all pipeline connections
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi->get_all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Set**](Set.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipelines_for_stream**
> PipelineConnections get_pipelines_for_stream(stream_id)

Get pipeline connections for the given stream



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi()
stream_id = graylog.Object() # Object | 

try: 
    # Get pipeline connections for the given stream
    api_response = api_instance.get_pipelines_for_stream(stream_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi->get_pipelines_for_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | [**Object**](.md)|  | 

### Return type

[**PipelineConnections**](PipelineConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

