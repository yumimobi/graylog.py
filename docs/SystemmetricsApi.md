# graylog.SystemmetricsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**by_namespace**](SystemmetricsApi.md#by_namespace) | **GET** /system/metrics/namespace/{namespace} | Get all metrics of a namespace
[**metric_names**](SystemmetricsApi.md#metric_names) | **GET** /system/metrics/names | Get all metrics keys/names
[**metrics**](SystemmetricsApi.md#metrics) | **GET** /system/metrics | Get all metrics
[**multiple_metrics**](SystemmetricsApi.md#multiple_metrics) | **POST** /system/metrics/multiple | Get the values of multiple metrics at once
[**single_metric**](SystemmetricsApi.md#single_metric) | **GET** /system/metrics/{metricName} | Get a single metric


# **by_namespace**
> MetricsSummaryResponse by_namespace(namespace)

Get all metrics of a namespace



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmetricsApi()
namespace = graylog.Object() # Object | 

try: 
    # Get all metrics of a namespace
    api_response = api_instance.by_namespace(namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmetricsApi->by_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | [**Object**](.md)|  | 

### Return type

[**MetricsSummaryResponse**](MetricsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_names**
> MetricNamesResponse metric_names()

Get all metrics keys/names



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmetricsApi()

try: 
    # Get all metrics keys/names
    api_response = api_instance.metric_names()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmetricsApi->metric_names: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetricNamesResponse**](MetricNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> MetricRegistry metrics()

Get all metrics

Note that this might return a huge result set.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmetricsApi()

try: 
    # Get all metrics
    api_response = api_instance.metrics()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmetricsApi->metrics: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetricRegistry**](MetricRegistry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multiple_metrics**
> MetricsSummaryResponse multiple_metrics(requested_metrics)

Get the values of multiple metrics at once



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmetricsApi()
requested_metrics = graylog.MetricsReadRequest() # MetricsReadRequest | 

try: 
    # Get the values of multiple metrics at once
    api_response = api_instance.multiple_metrics(requested_metrics)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmetricsApi->multiple_metrics: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_metrics** | [**MetricsReadRequest**](MetricsReadRequest.md)|  | 

### Return type

[**MetricsSummaryResponse**](MetricsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **single_metric**
> Metric single_metric(metric_name)

Get a single metric



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemmetricsApi()
metric_name = graylog.Object() # Object | 

try: 
    # Get a single metric
    api_response = api_instance.single_metric(metric_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemmetricsApi->single_metric: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_name** | [**Object**](.md)|  | 

### Return type

[**Metric**](Metric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

