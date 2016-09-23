# graylog.SystemclusterApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node**](SystemclusterApi.md#node) | **GET** /system/cluster/node | Information about this node.
[**node_0**](SystemclusterApi.md#node_0) | **GET** /system/cluster/nodes/{nodeId} | Information about a node.
[**nodes**](SystemclusterApi.md#nodes) | **GET** /system/cluster/nodes | List all active nodes in this cluster.


# **node**
> NodeSummary node()

Information about this node.

This is returning information of this node in context to its state in the cluster. Use the system API of the node itself to get system information.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterApi()

try: 
    # Information about this node.
    api_response = api_instance.node()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterApi->node: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSummary**](NodeSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_0**
> NodeSummary node_0(node_id)

Information about a node.

This is returning information of a node in context to its state in the cluster. Use the system API of the node itself to get system information.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterApi()
node_id = graylog.Object() # Object | 

try: 
    # Information about a node.
    api_response = api_instance.node_0(node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterApi->node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**Object**](.md)|  | 

### Return type

[**NodeSummary**](NodeSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes**
> NodeSummaryList nodes()

List all active nodes in this cluster.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemclusterApi()

try: 
    # List all active nodes in this cluster.
    api_response = api_instance.nodes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemclusterApi->nodes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSummaryList**](NodeSummaryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

