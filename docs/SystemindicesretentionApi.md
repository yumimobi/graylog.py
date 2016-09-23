# graylog.SystemindicesretentionApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](SystemindicesretentionApi.md#config) | **GET** /system/indices/retention/config | Configuration of the current retention strategy
[**config_0**](SystemindicesretentionApi.md#config_0) | **PUT** /system/indices/retention/config | Configuration of the current retention strategy
[**config_schema**](SystemindicesretentionApi.md#config_schema) | **GET** /system/indices/retention/strategies/{strategy} | Show JSON schema for configuration of given retention strategies
[**list**](SystemindicesretentionApi.md#list) | **GET** /system/indices/retention/strategies | List available retention strategies


# **config**
> RetentionStrategySummary config()

Configuration of the current retention strategy

This resource returns the configuration of the currently used retention strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesretentionApi()

try: 
    # Configuration of the current retention strategy
    api_response = api_instance.config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesretentionApi->config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionStrategySummary**](RetentionStrategySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_0**
> RetentionStrategySummary config_0()

Configuration of the current retention strategy

This resource stores the configuration of the currently used retention strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesretentionApi()
 = graylog.RetentionStrategySummary() # RetentionStrategySummary | The description of the retention strategy and its configuration

try: 
    # Configuration of the current retention strategy
    api_response = api_instance.config_0()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesretentionApi->config_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [**RetentionStrategySummary**](RetentionStrategySummary.md)| The description of the retention strategy and its configuration | 

### Return type

[**RetentionStrategySummary**](RetentionStrategySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_schema**
> RetentionStrategyDescription config_schema(strategy)

Show JSON schema for configuration of given retention strategies

This resource returns a JSON schema for the configuration of the given retention strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesretentionApi()
strategy = graylog.Object() # Object | The name of the retention strategy

try: 
    # Show JSON schema for configuration of given retention strategies
    api_response = api_instance.config_schema(strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesretentionApi->config_schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy** | [**Object**](.md)| The name of the retention strategy | 

### Return type

[**RetentionStrategyDescription**](RetentionStrategyDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> RetentionStrategies list()

List available retention strategies

This resource returns a list of all available retention strategies on this Graylog node.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesretentionApi()

try: 
    # List available retention strategies
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesretentionApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionStrategies**](RetentionStrategies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

