# graylog.ClustersystemloggersApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loggers**](ClustersystemloggersApi.md#loggers) | **GET** /cluster/system/loggers | List all loggers of all nodes and their current levels
[**set_subsystem_logger_level**](ClustersystemloggersApi.md#set_subsystem_logger_level) | **PUT** /cluster/system/loggers/{nodeId}/subsystems/{subsystem}/level/{level} | Set the loglevel of a whole subsystem
[**subsystems**](ClustersystemloggersApi.md#subsystems) | **GET** /cluster/system/loggers/subsystems | List all logger subsystems and their current levels


# **loggers**
> Map loggers()

List all loggers of all nodes and their current levels



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClustersystemloggersApi()

try: 
    # List all loggers of all nodes and their current levels
    api_response = api_instance.loggers()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClustersystemloggersApi->loggers: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subsystem_logger_level**
> set_subsystem_logger_level(node_id, subsystem, level)

Set the loglevel of a whole subsystem

Provided level is falling back to DEBUG if it does not exist

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClustersystemloggersApi()
node_id = graylog.Object() # Object | 
subsystem = graylog.Object() # Object | 
level = graylog.Object() # Object | 

try: 
    # Set the loglevel of a whole subsystem
    api_instance.set_subsystem_logger_level(node_id, subsystem, level)
except ApiException as e:
    print "Exception when calling ClustersystemloggersApi->set_subsystem_logger_level: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**Object**](.md)|  | 
 **subsystem** | [**Object**](.md)|  | 
 **level** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsystems**
> Map subsystems()

List all logger subsystems and their current levels



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClustersystemloggersApi()

try: 
    # List all logger subsystems and their current levels
    api_response = api_instance.subsystems()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClustersystemloggersApi->subsystems: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

