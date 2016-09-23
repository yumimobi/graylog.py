# graylog.SearchsavedApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SearchsavedApi.md#create) | **POST** /search/saved | Create a new saved search
[**delete**](SearchsavedApi.md#delete) | **DELETE** /search/saved/{searchId} | Delete a saved search
[**get**](SearchsavedApi.md#get) | **GET** /search/saved/{searchId} | Get a single saved search
[**list**](SearchsavedApi.md#list) | **GET** /search/saved | Get a list of all saved searches
[**update**](SearchsavedApi.md#update) | **PUT** /search/saved/{searchId} | Update a saved search


# **create**
> create(json_body)

Create a new saved search



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchsavedApi()
json_body = graylog.CreateSavedSearchRequest() # CreateSavedSearchRequest | 

try: 
    # Create a new saved search
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling SearchsavedApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CreateSavedSearchRequest**](CreateSavedSearchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(search_id)

Delete a saved search



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchsavedApi()
search_id = graylog.Object() # Object | 

try: 
    # Delete a saved search
    api_instance.delete(search_id)
except ApiException as e:
    print "Exception when calling SearchsavedApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Map get(search_id)

Get a single saved search



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchsavedApi()
search_id = graylog.Object() # Object | 

try: 
    # Get a single saved search
    api_response = api_instance.get(search_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchsavedApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**Object**](.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> Map list()

Get a list of all saved searches



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchsavedApi()

try: 
    # Get a list of all saved searches
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchsavedApi->list: %s\n" % e
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

# **update**
> Map update(search_id, json_body)

Update a saved search



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchsavedApi()
search_id = graylog.Object() # Object | 
json_body = graylog.CreateSavedSearchRequest() # CreateSavedSearchRequest | 

try: 
    # Update a saved search
    api_response = api_instance.update(search_id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchsavedApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**Object**](.md)|  | 
 **json_body** | [**CreateSavedSearchRequest**](CreateSavedSearchRequest.md)|  | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

