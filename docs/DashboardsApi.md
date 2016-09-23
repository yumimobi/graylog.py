# graylog.DashboardsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DashboardsApi.md#create) | **POST** /dashboards | Create a dashboard
[**delete**](DashboardsApi.md#delete) | **DELETE** /dashboards/{dashboardId} | Delete a dashboard and all its widgets
[**get**](DashboardsApi.md#get) | **GET** /dashboards/{dashboardId} | Get a single dashboards and all configurations of its widgets.
[**list**](DashboardsApi.md#list) | **GET** /dashboards | Get a list of all dashboards and all configurations of their widgets.
[**set_positions**](DashboardsApi.md#set_positions) | **PUT** /dashboards/{dashboardId}/positions | Update/set the positions of dashboard widgets.
[**update**](DashboardsApi.md#update) | **PUT** /dashboards/{dashboardId} | Update the settings of a dashboard.


# **create**
> create(json_body)

Create a dashboard



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()
json_body = graylog.CreateDashboardRequest() # CreateDashboardRequest | 

try: 
    # Create a dashboard
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling DashboardsApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(dashboard_id)

Delete a dashboard and all its widgets



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()
dashboard_id = graylog.Object() # Object | 

try: 
    # Delete a dashboard and all its widgets
    api_instance.delete(dashboard_id)
except ApiException as e:
    print "Exception when calling DashboardsApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Map get(dashboard_id)

Get a single dashboards and all configurations of its widgets.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()
dashboard_id = graylog.Object() # Object | 

try: 
    # Get a single dashboards and all configurations of its widgets.
    api_response = api_instance.get(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardsApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**Object**](.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> DashboardList list()

Get a list of all dashboards and all configurations of their widgets.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()

try: 
    # Get a list of all dashboards and all configurations of their widgets.
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardsApi->list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardList**](DashboardList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_positions**
> set_positions(dashboard_id, json_body)

Update/set the positions of dashboard widgets.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()
dashboard_id = graylog.Object() # Object | 
json_body = graylog.WidgetPositionsRequest() # WidgetPositionsRequest | 

try: 
    # Update/set the positions of dashboard widgets.
    api_instance.set_positions(dashboard_id, json_body)
except ApiException as e:
    print "Exception when calling DashboardsApi->set_positions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**Object**](.md)|  | 
 **json_body** | [**WidgetPositionsRequest**](WidgetPositionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(dashboard_id, json_body)

Update the settings of a dashboard.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.DashboardsApi()
dashboard_id = graylog.Object() # Object | 
json_body = graylog.UpdateDashboardRequest() # UpdateDashboardRequest | 

try: 
    # Update the settings of a dashboard.
    api_instance.update(dashboard_id, json_body)
except ApiException as e:
    print "Exception when calling DashboardsApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**Object**](.md)|  | 
 **json_body** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

