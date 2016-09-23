# graylog.PluginsorggraylogpluginsusagestatisticsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_cluster_data_set**](PluginsorggraylogpluginsusagestatisticsApi.md#show_cluster_data_set) | **GET** /plugins/org.graylog.plugins.usagestatistics/cluster | Show the collected anonymous usage statistics of this Graylog cluster
[**show_config**](PluginsorggraylogpluginsusagestatisticsApi.md#show_config) | **GET** /plugins/org.graylog.plugins.usagestatistics/config | Show configuration for the anonymous usage statistics plugin
[**show_node_data_set**](PluginsorggraylogpluginsusagestatisticsApi.md#show_node_data_set) | **GET** /plugins/org.graylog.plugins.usagestatistics/node | Show the collected anonymous usage statistics of this Graylog node


# **show_cluster_data_set**
> ClusterDataSet show_cluster_data_set()

Show the collected anonymous usage statistics of this Graylog cluster



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsusagestatisticsApi()

try: 
    # Show the collected anonymous usage statistics of this Graylog cluster
    api_response = api_instance.show_cluster_data_set()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsusagestatisticsApi->show_cluster_data_set: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterDataSet**](ClusterDataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_config**
> UsageStatsConfigurationResponse show_config()

Show configuration for the anonymous usage statistics plugin



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsusagestatisticsApi()

try: 
    # Show configuration for the anonymous usage statistics plugin
    api_response = api_instance.show_config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsusagestatisticsApi->show_config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UsageStatsConfigurationResponse**](UsageStatsConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_node_data_set**
> NodeDataSet show_node_data_set()

Show the collected anonymous usage statistics of this Graylog node



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.PluginsorggraylogpluginsusagestatisticsApi()

try: 
    # Show the collected anonymous usage statistics of this Graylog node
    api_response = api_instance.show_node_data_set()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PluginsorggraylogpluginsusagestatisticsApi->show_node_data_set: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeDataSet**](NodeDataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

