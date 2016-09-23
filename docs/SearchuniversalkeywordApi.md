# graylog.SearchuniversalkeywordApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_search_keyword_chunked**](SearchuniversalkeywordApi.md#export_search_keyword_chunked) | **GET** /search/universal/keyword/export | Export message search with keyword as timerange.
[**field_histogram_keyword**](SearchuniversalkeywordApi.md#field_histogram_keyword) | **GET** /search/universal/keyword/fieldhistogram | Datetime histogram of a query using keyword timerange.
[**histogram_keyword**](SearchuniversalkeywordApi.md#histogram_keyword) | **GET** /search/universal/keyword/histogram | Datetime histogram of a query using keyword timerange.
[**search_keyword**](SearchuniversalkeywordApi.md#search_keyword) | **GET** /search/universal/keyword | Message search with keyword as timerange.
[**stats_keyword**](SearchuniversalkeywordApi.md#stats_keyword) | **GET** /search/universal/keyword/stats | Field statistics for a query using a keyword timerange.
[**terms_keyword**](SearchuniversalkeywordApi.md#terms_keyword) | **GET** /search/universal/keyword/terms | Most common field terms of a query using a keyword timerange.
[**terms_stats_relative**](SearchuniversalkeywordApi.md#terms_stats_relative) | **GET** /search/universal/keyword/termsstats | Ordered field terms of a query computed on another field using a keyword timerange.


# **export_search_keyword_chunked**
> export_search_keyword_chunked(query, keyword, fields, limit=limit, offset=offset, filter=filter)

Export message search with keyword as timerange.

Search for messages in a timerange defined by a keyword like \"yesterday\" or \"2 weeks ago to wednesday\".

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
query = graylog.Object() # Object | Query (Lucene syntax)
keyword = graylog.Object() # Object | Range keyword
fields = graylog.Object() # Object | Comma separated list of fields to return
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Export message search with keyword as timerange.
    api_instance.export_search_keyword_chunked(query, keyword, fields, limit=limit, offset=offset, filter=filter)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->export_search_keyword_chunked: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **keyword** | [**Object**](.md)| Range keyword | 
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

# **field_histogram_keyword**
> HistogramResult field_histogram_keyword(query, field, interval, keyword, filter=filter, cardinality=cardinality)

Datetime histogram of a query using keyword timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
query = graylog.Object() # Object | Query (Lucene syntax)
field = graylog.Object() # Object | Field of whose values to get the histogram of
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
keyword = graylog.Object() # Object | Range keyword
filter = graylog.Object() # Object | Filter (optional)
cardinality = graylog.Object() # Object | Calculate the cardinality of the field as well (optional)

try: 
    # Datetime histogram of a query using keyword timerange.
    api_response = api_instance.field_histogram_keyword(query, field, interval, keyword, filter=filter, cardinality=cardinality)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->field_histogram_keyword: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **field** | [**Object**](.md)| Field of whose values to get the histogram of | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **keyword** | [**Object**](.md)| Range keyword | 
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

# **histogram_keyword**
> HistogramResult histogram_keyword(query, interval, keyword, filter=filter)

Datetime histogram of a query using keyword timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
query = graylog.Object() # Object | Query (Lucene syntax)
interval = graylog.Object() # Object | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
keyword = graylog.Object() # Object | Range keyword
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Datetime histogram of a query using keyword timerange.
    api_response = api_instance.histogram_keyword(query, interval, keyword, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->histogram_keyword: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **interval** | [**Object**](.md)| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **keyword** | [**Object**](.md)| Range keyword | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_keyword**
> SearchResponse search_keyword(query, keyword, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)

Message search with keyword as timerange.

Search for messages in a timerange defined by a keyword like \"yesterday\" or \"2 weeks ago to wednesday\".

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
query = graylog.Object() # Object | Query (Lucene syntax)
keyword = graylog.Object() # Object | Range keyword
limit = graylog.Object() # Object | Maximum number of messages to return. (optional)
offset = graylog.Object() # Object | Offset (optional)
filter = graylog.Object() # Object | Filter (optional)
fields = graylog.Object() # Object | Comma separated list of fields to return (optional)
sort = graylog.Object() # Object | Sorting (field:asc / field:desc) (optional)
decorate = graylog.Object() # Object | Run decorators on search result (optional) (default to true)

try: 
    # Message search with keyword as timerange.
    api_response = api_instance.search_keyword(query, keyword, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->search_keyword: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **keyword** | [**Object**](.md)| Range keyword | 
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

# **stats_keyword**
> FieldStatsResult stats_keyword(field, query, keyword, filter=filter)

Field statistics for a query using a keyword timerange.

Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
field = graylog.Object() # Object | Message field of numeric type to return statistics for
query = graylog.Object() # Object | Query (Lucene syntax)
keyword = graylog.Object() # Object | Range keyword
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Field statistics for a query using a keyword timerange.
    api_response = api_instance.stats_keyword(field, query, keyword, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->stats_keyword: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of numeric type to return statistics for | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **keyword** | [**Object**](.md)| Range keyword | 
 **filter** | [**Object**](.md)| Filter | [optional] 

### Return type

[**FieldStatsResult**](FieldStatsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_keyword**
> TermsResult terms_keyword(field, query, keyword, size=size, filter=filter)

Most common field terms of a query using a keyword timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
field = graylog.Object() # Object | Message field of to return terms of
query = graylog.Object() # Object | Query (Lucene syntax)
keyword = graylog.Object() # Object | Range keyword
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Most common field terms of a query using a keyword timerange.
    api_response = api_instance.terms_keyword(field, query, keyword, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->terms_keyword: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Object**](.md)| Message field of to return terms of | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **keyword** | [**Object**](.md)| Range keyword | 
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
> TermsStatsResult terms_stats_relative(key_field, value_field, order, query, keyword, size=size, filter=filter)

Ordered field terms of a query computed on another field using a keyword timerange.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SearchuniversalkeywordApi()
key_field = graylog.Object() # Object | Message field of to return terms of
value_field = graylog.Object() # Object | Value field used for computation
order = graylog.Object() # Object | What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)
query = graylog.Object() # Object | Query (Lucene syntax)
keyword = graylog.Object() # Object | Keyword timeframe
size = graylog.Object() # Object | Maximum number of terms to return (optional)
filter = graylog.Object() # Object | Filter (optional)

try: 
    # Ordered field terms of a query computed on another field using a keyword timerange.
    api_response = api_instance.terms_stats_relative(key_field, value_field, order, query, keyword, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchuniversalkeywordApi->terms_stats_relative: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_field** | [**Object**](.md)| Message field of to return terms of | 
 **value_field** | [**Object**](.md)| Value field used for computation | 
 **order** | [**Object**](.md)| What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) | 
 **query** | [**Object**](.md)| Query (Lucene syntax) | 
 **keyword** | [**Object**](.md)| Keyword timeframe | 
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

