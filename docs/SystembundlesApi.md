# graylog.SystembundlesApi

All URIs are relative to *http://log.ano.yumimobi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_bundle**](SystembundlesApi.md#apply_bundle) | **POST** /system/bundles/{bundleId}/apply | Set up entities described by content pack
[**create_bundle**](SystembundlesApi.md#create_bundle) | **POST** /system/bundles | Upload a content pack
[**delete_bundle**](SystembundlesApi.md#delete_bundle) | **DELETE** /system/bundles/{bundleId} | Delete content pack
[**export_bundle**](SystembundlesApi.md#export_bundle) | **POST** /system/bundles/export | Export entities as a content pack
[**list_bundles**](SystembundlesApi.md#list_bundles) | **GET** /system/bundles | List available content packs
[**show_bundle**](SystembundlesApi.md#show_bundle) | **GET** /system/bundles/{bundleId} | Show content pack
[**update_bundle**](SystembundlesApi.md#update_bundle) | **PUT** /system/bundles/{bundleId} | Update content pack


# **apply_bundle**
> apply_bundle(bundle_id)

Set up entities described by content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
bundle_id = graylog.Object() # Object | Content pack ID

try: 
    # Set up entities described by content pack
    api_instance.apply_bundle(bundle_id)
except ApiException as e:
    print "Exception when calling SystembundlesApi->apply_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**Object**](.md)| Content pack ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bundle**
> create_bundle(request_body)

Upload a content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
request_body = graylog.ConfigurationBundle() # ConfigurationBundle | Content pack

try: 
    # Upload a content pack
    api_instance.create_bundle(request_body)
except ApiException as e:
    print "Exception when calling SystembundlesApi->create_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**ConfigurationBundle**](ConfigurationBundle.md)| Content pack | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bundle**
> delete_bundle(bundle_id)

Delete content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
bundle_id = graylog.Object() # Object | Content pack ID

try: 
    # Delete content pack
    api_instance.delete_bundle(bundle_id)
except ApiException as e:
    print "Exception when calling SystembundlesApi->delete_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**Object**](.md)| Content pack ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_bundle**
> ConfigurationBundle export_bundle(export_bundle)

Export entities as a content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
export_bundle = graylog.ExportBundle() # ExportBundle | Export content pack

try: 
    # Export entities as a content pack
    api_response = api_instance.export_bundle(export_bundle)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystembundlesApi->export_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_bundle** | [**ExportBundle**](ExportBundle.md)| Export content pack | 

### Return type

[**ConfigurationBundle**](ConfigurationBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bundles**
> Multimap list_bundles()

List available content packs



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()

try: 
    # List available content packs
    api_response = api_instance.list_bundles()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystembundlesApi->list_bundles: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Multimap**](Multimap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_bundle**
> ConfigurationBundle show_bundle(bundle_id)

Show content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
bundle_id = graylog.Object() # Object | Content pack ID

try: 
    # Show content pack
    api_response = api_instance.show_bundle(bundle_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SystembundlesApi->show_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**Object**](.md)| Content pack ID | 

### Return type

[**ConfigurationBundle**](ConfigurationBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bundle**
> update_bundle(bundle_id, request_body)

Update content pack



### Example 
```python
import time
import graylog
from graylog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graylog.SystembundlesApi()
bundle_id = graylog.Object() # Object | Content pack ID
request_body = graylog.ConfigurationBundle() # ConfigurationBundle | Content pack

try: 
    # Update content pack
    api_instance.update_bundle(bundle_id, request_body)
except ApiException as e:
    print "Exception when calling SystembundlesApi->update_bundle: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**Object**](.md)| Content pack ID | 
 **request_body** | [**ConfigurationBundle**](ConfigurationBundle.md)| Content pack | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

