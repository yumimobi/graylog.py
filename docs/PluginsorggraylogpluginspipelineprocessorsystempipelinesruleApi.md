# graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_from_parser**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#create_from_parser) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule | Create a processing rule from source
[**delete**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#delete) | **DELETE** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id} | Delete a processing rule
[**function_descriptors**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#function_descriptors) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/functions | Get function descriptors
[**get**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#get) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id} | Get a processing rule
[**get_all**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#get_all) | **GET** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule | Get all processing rules
[**get_bulk**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#get_bulk) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/multiple | Retrieve the named processing rules in bulk
[**parse**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#parse) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/parse | Parse a processing rule without saving it
[**update**](PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi.md#update) | **PUT** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id} | Modify a processing rule


# **create_from_parser**
> RuleSource create_from_parser(rule)

Create a processing rule from source



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
rule = graylog.RuleSource() # RuleSource | 

try: 
    # Create a processing rule from source
    api_response = api_instance.create_from_parser(rule)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->create_from_parser: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**RuleSource**](RuleSource.md)|  | 

### Return type

[**RuleSource**](RuleSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a processing rule

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
id = graylog.Object() # Object | 

try: 
    # Delete a processing rule
    api_instance.delete(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->delete: %s\n" % e
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

# **function_descriptors**
> Collection function_descriptors()

Get function descriptors



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()

try: 
    # Get function descriptors
    api_response = api_instance.function_descriptors()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->function_descriptors: %s\n" % e
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

# **get**
> RuleSource get(id)

Get a processing rule

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
id = graylog.Object() # Object | 

try: 
    # Get a processing rule
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 

### Return type

[**RuleSource**](RuleSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> Collection get_all()

Get all processing rules



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()

try: 
    # Get all processing rules
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->get_all: %s\n" % e
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

# **get_bulk**
> Collection get_bulk(=)

Retrieve the named processing rules in bulk



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
 = graylog.BulkRuleRequest() # BulkRuleRequest | rules (optional)

try: 
    # Retrieve the named processing rules in bulk
    api_response = api_instance.get_bulk(=)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->get_bulk: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [**BulkRuleRequest**](BulkRuleRequest.md)| rules | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse**
> RuleSource parse(rule)

Parse a processing rule without saving it



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
rule = graylog.RuleSource() # RuleSource | 

try: 
    # Parse a processing rule without saving it
    api_response = api_instance.parse(rule)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->parse: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**RuleSource**](RuleSource.md)|  | 

### Return type

[**RuleSource**](RuleSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> RuleSource update(id, rule)

Modify a processing rule

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi()
id = graylog.Object() # Object | 
rule = graylog.RuleSource() # RuleSource | 

try: 
    # Modify a processing rule
    api_response = api_instance.update(id, rule)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **rule** | [**RuleSource**](RuleSource.md)|  | 

### Return type

[**RuleSource**](RuleSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

