# graylog.SearchdecoratorsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SearchdecoratorsApi.md#create) | **POST** /search/decorators | Creates a message decoration configuration
[**delete**](SearchdecoratorsApi.md#delete) | **DELETE** /search/decorators/{decoratorId} | Create a decorator
[**get**](SearchdecoratorsApi.md#get) | **GET** /search/decorators | Returns all configured message decorations
[**get_available**](SearchdecoratorsApi.md#get_available) | **GET** /search/decorators/available | Returns all available message decorations
[**update**](SearchdecoratorsApi.md#update) | **PUT** /search/decorators/{decoratorId} | Update a decorator


# **create**
> Decorator create(json_body)

Creates a message decoration configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchdecoratorsApi()
json_body = graylog.DecoratorImpl() # DecoratorImpl | 

try: 
    # Creates a message decoration configuration
    api_response = api_instance.create(json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchdecoratorsApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**DecoratorImpl**](DecoratorImpl.md)|  | 

### Return type

[**Decorator**](Decorator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(decorator_id)

Create a decorator



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchdecoratorsApi()
decorator_id = graylog.Object() # Object | 

try: 
    # Create a decorator
    api_instance.delete(decorator_id)
except ApiException as e:
    print "Exception when calling SearchdecoratorsApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decorator_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> List get()

Returns all configured message decorations



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchdecoratorsApi()

try: 
    # Returns all configured message decorations
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchdecoratorsApi->get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available**
> Map get_available()

Returns all available message decorations



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchdecoratorsApi()

try: 
    # Returns all available message decorations
    api_response = api_instance.get_available()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchdecoratorsApi->get_available: %s\n" % e
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
> Decorator update(decorator_id, json_body)

Update a decorator



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchdecoratorsApi()
decorator_id = graylog.Object() # Object | 
json_body = graylog.DecoratorImpl() # DecoratorImpl | 

try: 
    # Update a decorator
    api_response = api_instance.update(decorator_id, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchdecoratorsApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decorator_id** | [**Object**](.md)|  | 
 **json_body** | [**DecoratorImpl**](DecoratorImpl.md)|  | 

### Return type

[**Decorator**](Decorator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

