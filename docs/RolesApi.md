# graylog.RolesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](RolesApi.md#add_member) | **PUT** /roles/{rolename}/members/{username} | Add a user to a role
[**create**](RolesApi.md#create) | **POST** /roles | Create a new role
[**delete**](RolesApi.md#delete) | **DELETE** /roles/{rolename} | Remove the named role and dissociate any users from it
[**get_members**](RolesApi.md#get_members) | **GET** /roles/{rolename}/members | Retrieve the role&#39;s members
[**list_all**](RolesApi.md#list_all) | **GET** /roles | List all roles
[**read**](RolesApi.md#read) | **GET** /roles/{rolename} | Retrieve permissions for a single role
[**remove_member**](RolesApi.md#remove_member) | **DELETE** /roles/{rolename}/members/{username} | Remove a user from a role
[**update**](RolesApi.md#update) | **PUT** /roles/{rolename} | Update an existing role


# **add_member**
> add_member(rolename, username, json_body=json_body)

Add a user to a role



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 
username = graylog.Object() # Object | 
json_body = 'json_body_example' # String | Placeholder because PUT requests should have a body. Set to '{}', the content will be ignored. (optional)

try: 
    # Add a user to a role
    api_instance.add_member(rolename, username, json_body=json_body)
except ApiException as e:
    print "Exception when calling RolesApi->add_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 
 **username** | [**Object**](.md)|  | 
 **json_body** | [**String**](String.md)| Placeholder because PUT requests should have a body. Set to &#39;{}&#39;, the content will be ignored. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> create(json_body)

Create a new role



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
json_body = graylog.RoleResponse() # RoleResponse | The new role to create

try: 
    # Create a new role
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling RolesApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**RoleResponse**](RoleResponse.md)| The new role to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(rolename)

Remove the named role and dissociate any users from it



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 

try: 
    # Remove the named role and dissociate any users from it
    api_instance.delete(rolename)
except ApiException as e:
    print "Exception when calling RolesApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members**
> RoleMembershipResponse get_members(rolename)

Retrieve the role's members



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 

try: 
    # Retrieve the role's members
    api_response = api_instance.get_members(rolename)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->get_members: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 

### Return type

[**RoleMembershipResponse**](RoleMembershipResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all**
> RolesResponse list_all()

List all roles



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()

try: 
    # List all roles
    api_response = api_instance.list_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->list_all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> RoleResponse read(rolename)

Retrieve permissions for a single role



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 

try: 
    # Retrieve permissions for a single role
    api_response = api_instance.read(rolename)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->read: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member**
> remove_member(rolename, username)

Remove a user from a role



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 
username = graylog.Object() # Object | 

try: 
    # Remove a user from a role
    api_instance.remove_member(rolename, username)
except ApiException as e:
    print "Exception when calling RolesApi->remove_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 
 **username** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> RoleResponse update(rolename, json_body)

Update an existing role



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.RolesApi()
rolename = graylog.Object() # Object | 
json_body = graylog.RoleResponse() # RoleResponse | The new representation of the role

try: 
    # Update an existing role
    api_response = api_instance.update(rolename, json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->update: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rolename** | [**Object**](.md)|  | 
 **json_body** | [**RoleResponse**](RoleResponse.md)| The new representation of the role | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

