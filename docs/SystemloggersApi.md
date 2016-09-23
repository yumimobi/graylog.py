# graylog.SystemloggersApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loggers**](SystemloggersApi.md#loggers) | **GET** /system/loggers | List all loggers and their current levels
[**messages**](SystemloggersApi.md#messages) | **GET** /system/loggers/messages/recent | Get recent internal log messages
[**set_single_logger_level**](SystemloggersApi.md#set_single_logger_level) | **PUT** /system/loggers/{loggerName}/level/{level} | Set the loglevel of a single logger
[**set_subsystem_logger_level**](SystemloggersApi.md#set_subsystem_logger_level) | **PUT** /system/loggers/subsystems/{subsystem}/level/{level} | Set the loglevel of a whole subsystem
[**subsystems**](SystemloggersApi.md#subsystems) | **GET** /system/loggers/subsystems | List all logger subsystems and their current levels


# **loggers**
> LoggersSummary loggers()

List all loggers and their current levels



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemloggersApi()

try: 
    # List all loggers and their current levels
    api_response = api_instance.loggers()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemloggersApi->loggers: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoggersSummary**](LoggersSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages**
> LogMessagesSummary messages(limit=limit, level=level)

Get recent internal log messages



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemloggersApi()
limit = graylog.Object() # Object | How many log messages should be returned (optional) (default to 500)
level = graylog.Object() # Object | Which log level (or higher) should the messages have (optional) (default to ALL)

try: 
    # Get recent internal log messages
    api_response = api_instance.messages(limit=limit, level=level)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemloggersApi->messages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**Object**](.md)| How many log messages should be returned | [optional] [default to 500]
 **level** | [**Object**](.md)| Which log level (or higher) should the messages have | [optional] [default to ALL]

### Return type

[**LogMessagesSummary**](LogMessagesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_single_logger_level**
> set_single_logger_level(logger_name, level)

Set the loglevel of a single logger

Provided level is falling back to DEBUG if it does not exist

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemloggersApi()
logger_name = graylog.Object() # Object | 
level = graylog.Object() # Object | 

try: 
    # Set the loglevel of a single logger
    api_instance.set_single_logger_level(logger_name, level)
except ApiException as e:
    print "Exception when calling SystemloggersApi->set_single_logger_level: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger_name** | [**Object**](.md)|  | 
 **level** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subsystem_logger_level**
> set_subsystem_logger_level(subsystem, level)

Set the loglevel of a whole subsystem

Provided level is falling back to DEBUG if it does not exist

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemloggersApi()
subsystem = graylog.Object() # Object | 
level = graylog.Object() # Object | 

try: 
    # Set the loglevel of a whole subsystem
    api_instance.set_subsystem_logger_level(subsystem, level)
except ApiException as e:
    print "Exception when calling SystemloggersApi->set_subsystem_logger_level: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> SubsystemSummary subsystems()

List all logger subsystems and their current levels



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemloggersApi()

try: 
    # List all logger subsystems and their current levels
    api_response = api_instance.subsystems()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemloggersApi->subsystems: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubsystemSummary**](SubsystemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

