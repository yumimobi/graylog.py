# graylog.SystemsessionsApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**new_session**](SystemsessionsApi.md#new_session) | **POST** /system/sessions | Create a new session
[**terminate_session**](SystemsessionsApi.md#terminate_session) | **DELETE** /system/sessions/{sessionId} | Terminate an existing session
[**validate_session**](SystemsessionsApi.md#validate_session) | **GET** /system/sessions | Validate an existing session


# **new_session**
> SessionResponse new_session(login_request)

Create a new session

This request creates a new session for a user or reactivates an existing session: the equivalent of logging in.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemsessionsApi()
login_request = graylog.SessionCreateRequest() # SessionCreateRequest | Username and credentials

try: 
    # Create a new session
    api_response = api_instance.new_session(login_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemsessionsApi->new_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**SessionCreateRequest**](SessionCreateRequest.md)| Username and credentials | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_session**
> terminate_session(session_id)

Terminate an existing session

Destroys the session with the given ID: the equivalent of logging out.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemsessionsApi()
session_id = graylog.Object() # Object | 

try: 
    # Terminate an existing session
    api_instance.terminate_session(session_id)
except ApiException as e:
    print "Exception when calling SystemsessionsApi->terminate_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_session**
> SessionValidationResponse validate_session()

Validate an existing session

Checks the session with the given ID: returns http status 204 (No Content) if session is valid.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemsessionsApi()

try: 
    # Validate an existing session
    api_response = api_instance.validate_session()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemsessionsApi->validate_session: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionValidationResponse**](SessionValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

