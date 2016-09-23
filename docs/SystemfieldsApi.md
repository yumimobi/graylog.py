# graylog.SystemfieldsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fields**](SystemfieldsApi.md#fields) | **GET** /system/fields | Get list of message fields that exist


# **fields**
> Map fields(limit=limit)

Get list of message fields that exist

This operation is comparably fast because it reads directly from the indexer mapping.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemfieldsApi()
limit = graylog.Object() # Object | Maximum number of fields to return. Set to 0 for all fields. (optional)

try: 
    # Get list of message fields that exist
    api_response = api_instance.fields(limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemfieldsApi->fields: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**Object**](.md)| Maximum number of fields to return. Set to 0 for all fields. | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

