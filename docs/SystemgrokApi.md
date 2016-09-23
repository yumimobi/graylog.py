# graylog.SystemgrokApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_patterns**](SystemgrokApi.md#bulk_update_patterns) | **PUT** /system/grok | Add a list of new patterns
[**create_pattern**](SystemgrokApi.md#create_pattern) | **POST** /system/grok | Add a new named pattern
[**list_grok_patterns**](SystemgrokApi.md#list_grok_patterns) | **GET** /system/grok | Get all existing grok patterns
[**list_pattern**](SystemgrokApi.md#list_pattern) | **GET** /system/grok/{patternId} | Get the existing grok pattern
[**remove_pattern**](SystemgrokApi.md#remove_pattern) | **DELETE** /system/grok/{patternId} | Remove an existing pattern by id
[**update_pattern**](SystemgrokApi.md#update_pattern) | **PUT** /system/grok/{patternId} | Update an existing pattern


# **bulk_update_patterns**
> bulk_update_patterns(patterns, replace=replace)

Add a list of new patterns



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()
patterns = graylog.GrokPatternList() # GrokPatternList | 
replace = graylog.Object() # Object | Replace all patterns with the new ones. (optional) (default to false)

try: 
    # Add a list of new patterns
    api_instance.bulk_update_patterns(patterns, replace=replace)
except ApiException as e:
    print "Exception when calling SystemgrokApi->bulk_update_patterns: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patterns** | [**GrokPatternList**](GrokPatternList.md)|  | 
 **replace** | [**Object**](.md)| Replace all patterns with the new ones. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pattern**
> create_pattern(pattern)

Add a new named pattern



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()
pattern = graylog.GrokPatternSummary() # GrokPatternSummary | 

try: 
    # Add a new named pattern
    api_instance.create_pattern(pattern)
except ApiException as e:
    print "Exception when calling SystemgrokApi->create_pattern: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | [**GrokPatternSummary**](GrokPatternSummary.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grok_patterns**
> GrokPatternList list_grok_patterns()

Get all existing grok patterns



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()

try: 
    # Get all existing grok patterns
    api_response = api_instance.list_grok_patterns()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemgrokApi->list_grok_patterns: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GrokPatternList**](GrokPatternList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pattern**
> GrokPattern list_pattern(pattern_id)

Get the existing grok pattern



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()
pattern_id = graylog.Object() # Object | 

try: 
    # Get the existing grok pattern
    api_response = api_instance.list_pattern(pattern_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemgrokApi->list_pattern: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | [**Object**](.md)|  | 

### Return type

[**GrokPattern**](GrokPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_pattern**
> remove_pattern()

Remove an existing pattern by id



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()

try: 
    # Remove an existing pattern by id
    api_instance.remove_pattern()
except ApiException as e:
    print "Exception when calling SystemgrokApi->remove_pattern: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pattern**
> GrokPattern update_pattern(pattern_id, pattern)

Update an existing pattern



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemgrokApi()
pattern_id = graylog.Object() # Object | 
pattern = graylog.GrokPatternSummary() # GrokPatternSummary | 

try: 
    # Update an existing pattern
    api_response = api_instance.update_pattern(pattern_id, pattern)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemgrokApi->update_pattern: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | [**Object**](.md)|  | 
 **pattern** | [**GrokPatternSummary**](GrokPatternSummary.md)|  | 

### Return type

[**GrokPattern**](GrokPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

