# graylog.SystemjobsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](SystemjobsApi.md#cancel) | **DELETE** /system/jobs/{jobId} | Cancel running job
[**get**](SystemjobsApi.md#get) | **GET** /system/jobs/{jobId} | Get information of a specific currently running job
[**list**](SystemjobsApi.md#list) | **GET** /system/jobs | List currently running jobs
[**trigger**](SystemjobsApi.md#trigger) | **POST** /system/jobs | Trigger new job


# **cancel**
> SystemJobSummary cancel(job_id)

Cancel running job



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemjobsApi()
job_id = graylog.Object() # Object | 

try: 
    # Cancel running job
    api_response = api_instance.cancel(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemjobsApi->cancel: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**Object**](.md)|  | 

### Return type

[**SystemJobSummary**](SystemJobSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SystemJobSummary get(job_id)

Get information of a specific currently running job



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemjobsApi()
job_id = graylog.Object() # Object | 

try: 
    # Get information of a specific currently running job
    api_response = api_instance.get(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemjobsApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**Object**](.md)|  | 

### Return type

[**SystemJobSummary**](SystemJobSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> Map list()

List currently running jobs



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemjobsApi()

try: 
    # List currently running jobs
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemjobsApi->list: %s\n" % e
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

# **trigger**
> trigger(json_body)

Trigger new job



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemjobsApi()
json_body = graylog.TriggerRequest() # TriggerRequest | 

try: 
    # Trigger new job
    api_instance.trigger(json_body)
except ApiException as e:
    print "Exception when calling SystemjobsApi->trigger: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**TriggerRequest**](TriggerRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

