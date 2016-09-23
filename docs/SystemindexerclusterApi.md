# graylog.SystemindexerclusterApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_health**](SystemindexerclusterApi.md#cluster_health) | **GET** /system/indexer/cluster/health | Get cluster and shard health overview
[**cluster_name**](SystemindexerclusterApi.md#cluster_name) | **GET** /system/indexer/cluster/name | Get the cluster name


# **cluster_health**
> ClusterHealth cluster_health()

Get cluster and shard health overview



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerclusterApi()

try: 
    # Get cluster and shard health overview
    api_response = api_instance.cluster_health()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerclusterApi->cluster_health: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterHealth**](ClusterHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_name**
> ClusterName cluster_name()

Get the cluster name



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemindexerclusterApi()

try: 
    # Get the cluster name
    api_response = api_instance.cluster_name()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemindexerclusterApi->cluster_name: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterName**](ClusterName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

