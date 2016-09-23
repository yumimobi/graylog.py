# graylog.SystempermissionsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions**](SystempermissionsApi.md#permissions) | **GET** /system/permissions | Get all available user permissions.
[**reader_permissions**](SystempermissionsApi.md#reader_permissions) | **GET** /system/permissions/reader/{username} | Get the initial permissions assigned to a reader account


# **permissions**
> Map permissions()

Get all available user permissions.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystempermissionsApi()

try: 
    # Get all available user permissions.
    api_response = api_instance.permissions()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystempermissionsApi->permissions: %s\n" % e
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

# **reader_permissions**
> ReaderPermissionResponse reader_permissions(username)

Get the initial permissions assigned to a reader account



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystempermissionsApi()
username = graylog.Object() # Object | 

try: 
    # Get the initial permissions assigned to a reader account
    api_response = api_instance.reader_permissions(username)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystempermissionsApi->reader_permissions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)|  | 

### Return type

[**ReaderPermissionResponse**](ReaderPermissionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

