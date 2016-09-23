# graylog.PluginsorggraylogpluginscollectorApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_configuration**](PluginsorggraylogpluginscollectorApi.md#copy_configuration) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/{name} | Copy a configuration
[**copy_input**](PluginsorggraylogpluginscollectorApi.md#copy_input) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{inputId}/{name} | Copy a configuration input
[**copy_output**](PluginsorggraylogpluginscollectorApi.md#copy_output) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{outputId}/{name} | Copy a configuration output
[**copy_snippet**](PluginsorggraylogpluginscollectorApi.md#copy_snippet) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippetId}/{name} | Copy a configuration snippet
[**create_configuration**](PluginsorggraylogpluginscollectorApi.md#create_configuration) | **POST** /plugins/org.graylog.plugins.collector/configurations | Create new collector configuration
[**create_input**](PluginsorggraylogpluginscollectorApi.md#create_input) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/inputs | Create a configuration input
[**create_output**](PluginsorggraylogpluginscollectorApi.md#create_output) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/outputs | Create a configuration output
[**create_snippet**](PluginsorggraylogpluginscollectorApi.md#create_snippet) | **POST** /plugins/org.graylog.plugins.collector/configurations/{id}/snippets | Create a configuration snippet
[**delete_configuration**](PluginsorggraylogpluginscollectorApi.md#delete_configuration) | **DELETE** /plugins/org.graylog.plugins.collector/configurations/{id} | Delete a collector configuration
[**delete_input**](PluginsorggraylogpluginscollectorApi.md#delete_input) | **DELETE** /plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{inputId} | Delete input form configuration
[**delete_output**](PluginsorggraylogpluginscollectorApi.md#delete_output) | **DELETE** /plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{outputId} | Delete output from configuration
[**delete_snippet**](PluginsorggraylogpluginscollectorApi.md#delete_snippet) | **DELETE** /plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippetId} | Delete snippet from configuration
[**get_configuration**](PluginsorggraylogpluginscollectorApi.md#get_configuration) | **GET** /plugins/org.graylog.plugins.collector/{collectorId} | Get a single collector configuration
[**get_configurations**](PluginsorggraylogpluginscollectorApi.md#get_configurations) | **GET** /plugins/org.graylog.plugins.collector/configurations/{id} | Show collector configuration details
[**get_tags**](PluginsorggraylogpluginscollectorApi.md#get_tags) | **GET** /plugins/org.graylog.plugins.collector/configurations/tags | List all used tags
[**list_configurations**](PluginsorggraylogpluginscollectorApi.md#list_configurations) | **GET** /plugins/org.graylog.plugins.collector/configurations | List all collector configurations
[**update_configuration_name**](PluginsorggraylogpluginscollectorApi.md#update_configuration_name) | **PUT** /plugins/org.graylog.plugins.collector/configurations/{id}/name | Updates a collector configuration name
[**update_input**](PluginsorggraylogpluginscollectorApi.md#update_input) | **PUT** /plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{input_id} | Update a configuration input
[**update_output**](PluginsorggraylogpluginscollectorApi.md#update_output) | **PUT** /plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{output_id} | Update a configuration output
[**update_snippet**](PluginsorggraylogpluginscollectorApi.md#update_snippet) | **PUT** /plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippet_id} | Update a configuration snippet


# **copy_configuration**
> copy_configuration(id)

Copy a configuration

This is a stateless method which copies a collector configuration to one with another name

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Copy a configuration
    api_instance.copy_configuration(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->copy_configuration: %s\n" % e
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

# **copy_input**
> copy_input(id)

Copy a configuration input

This is a stateless method which copies a collector input to one with another name

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Copy a configuration input
    api_instance.copy_input(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->copy_input: %s\n" % e
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

# **copy_output**
> copy_output(id)

Copy a configuration output

This is a stateless method which copies a collector output to one with another name

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Copy a configuration output
    api_instance.copy_output(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->copy_output: %s\n" % e
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

# **copy_snippet**
> copy_snippet(id)

Copy a configuration snippet

This is a stateless method which copies a collector snippet to one with another name

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Copy a configuration snippet
    api_instance.copy_snippet(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->copy_snippet: %s\n" % e
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

# **create_configuration**
> CollectorConfiguration create_configuration(json_body, create_defaults=create_defaults)

Create new collector configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
json_body = graylog.CollectorConfiguration() # CollectorConfiguration | 
create_defaults = graylog.Object() # Object |  (optional)

try: 
    # Create new collector configuration
    api_response = api_instance.create_configuration(json_body, create_defaults=create_defaults)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->create_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CollectorConfiguration**](CollectorConfiguration.md)|  | 
 **create_defaults** | [**Object**](.md)|  | [optional] 

### Return type

[**CollectorConfiguration**](CollectorConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_input**
> create_input(id, json_body)

Create a configuration input

This is a stateless method which inserts a collector input

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
json_body = graylog.CollectorInput() # CollectorInput | 

try: 
    # Create a configuration input
    api_instance.create_input(id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->create_input: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorInput**](CollectorInput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_output**
> create_output(id, json_body)

Create a configuration output

This is a stateless method which inserts a collector output

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
json_body = graylog.CollectorOutput() # CollectorOutput | 

try: 
    # Create a configuration output
    api_instance.create_output(id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->create_output: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorOutput**](CollectorOutput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snippet**
> create_snippet(id, json_body)

Create a configuration snippet

This is a stateless method which inserts a collector configuration snippet

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
json_body = graylog.CollectorConfigurationSnippet() # CollectorConfigurationSnippet | 

try: 
    # Create a configuration snippet
    api_instance.create_snippet(id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->create_snippet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorConfigurationSnippet**](CollectorConfigurationSnippet.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration**
> delete_configuration(id)

Delete a collector configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Delete a collector configuration
    api_instance.delete_configuration(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->delete_configuration: %s\n" % e
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

# **delete_input**
> delete_input(id)

Delete input form configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Delete input form configuration
    api_instance.delete_input(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->delete_input: %s\n" % e
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

# **delete_output**
> delete_output(id)

Delete output from configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Delete output from configuration
    api_instance.delete_output(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->delete_output: %s\n" % e
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

# **delete_snippet**
> delete_snippet(id)

Delete snippet from configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Delete snippet from configuration
    api_instance.delete_snippet(id)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->delete_snippet: %s\n" % e
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

# **get_configuration**
> CollectorConfiguration get_configuration(collector_id, tags=tags)

Get a single collector configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
collector_id = graylog.Object() # Object | 
tags = graylog.Object() # Object |  (optional)

try: 
    # Get a single collector configuration
    api_response = api_instance.get_configuration(collector_id, tags=tags)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->get_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | [**Object**](.md)|  | 
 **tags** | [**Object**](.md)|  | [optional] 

### Return type

[**CollectorConfiguration**](CollectorConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations**
> CollectorConfiguration get_configurations(id)

Show collector configuration details



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 

try: 
    # Show collector configuration details
    api_response = api_instance.get_configurations(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->get_configurations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 

### Return type

[**CollectorConfiguration**](CollectorConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> List get_tags()

List all used tags



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()

try: 
    # List all used tags
    api_response = api_instance.get_tags()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->get_tags: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configurations**
> CollectorConfigurationListResponse list_configurations()

List all collector configurations



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()

try: 
    # List all collector configurations
    api_response = api_instance.list_configurations()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->list_configurations: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectorConfigurationListResponse**](CollectorConfigurationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_name**
> CollectorConfiguration update_configuration_name(id, json_body)

Updates a collector configuration name



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
json_body = graylog.CollectorConfiguration() # CollectorConfiguration | 

try: 
    # Updates a collector configuration name
    api_response = api_instance.update_configuration_name(id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->update_configuration_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorConfiguration**](CollectorConfiguration.md)|  | 

### Return type

[**CollectorConfiguration**](CollectorConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_input**
> update_input(id, input_id, json_body)

Update a configuration input

This is a stateless method which updates a collector input

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
input_id = graylog.Object() # Object | 
json_body = graylog.CollectorInput() # CollectorInput | 

try: 
    # Update a configuration input
    api_instance.update_input(id, input_id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->update_input: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **input_id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorInput**](CollectorInput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_output**
> update_output(id, output_id, json_body)

Update a configuration output

This is a stateless method which updates a collector output

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
output_id = graylog.Object() # Object | 
json_body = graylog.CollectorOutput() # CollectorOutput | 

try: 
    # Update a configuration output
    api_instance.update_output(id, output_id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->update_output: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **output_id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorOutput**](CollectorOutput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snippet**
> update_snippet(id, snippet_id, json_body)

Update a configuration snippet

This is a stateless method which updates a collector snippet

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginscollectorApi()
id = graylog.Object() # Object | 
snippet_id = graylog.Object() # Object | 
json_body = graylog.CollectorConfigurationSnippet() # CollectorConfigurationSnippet | 

try: 
    # Update a configuration snippet
    api_instance.update_snippet(id, snippet_id, json_body)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginscollectorApi->update_snippet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Object**](.md)|  | 
 **snippet_id** | [**Object**](.md)|  | 
 **json_body** | [**CollectorConfigurationSnippet**](CollectorConfigurationSnippet.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

