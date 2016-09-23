# graylog.ClustermetricsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multiple_metrics_all_nodes**](ClustermetricsApi.md#multiple_metrics_all_nodes) | **POST** /cluster/metrics/multiple | Get all metrics of all nodes in the cluster


# **multiple_metrics_all_nodes**
> Map multiple_metrics_all_nodes(requested_metrics)

Get all metrics of all nodes in the cluster



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.ClustermetricsApi()
requested_metrics = graylog.MetricsReadRequest() # MetricsReadRequest | 

try: 
    # Get all metrics of all nodes in the cluster
    api_response = api_instance.multiple_metrics_all_nodes(requested_metrics)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClustermetricsApi->multiple_metrics_all_nodes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_metrics** | [**MetricsReadRequest**](MetricsReadRequest.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

