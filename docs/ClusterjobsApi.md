# graylog.ClusterjobsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](ClusterjobsApi.md#cancel_job) | **DELETE** /cluster/jobs/{jobId} | Cancel job with the given ID
[**get_job**](ClusterjobsApi.md#get_job) | **GET** /cluster/jobs/{jobId} | Get job with the given ID
[**list**](ClusterjobsApi.md#list) | **GET** /cluster/jobs | List currently running jobs


# **cancel_job**
> SystemJobSummary cancel_job(job_id)

Cancel job with the given ID



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterjobsApi()
job_id = graylog.Object() # Object | 

try: 
    # Cancel job with the given ID
    api_response = api_instance.cancel_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterjobsApi->cancel_job: %s\n" % e
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

# **get_job**
> SystemJobSummary get_job(job_id)

Get job with the given ID



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClusterjobsApi()
job_id = graylog.Object() # Object | 

try: 
    # Get job with the given ID
    api_response = api_instance.get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterjobsApi->get_job: %s\n" % e
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
api_instance = graylog.ClusterjobsApi()

try: 
    # List currently running jobs
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterjobsApi->list: %s\n" % e
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

