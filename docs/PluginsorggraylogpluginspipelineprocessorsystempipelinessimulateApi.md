# graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinessimulateApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simulate**](PluginsorggraylogpluginspipelineprocessorsystempipelinessimulateApi.md#simulate) | **POST** /plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/simulate | Simulate the execution of the pipeline message processor


# **simulate**
> SimulationResponse simulate(simulation)

Simulate the execution of the pipeline message processor



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginspipelineprocessorsystempipelinessimulateApi()
simulation = graylog.SimulationRequest() # SimulationRequest | 

try: 
    # Simulate the execution of the pipeline message processor
    api_response = api_instance.simulate(simulation)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginspipelineprocessorsystempipelinessimulateApi->simulate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | [**SimulationRequest**](SimulationRequest.md)|  | 

### Return type

[**SimulationResponse**](SimulationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

