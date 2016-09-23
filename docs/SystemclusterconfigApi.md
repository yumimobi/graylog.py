# graylog.SystemclusterconfigApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](SystemclusterconfigApi.md#delete) | **DELETE** /system/cluster_config/{configClass} | Delete configuration settings from database
[**list**](SystemclusterconfigApi.md#list) | **GET** /system/cluster_config | List all configuration classes
[**schema**](SystemclusterconfigApi.md#schema) | **GET** /system/cluster_config/{configClass} | Get JSON schema of configuration class
[**update**](SystemclusterconfigApi.md#update) | **PUT** /system/cluster_config/{configClass} | Update configuration in database


# **delete**
> delete(config_class)

Delete configuration settings from database



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterconfigApi()
config_class = graylog.Object() # Object | The name of the cluster configuration class

try: 
    # Delete configuration settings from database
    api_instance.delete(config_class)
except ApiException as e:
    print "Exception when calling SystemclusterconfigApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | [**Object**](.md)| The name of the cluster configuration class | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ClusterConfigList list()

List all configuration classes



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterconfigApi()

try: 
    # List all configuration classes
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterconfigApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfigList**](ClusterConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema**
> JsonSchema schema(config_class)

Get JSON schema of configuration class



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterconfigApi()
config_class = graylog.Object() # Object | The name of the cluster configuration class

try: 
    # Get JSON schema of configuration class
    api_response = api_instance.schema(config_class)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterconfigApi->schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | [**Object**](.md)| The name of the cluster configuration class | 

### Return type

[**JsonSchema**](JsonSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/schema+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(config_class, body)

Update configuration in database



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterconfigApi()
config_class = graylog.Object() # Object | The name of the cluster configuration class
body = graylog.InputStream() # InputStream | The payload of the cluster configuration

try: 
    # Update configuration in database
    api_instance.update(config_class, body)
except ApiException as e:
    print "Exception when calling SystemclusterconfigApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | [**Object**](.md)| The name of the cluster configuration class | 
 **body** | [**InputStream**](InputStream.md)| The payload of the cluster configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

