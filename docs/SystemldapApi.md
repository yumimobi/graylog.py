# graylog.SystemldapApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ldap_settings**](SystemldapApi.md#delete_ldap_settings) | **DELETE** /system/ldap/settings | Remove the LDAP configuration
[**get_ldap_settings**](SystemldapApi.md#get_ldap_settings) | **GET** /system/ldap/settings | Get the LDAP configuration if it is configured
[**read_group_mapping**](SystemldapApi.md#read_group_mapping) | **GET** /system/ldap/settings/groups | Get the LDAP group to Graylog role mapping
[**read_groups**](SystemldapApi.md#read_groups) | **GET** /system/ldap/groups | Get the available LDAP groups
[**test_ldap_configuration**](SystemldapApi.md#test_ldap_configuration) | **POST** /system/ldap/test | Test LDAP Configuration
[**update_group_mapping_settings**](SystemldapApi.md#update_group_mapping_settings) | **PUT** /system/ldap/settings/groups | Update the LDAP group to Graylog role mapping
[**update_ldap_settings**](SystemldapApi.md#update_ldap_settings) | **PUT** /system/ldap/settings | Update the LDAP configuration


# **delete_ldap_settings**
> delete_ldap_settings()

Remove the LDAP configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()

try: 
    # Remove the LDAP configuration
    api_instance.delete_ldap_settings()
except ApiException as e:
    print "Exception when calling SystemldapApi->delete_ldap_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_settings**
> LdapSettingsResponse get_ldap_settings()

Get the LDAP configuration if it is configured



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()

try: 
    # Get the LDAP configuration if it is configured
    api_response = api_instance.get_ldap_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemldapApi->get_ldap_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LdapSettingsResponse**](LdapSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_group_mapping**
> Map read_group_mapping()

Get the LDAP group to Graylog role mapping

The return value is a simple hash with keys being the LDAP group names and the values the corresponding Graylog role names.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()

try: 
    # Get the LDAP group to Graylog role mapping
    api_response = api_instance.read_group_mapping()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemldapApi->read_group_mapping: %s\n" % e
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

# **read_groups**
> Set read_groups()

Get the available LDAP groups



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()

try: 
    # Get the available LDAP groups
    api_response = api_instance.read_groups()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemldapApi->read_groups: %s\n" % e
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

# **test_ldap_configuration**
> LdapTestConfigResponse test_ldap_configuration(configuration_to_test)

Test LDAP Configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()
configuration_to_test = graylog.LdapTestConfigRequest() # LdapTestConfigRequest | 

try: 
    # Test LDAP Configuration
    api_response = api_instance.test_ldap_configuration(configuration_to_test)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystemldapApi->test_ldap_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_to_test** | [**LdapTestConfigRequest**](LdapTestConfigRequest.md)|  | 

### Return type

[**LdapTestConfigResponse**](LdapTestConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_mapping_settings**
> update_group_mapping_settings(json_body)

Update the LDAP group to Graylog role mapping

Corresponds directly to the output of GET /system/ldap/settings/groups

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()
json_body = graylog.Map() # Map | A hash in which the keys are the LDAP group names and values is the Graylog role name.

try: 
    # Update the LDAP group to Graylog role mapping
    api_instance.update_group_mapping_settings(json_body)
except ApiException as e:
    print "Exception when calling SystemldapApi->update_group_mapping_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**Map**](Map.md)| A hash in which the keys are the LDAP group names and values is the Graylog role name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_settings**
> update_ldap_settings(json_body)

Update the LDAP configuration



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystemldapApi()
json_body = graylog.LdapSettingsRequest() # LdapSettingsRequest | 

try: 
    # Update the LDAP configuration
    api_instance.update_ldap_settings(json_body)
except ApiException as e:
    print "Exception when calling SystemldapApi->update_ldap_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**LdapSettingsRequest**](LdapSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

