# graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_from_parser**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#create_from_parser) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline | Create a processing pipeline from source
[**delete**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#delete) | **DELETE** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline/{id} | Delete a processing pipeline
[**get**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#get) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline/{id} | Get a processing pipeline
[**get_all**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#get_all) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline | Get all processing pipelines
[**parse**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#parse) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline/parse | Parse a processing pipeline without saving it
[**update**](PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi.md#update) | **PUT** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/pipeline/{id} | Modify a processing pipeline


# **create_from_parser**
> PipelineSource create_from_parser(pipeline)

Create a processing pipeline from source



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()
pipeline = graylog.PipelineSource() # PipelineSource | 

try: 
    # Create a processing pipeline from source
    api_response = api_instance.create_from_parser(pipeline)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->create_from_parser: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**PipelineSource**](PipelineSource.md)|  | 

### Return type

[**PipelineSource**](PipelineSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a processing pipeline

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()
id = graylog.Object() # Object | 

try: 
    # Delete a processing pipeline
    api_instance.delete(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> PipelineSource get(id)

Get a processing pipeline

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()
id = graylog.Object() # Object | 

try: 
    # Get a processing pipeline
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 

### Return type

[**PipelineSource**](PipelineSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> Collection get_all()

Get all processing pipelines



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()

try: 
    # Get all processing pipelines
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->get_all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Collection**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse**
> PipelineSource parse(pipeline)

Parse a processing pipeline without saving it



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()
pipeline = graylog.PipelineSource() # PipelineSource | 

try: 
    # Parse a processing pipeline without saving it
    api_response = api_instance.parse(pipeline)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->parse: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**PipelineSource**](PipelineSource.md)|  | 

### Return type

[**PipelineSource**](PipelineSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> PipelineSource update(id, pipeline)

Modify a processing pipeline

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi()
id = graylog.Object() # Object | 
pipeline = graylog.PipelineSource() # PipelineSource | 

try: 
    # Modify a processing pipeline
    api_response = api_instance.update(id, pipeline)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinespipelineApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **pipeline** | [**PipelineSource**](PipelineSource.md)|  | 

### Return type

[**PipelineSource**](PipelineSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

