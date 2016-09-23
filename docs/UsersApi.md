# graylog.UsersApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](UsersApi.md#change_password) | **PUT** /users/{username}/password | Update the password for a user.
[**change_user**](UsersApi.md#change_user) | **PUT** /users/{username} | Modify user details.
[**create**](UsersApi.md#create) | **POST** /users | Create a new user account.
[**delete_permissions**](UsersApi.md#delete_permissions) | **DELETE** /users/{username}/permissions | Revoke all permissions for a user without deleting the account.
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{username} | Removes a user account.
[**edit_permissions**](UsersApi.md#edit_permissions) | **PUT** /users/{username}/permissions | Update a user&#39;s permission set.
[**generate_new_token**](UsersApi.md#generate_new_token) | **POST** /users/{username}/tokens/{name} | Generates a new access token for a user
[**get**](UsersApi.md#get) | **GET** /users/{username} | Get user details
[**list_tokens**](UsersApi.md#list_tokens) | **GET** /users/{username}/tokens | Retrieves the list of access tokens for a user
[**list_users**](UsersApi.md#list_users) | **GET** /users | List all users
[**revoke_token**](UsersApi.md#revoke_token) | **DELETE** /users/{username}/tokens/{token} | Removes a token for a user
[**save_preferences**](UsersApi.md#save_preferences) | **PUT** /users/{username}/preferences | Update a user&#39;s preferences set.


# **change_password**
> change_password(username, json_body)

Update the password for a user.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user whose password to change.
json_body = graylog.ChangePasswordRequest() # ChangePasswordRequest | The old and new passwords.

try: 
    # Update the password for a user.
    api_instance.change_password(username, json_body)
except ApiException as e:
    print "Exception when calling UsersApi->change_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user whose password to change. | 
 **json_body** | [**ChangePasswordRequest**](ChangePasswordRequest.md)| The old and new passwords. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user**
> change_user(username, json_body)

Modify user details.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user to modify.
json_body = graylog.ChangeUserRequest() # ChangeUserRequest | Updated user information.

try: 
    # Modify user details.
    api_instance.change_user(username, json_body)
except ApiException as e:
    print "Exception when calling UsersApi->change_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user to modify. | 
 **json_body** | [**ChangeUserRequest**](ChangeUserRequest.md)| Updated user information. | 

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

Create a new user account.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
json_body = graylog.CreateUserRequest() # CreateUserRequest | Must contain username, full_name, email, password and a list of permissions.

try: 
    # Create a new user account.
    api_instance.create(json_body)
except ApiException as e:
    print "Exception when calling UsersApi->create: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_body** | [**CreateUserRequest**](CreateUserRequest.md)| Must contain username, full_name, email, password and a list of permissions. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permissions**
> delete_permissions(username)

Revoke all permissions for a user without deleting the account.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user to modify.

try: 
    # Revoke all permissions for a user without deleting the account.
    api_instance.delete_permissions(username)
except ApiException as e:
    print "Exception when calling UsersApi->delete_permissions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

Removes a user account.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user to delete.

try: 
    # Removes a user account.
    api_instance.delete_user(username)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_permissions**
> edit_permissions(username, json_body)

Update a user's permission set.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user to modify.
json_body = graylog.PermissionEditRequest() # PermissionEditRequest | The list of permissions to assign to the user.

try: 
    # Update a user's permission set.
    api_instance.edit_permissions(username, json_body)
except ApiException as e:
    print "Exception when calling UsersApi->edit_permissions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user to modify. | 
 **json_body** | [**PermissionEditRequest**](PermissionEditRequest.md)| The list of permissions to assign to the user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_new_token**
> Token generate_new_token(username, name, json_body=json_body)

Generates a new access token for a user



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | 
name = graylog.Object() # Object | Descriptive name for this token (e.g. 'cronjob') 
json_body = 'json_body_example' # String | Placeholder because POST requests should have a body. Set to '{}', the content will be ignored. (optional)

try: 
    # Generates a new access token for a user
    api_response = api_instance.generate_new_token(username, name, json_body=json_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->generate_new_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)|  | 
 **name** | [**Object**](.md)| Descriptive name for this token (e.g. &#39;cronjob&#39;)  | 
 **json_body** | [**String**](String.md)| Placeholder because POST requests should have a body. Set to &#39;{}&#39;, the content will be ignored. | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> UserSummary get(username)

Get user details

The user's permissions are only included if a user asks for his own account or for users with the necessary permissions to edit permissions.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The username to return information for.

try: 
    # Get user details
    api_response = api_instance.get(username)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The username to return information for. | 

### Return type

[**UserSummary**](UserSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokens**
> TokenList list_tokens(username)

Retrieves the list of access tokens for a user



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | 

try: 
    # Retrieves the list of access tokens for a user
    api_response = api_instance.list_tokens(username)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->list_tokens: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)|  | 

### Return type

[**TokenList**](TokenList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> UserList list_users()

List all users

The permissions assigned to the users are always included.

### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()

try: 
    # List all users
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->list_users: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserList**](UserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(username, token)

Removes a token for a user



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | 
token = graylog.Object() # Object | 

try: 
    # Removes a token for a user
    api_instance.revoke_token(username, token)
except ApiException as e:
    print "Exception when calling UsersApi->revoke_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)|  | 
 **token** | [**Object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_preferences**
> save_preferences(username, json_body)

Update a user's preferences set.



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.UsersApi()
username = graylog.Object() # Object | The name of the user to modify.
json_body = graylog.UpdateUserPreferences() # UpdateUserPreferences | The map of preferences to assign to the user.

try: 
    # Update a user's preferences set.
    api_instance.save_preferences(username, json_body)
except ApiException as e:
    print "Exception when calling UsersApi->save_preferences: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Object**](.md)| The name of the user to modify. | 
 **json_body** | [**UpdateUserPreferences**](UpdateUserPreferences.md)| The map of preferences to assign to the user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

