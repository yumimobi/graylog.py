# graylog.SystemprocessingApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pause_processing**](SystemprocessingApi.md#pause_processing) | **PUT** /system/processing/pause | Pauses message processing
[**resume_processing**](SystemprocessingApi.md#resume_processing) | **PUT** /system/processing/resume | Resume message processing


# **pause_processing**
> pause_processing()

Pauses message processing

If the message journal is enabled, incoming messages will be spooled on disk, if it is disabled, you might lose messages from inputs which cannot buffer themselves, like AMQP or Kafka-based inputs.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemprocessingApi()

try: 
    # Pauses message processing
    api_instance.pause_processing()
except ApiException as e:
    print "Exception when calling SystemprocessingApi->pause_processing: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_processing**
> resume_processing()

Resume message processing



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemprocessingApi()

try: 
    # Resume message processing
    api_instance.resume_processing()
except ApiException as e:
    print "Exception when calling SystemprocessingApi->resume_processing: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

