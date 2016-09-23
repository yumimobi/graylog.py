# graylog.MessagesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze**](MessagesApi.md#analyze) | **GET** /messages/{index}/analyze | Analyze a message string
[**parse**](MessagesApi.md#parse) | **POST** /messages/parse | Parse a raw message
[**search**](MessagesApi.md#search) | **GET** /messages/{index}/{messageId} | Get a single message.


# **analyze**
> MessageTokens analyze(index, string)

Analyze a message string

Returns what tokens/terms a message string (message or full_message) is split to.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.MessagesApi()
index = graylog.Object() # Object | The index the message containing the string is stored in.
string = graylog.Object() # Object | The string to analyze.

try: 
    # Analyze a message string
    api_response = api_instance.analyze(index, string)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->analyze: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)| The index the message containing the string is stored in. | 
 **string** | [**Object**](.md)| The string to analyze. | 

### Return type

[**MessageTokens**](MessageTokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse**
> ResultMessage parse(json_body)

Parse a raw message



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.MessagesApi()
json_body = graylog.MessageParseRequest() # MessageParseRequest | 

try: 
    # Parse a raw message
    api_response = api_instance.parse(json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->parse: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**MessageParseRequest**](MessageParseRequest.md)|  | 

### Return type

[**ResultMessage**](ResultMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> ResultMessage search(index, message_id)

Get a single message.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.MessagesApi()
index = graylog.Object() # Object | The index this message is stored in.
message_id = graylog.Object() # Object | 

try: 
    # Get a single message.
    api_response = api_instance.search(index, message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->search: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | [**Object**](.md)| The index this message is stored in. | 
 **message_id** | [**Object**](.md)|  | 

### Return type

[**ResultMessage**](ResultMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

