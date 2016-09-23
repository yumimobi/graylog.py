# graylog.SearchuniversalabsoluteApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_search_absolute_chunked**](SearchuniversalabsoluteApi.md#export_search_absolute_chunked) | **GET** /search/universal/absolute/export | Export message search with absolute timerange.
[**field_histogram_absolute**](SearchuniversalabsoluteApi.md#field_histogram_absolute) | **GET** /search/universal/absolute/fieldhistogram | Field value histogram of a query using an absolute timerange.
[**histogram_absolute**](SearchuniversalabsoluteApi.md#histogram_absolute) | **GET** /search/universal/absolute/histogram | Datetime histogram of a query using an absolute timerange.
[**search_absolute**](SearchuniversalabsoluteApi.md#search_absolute) | **GET** /search/universal/absolute | Message search with absolute timerange.
[**stats_absolute**](SearchuniversalabsoluteApi.md#stats_absolute) | **GET** /search/universal/absolute/stats | Field statistics for a query using an absolute timerange.
[**terms_absolute**](SearchuniversalabsoluteApi.md#terms_absolute) | **GET** /search/universal/absolute/terms | Most common field terms of a query using an absolute timerange.
[**terms_stats_absolute**](SearchuniversalabsoluteApi.md#terms_stats_absolute) | **GET** /search/universal/absolute/termsstats | Ordered field terms of a query computed on another field using an absolute timerange.


# **export_search_absolute_chunked**
> export_search_absolute_chunked(query, _from, to, fields, limit=limit, offset=offset, filter=filter)

Export message search with absolute timerange.

Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
query = graylog.Object() # Object | Query (Lucene syntax)
_from = graylog.Object() # Object | Timerange start. See description for date format
to = graylog.Object() # Object | Timerange end. See description for date format
fields = graylog.Object() # Object | Comma separated list of fields to return
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Export message search with absolute timerange.
    api_instance.export_search_absolute_chunked(query, _from, to, fields, limit=limit, offset=offset, filter=filter)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->export_search_absolute_chunked: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **_from** | [**Object**](.md)| Timerange start. See description for date format | 
 **to** | [**Object**](.md)| Timerange end. See description for date format | 
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

# **field_histogram_absolute**
> HistogramResult field_histogram_absolute(query, field, interval, _from, to, filter=filter, cardinality=cardinality)

Field value histogram of a query using an absolute timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
query = graylog.Object() # Object | Query (Lucene syntax)
field = graylog.Object() # Object | Field of whose values to get the histogram of
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
_from = graylog.Object() # Object | Timerange start. See search method description for date format
to = graylog.Object() # Object | Timerange end. See search method description for date format
filter = graylog.Object() # Object | Filter (optional)
cardinality = graylog.Object() # Object | Calculate the cardinality of the field as well (optional)

try: 
    # Field value histogram of a query using an absolute timerange.
    api_response = api_instance.field_histogram_absolute(query, field, interval, _from, to, filter=filter, cardinality=cardinality)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->field_histogram_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **field** | [**Object**](.md)| Field of whose values to get the histogram of | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **_from** | [**Object**](.md)| Timerange start. See search method description for date format | 
 **to** | [**Object**](.md)| Timerange end. See search method description for date format | 
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

# **histogram_absolute**
> HistogramResult histogram_absolute(query, interval, _from, to, filter=filter)

Datetime histogram of a query using an absolute timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
query = graylog.Object() # Object | Query (Lucene syntax)
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
_from = graylog.Object() # Object | Timerange start. See search method description for date format
to = graylog.Object() # Object | Timerange end. See search method description for date format
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Datetime histogram of a query using an absolute timerange.
    api_response = api_instance.histogram_absolute(query, interval, _from, to, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->histogram_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **_from** | [**Object**](.md)| Timerange start. See search method description for date format | 
 **to** | [**Object**](.md)| Timerange end. See search method description for date format | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_absolute**
> SearchResponse search_absolute(query, _from, to, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)

Message search with absolute timerange.

Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
query = graylog.Object() # Object | Query (Lucene syntax)
_from = graylog.Object() # Object | Timerange start. See description for date format
to = graylog.Object() # Object | Timerange end. See description for date format
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)
fields = graylog.Object() # Object | Comma separated list of fields to return (optional)
sort = graylog.Object() # Object | Sorting (field:asc / field:desc) (optional)
decorate = graylog.Object() # Object | Run decorators on search result (optional) (default to true)

try: 
    # Message search with absolute timerange.
    api_response = api_instance.search_absolute(query, _from, to, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->search_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **_from** | [**Object**](.md)| Timerange start. See description for date format | 
 **to** | [**Object**](.md)| Timerange end. See description for date format | 
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

# **stats_absolute**
> FieldStatsResult stats_absolute(field, query, _from, to, filter=filter)

Field statistics for a query using an absolute timerange.

Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
field = graylog.Object() # Object | Message field of numeric type to return statistics for
query = graylog.Object() # Object | Query (Lucene syntax)
_from = graylog.Object() # Object | Timerange start. See search method description for date format
to = graylog.Object() # Object | Timerange end. See search method description for date format
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Field statistics for a query using an absolute timerange.
    api_response = api_instance.stats_absolute(field, query, _from, to, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->stats_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of numeric type to return statistics for | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **_from** | [**Object**](.md)| Timerange start. See search method description for date format | 
 **to** | [**Object**](.md)| Timerange end. See search method description for date format | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**FieldStatsResult**](FieldStatsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_absolute**
> TermsResult terms_absolute(field, query, _from, to, size=size, filter=filter)

Most common field terms of a query using an absolute timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
field = graylog.Object() # Object | Message field of to return terms of
query = graylog.Object() # Object | Query (Lucene syntax)
_from = graylog.Object() # Object | Timerange start. See search method description for date format
to = graylog.Object() # Object | Timerange end. See search method description for date format
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Most common field terms of a query using an absolute timerange.
    api_response = api_instance.terms_absolute(field, query, _from, to, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->terms_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of to return terms of | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **_from** | [**Object**](.md)| Timerange start. See search method description for date format | 
 **to** | [**Object**](.md)| Timerange end. See search method description for date format | 
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

# **terms_stats_absolute**
> TermsStatsResult terms_stats_absolute(key_field, value_field, order, query, _from, to, size=size, filter=filter)

Ordered field terms of a query computed on another field using an absolute timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalabsoluteApi()
key_field = graylog.Object() # Object | Message field of to return terms of
value_field = graylog.Object() # Object | Value field used for computation
order = graylog.Object() # Object | What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)
query = graylog.Object() # Object | Query (Lucene syntax)
_from = graylog.Object() # Object | Timerange start. See search method description for date format
to = graylog.Object() # Object | Timerange end. See search method description for date format
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Ordered field terms of a query computed on another field using an absolute timerange.
    api_response = api_instance.terms_stats_absolute(key_field, value_field, order, query, _from, to, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalabsoluteApi->terms_stats_absolute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_field** | [**Object**](.md)| Message field of to return terms of | 
 **value_field** | [**Object**](.md)| Value field used for computation | 
 **order** | [**Object**](.md)| What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **_from** | [**Object**](.md)| Timerange start. See search method description for date format | 
 **to** | [**Object**](.md)| Timerange end. See search method description for date format | 
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

