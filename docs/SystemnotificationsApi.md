# graylog.SystemnotificationsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification**](SystemnotificationsApi.md#delete_notification) | **DELETE** /system/notifications/{notificationType} | Delete a notification
[**list_notifications**](SystemnotificationsApi.md#list_notifications) | **GET** /system/notifications | Get all active notifications


# **delete_notification**
> delete_notification(notification_type)

Delete a notification



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemnotificationsApi()
notification_type = graylog.Object() # Object | 

try: 
    # Delete a notification
    api_instance.delete_notification(notification_type)
except ApiException as e:
    print "Exception when calling SystemnotificationsApi->delete_notification: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> Map list_notifications()

Get all active notifications



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemnotificationsApi()

try: 
    # Get all active notifications
    api_response = api_instance.list_notifications()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemnotificationsApi->list_notifications: %s\n" % e
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

