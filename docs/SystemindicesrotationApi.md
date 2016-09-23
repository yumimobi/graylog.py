# graylog.SystemindicesrotationApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](SystemindicesrotationApi.md#config) | **GET** /system/indices/rotation/config | Configuration of the current rotation strategy
[**config_0**](SystemindicesrotationApi.md#config_0) | **PUT** /system/indices/rotation/config | Configuration of the current rotation strategy
[**config_schema**](SystemindicesrotationApi.md#config_schema) | **GET** /system/indices/rotation/strategies/{strategy} | Show JSON schema for configuration of given rotation strategies
[**list**](SystemindicesrotationApi.md#list) | **GET** /system/indices/rotation/strategies | List available rotation strategies


# **config**
> RotationStrategySummary config()

Configuration of the current rotation strategy

This resource returns the configuration of the currently used rotation strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrotationApi()

try: 
    # Configuration of the current rotation strategy
    api_response = api_instance.config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrotationApi->config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RotationStrategySummary**](RotationStrategySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_0**
> RotationStrategySummary config_0()

Configuration of the current rotation strategy

This resource stores the configuration of the currently used rotation strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrotationApi()
 = graylog.RotationStrategySummary() # RotationStrategySummary | The description of the rotation strategy and its configuration

try: 
    # Configuration of the current rotation strategy
    api_response = api_instance.config_0()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrotationApi->config_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [**RotationStrategySummary**](RotationStrategySummary.md)| The description of the rotation strategy and its configuration | 

### Return type

[**RotationStrategySummary**](RotationStrategySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_schema**
> RotationStrategyDescription config_schema(strategy)

Show JSON schema for configuration of given rotation strategies

This resource returns a JSON schema for the configuration of the given rotation strategy.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrotationApi()
strategy = graylog.Object() # Object | The name of the rotation strategy

try: 
    # Show JSON schema for configuration of given rotation strategies
    api_response = api_instance.config_schema(strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrotationApi->config_schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy** | [**Object**](.md)| The name of the rotation strategy | 

### Return type

[**RotationStrategyDescription**](RotationStrategyDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> RotationStrategies list()

List available rotation strategies

This resource returns a list of all available rotation strategies on this Graylog node.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindicesrotationApi()

try: 
    # List available rotation strategies
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindicesrotationApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RotationStrategies**](RotationStrategies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

