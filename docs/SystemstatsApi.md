# graylog.SystemstatsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fs_stats**](SystemstatsApi.md#fs_stats) | **GET** /system/stats/fs | Filesystem information about this node.
[**jvm_stats**](SystemstatsApi.md#jvm_stats) | **GET** /system/stats/jvm | JVM information about this node.
[**network_stats**](SystemstatsApi.md#network_stats) | **GET** /system/stats/network | Networking information about this node.
[**os_stats**](SystemstatsApi.md#os_stats) | **GET** /system/stats/os | OS information about this node.
[**process_stats**](SystemstatsApi.md#process_stats) | **GET** /system/stats/process | Process information about this node.
[**system_stats**](SystemstatsApi.md#system_stats) | **GET** /system/stats | System information about this node.


# **fs_stats**
> FsStats fs_stats()

Filesystem information about this node.

This resource returns information about the filesystems of this node.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # Filesystem information about this node.
    api_response = api_instance.fs_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->fs_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FsStats**](FsStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jvm_stats**
> JvmStats jvm_stats()

JVM information about this node.

This resource returns information about the Java Virtual Machine of this node.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # JVM information about this node.
    api_response = api_instance.jvm_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->jvm_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JvmStats**](JvmStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_stats**
> NetworkStats network_stats()

Networking information about this node.

This resource returns information about the networking system this node is running with.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # Networking information about this node.
    api_response = api_instance.network_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->network_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkStats**](NetworkStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_stats**
> OsStats os_stats()

OS information about this node.

This resource returns information about the operating system this node is running on.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # OS information about this node.
    api_response = api_instance.os_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->os_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OsStats**](OsStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_stats**
> ProcessStats process_stats()

Process information about this node.

This resource returns information about the process this node is running as.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # Process information about this node.
    api_response = api_instance.process_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->process_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessStats**](ProcessStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_stats**
> SystemStats system_stats()

System information about this node.

This resource returns information about the system this node is running on.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemstatsApi()

try: 
    # System information about this node.
    api_response = api_instance.system_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemstatsApi->system_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStats**](SystemStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

