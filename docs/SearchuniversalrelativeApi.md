# graylog.SearchuniversalrelativeApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_search_relative_chunked**](SearchuniversalrelativeApi.md#export_search_relative_chunked) | **GET** /search/universal/relative/export | Export message search with relative timerange.
[**field_histogram_relative**](SearchuniversalrelativeApi.md#field_histogram_relative) | **GET** /search/universal/relative/fieldhistogram | Field value histogram of a query using a relative timerange.
[**histogram_relative**](SearchuniversalrelativeApi.md#histogram_relative) | **GET** /search/universal/relative/histogram | Datetime histogram of a query using a relative timerange.
[**search_relative**](SearchuniversalrelativeApi.md#search_relative) | **GET** /search/universal/relative | Message search with relative timerange.
[**stats_relative**](SearchuniversalrelativeApi.md#stats_relative) | **GET** /search/universal/relative/stats | Field statistics for a query using a relative timerange.
[**terms_relative**](SearchuniversalrelativeApi.md#terms_relative) | **GET** /search/universal/relative/terms | Most common field terms of a query using a relative timerange.
[**terms_stats_relative**](SearchuniversalrelativeApi.md#terms_stats_relative) | **GET** /search/universal/relative/termsstats | Ordered field terms of a query computed on another field using a relative timerange.


# **export_search_relative_chunked**
> export_search_relative_chunked(query, range, fields, limit=limit, offset=offset, filter=filter)

Export message search with relative timerange.

Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
query = graylog.Object() # Object | Query (Lucene syntax)
range = graylog.Object() # Object | Relative timeframe to search in. See method description.
fields = graylog.Object() # Object | Comma separated list of fields to return
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Export message search with relative timerange.
    api_instance.export_search_relative_chunked(query, range, fields, limit=limit, offset=offset, filter=filter)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->export_search_relative_chunked: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See method description. | 
 **fields** | [**Object**](.md)| Comma separated list of fields to return | 
 **limit** | [**Object**](.md)| Maximum number of messages to return. | [optional] 
 **offset** | [**Object**](.md)| Offset | [optional] 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **field_histogram_relative**
> HistogramResult field_histogram_relative(query, field, interval, range, filter=filter, cardinality=cardinality)

Field value histogram of a query using a relative timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
query = graylog.Object() # Object | Query (Lucene syntax)
field = graylog.Object() # Object | Field of whose values to get the histogram of
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
range = graylog.Object() # Object | Relative timeframe to search in. See search method description.
filter = graylog.Object() # Object | Filter (optional)
cardinality = graylog.Object() # Object | Calculate the cardinality of the field as well (optional)

try: 
    # Field value histogram of a query using a relative timerange.
    api_response = api_instance.field_histogram_relative(query, field, interval, range, filter=filter, cardinality=cardinality)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->field_histogram_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **field** | [**Object**](.md)| Field of whose values to get the histogram of | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See search method description. | 
 **filter** | [**Object**](.md)| Filter | [optional] 
 **cardinality** | [**Object**](.md)| Calculate the cardinality of the field as well | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **histogram_relative**
> HistogramResult histogram_relative(query, interval, range, filter=filter)

Datetime histogram of a query using a relative timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
query = graylog.Object() # Object | Query (Lucene syntax)
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
range = graylog.Object() # Object | Relative timeframe to search in. See search method description.
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Datetime histogram of a query using a relative timerange.
    api_response = api_instance.histogram_relative(query, interval, range, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->histogram_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See search method description. | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_relative**
> SearchResponse search_relative(query, range, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)

Message search with relative timerange.

Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
query = graylog.Object() # Object | Query (Lucene syntax)
range = graylog.Object() # Object | Relative timeframe to search in. See method description.
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)
fields = graylog.Object() # Object | Comma separated list of fields to return (optional)
sort = graylog.Object() # Object | Sorting (field:asc / field:desc) (optional)
decorate = graylog.Object() # Object | Run decorators on search result (optional) (default to true)

try: 
    # Message search with relative timerange.
    api_response = api_instance.search_relative(query, range, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->search_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See method description. | 
 **limit** | [**Object**](.md)| Maximum number of messages to return. | [optional] 
 **offset** | [**Object**](.md)| Offset | [optional] 
 **filter** | [**Object**](.md)| Filter | [optional] 
 **fields** | [**Object**](.md)| Comma separated list of fields to return | [optional] 
 **sort** | [**Object**](.md)| Sorting (field:asc / field:desc) | [optional] 
 **decorate** | [**Object**](.md)| Run decorators on search result | [optional] [default to true]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_relative**
> FieldStatsResult stats_relative(field, query, range, filter=filter)

Field statistics for a query using a relative timerange.

Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
field = graylog.Object() # Object | Message field of numeric type to return statistics for
query = graylog.Object() # Object | Query (Lucene syntax)
range = graylog.Object() # Object | Relative timeframe to search in. See search method description.
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Field statistics for a query using a relative timerange.
    api_response = api_instance.stats_relative(field, query, range, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->stats_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of numeric type to return statistics for | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See search method description. | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**FieldStatsResult**](FieldStatsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_relative**
> TermsResult terms_relative(field, query, range, size=size, filter=filter)

Most common field terms of a query using a relative timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
field = graylog.Object() # Object | Message field of to return terms of
query = graylog.Object() # Object | Query (Lucene syntax)
range = graylog.Object() # Object | Relative timeframe to search in. See search method description.
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Most common field terms of a query using a relative timerange.
    api_response = api_instance.terms_relative(field, query, range, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->terms_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of to return terms of | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See search method description. | 
 **size** | [**Object**](.md)| Maximum number of terms to return | [optional] 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**TermsResult**](TermsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_stats_relative**
> TermsStatsResult terms_stats_relative(key_field, value_field, order, query, range, size=size, filter=filter)

Ordered field terms of a query computed on another field using a relative timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalrelativeApi()
key_field = graylog.Object() # Object | Message field of to return terms of
value_field = graylog.Object() # Object | Value field used for computation
order = graylog.Object() # Object | What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)
query = graylog.Object() # Object | Query (Lucene syntax)
range = graylog.Object() # Object | Relative timeframe to search in. See search method description.
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Ordered field terms of a query computed on another field using a relative timerange.
    api_response = api_instance.terms_stats_relative(key_field, value_field, order, query, range, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalrelativeApi->terms_stats_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_field** | [**Object**](.md)| Message field of to return terms of | 
 **value_field** | [**Object**](.md)| Value field used for computation | 
 **order** | [**Object**](.md)| What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **range** | [**Object**](.md)| Relative timeframe to search in. See search method description. | 
 **size** | [**Object**](.md)| Maximum number of terms to return | [optional] 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**TermsStatsResult**](TermsStatsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

