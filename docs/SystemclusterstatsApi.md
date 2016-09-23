# graylog.SystemclusterstatsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elasticsearch_stats**](SystemclusterstatsApi.md#elasticsearch_stats) | **GET** /system/cluster/stats/elasticsearch | Elasticsearch information.
[**mongo_stats**](SystemclusterstatsApi.md#mongo_stats) | **GET** /system/cluster/stats/mongo | MongoDB information.
[**system_stats**](SystemclusterstatsApi.md#system_stats) | **GET** /system/cluster/stats | Cluster status information.


# **elasticsearch_stats**
> ElasticsearchStats elasticsearch_stats()

Elasticsearch information.

This resource returns information about the Elasticsearch Cluster.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterstatsApi()

try: 
    # Elasticsearch information.
    api_response = api_instance.elasticsearch_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterstatsApi->elasticsearch_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ElasticsearchStats**](ElasticsearchStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_stats**
> MongoStats mongo_stats()

MongoDB information.

This resource returns information about MongoDB.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterstatsApi()

try: 
    # MongoDB information.
    api_response = api_instance.mongo_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterstatsApi->mongo_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MongoStats**](MongoStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_stats**
> ClusterStats system_stats()

Cluster status information.

This resource returns information about the Graylog cluster.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterstatsApi()

try: 
    # Cluster status information.
    api_response = api_instance.system_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterstatsApi->system_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStats**](ClusterStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

