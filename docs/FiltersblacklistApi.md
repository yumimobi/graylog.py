# graylog.FiltersblacklistApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FiltersblacklistApi.md#create) | **POST** /filters/blacklist | Create a blacklist filter
[**delete**](FiltersblacklistApi.md#delete) | **DELETE** /filters/blacklist/{filterId} | Remove the existing blacklist filter
[**get**](FiltersblacklistApi.md#get) | **GET** /filters/blacklist/{filterId} | Get the existing blacklist filter
[**get_all**](FiltersblacklistApi.md#get_all) | **GET** /filters/blacklist | Get all blacklist filters
[**update**](FiltersblacklistApi.md#update) | **PUT** /filters/blacklist/{filterId} | Update an existing blacklist filter


# **create**
> create(filter_entry)

Create a blacklist filter

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.FiltersblacklistApi()
filter_entry = graylog.FilterDescription() # FilterDescription | 

try: 
    # Create a blacklist filter
    api_instance.create(filter_entry)
except ApiException as e:
    print "Exception when calling FiltersblacklistApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_entry** | [**FilterDescription**](FilterDescription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(filter_id)

Remove the existing blacklist filter

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.FiltersblacklistApi()
filter_id = graylog.Object() # Object | 

try: 
    # Remove the existing blacklist filter
    api_instance.delete(filter_id)
except ApiException as e:
    print "Exception when calling FiltersblacklistApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> FilterDescription get(filter_id)

Get the existing blacklist filter



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.FiltersblacklistApi()
filter_id = graylog.Object() # Object | 

try: 
    # Get the existing blacklist filter
    api_response = api_instance.get(filter_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FiltersblacklistApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**Object**](.md)|  | 

### Return type

[**FilterDescription**](FilterDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> Set get_all()

Get all blacklist filters



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.FiltersblacklistApi()

try: 
    # Get all blacklist filters
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FiltersblacklistApi->get_all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Set**](Set.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(filter_id, filter_entry)

Update an existing blacklist filter

It can take up to a second until the change is applied

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.FiltersblacklistApi()
filter_id = graylog.Object() # Object | 
filter_entry = graylog.FilterDescription() # FilterDescription | 

try: 
    # Update an existing blacklist filter
    api_instance.update(filter_id, filter_entry)
except ApiException as e:
    print "Exception when calling FiltersblacklistApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**Object**](.md)|  | 
 **filter_entry** | [**FilterDescription**](FilterDescription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

