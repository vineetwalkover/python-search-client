# universal_search_engine.SearchApi

All URIs are relative to *https://search-engine-walkover.el.r.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_index**](SearchApi.md#add_index) | **POST** /addIndexByApi | Add Index By Api
[**add_object**](SearchApi.md#add_object) | **POST** /add/{index_name} | This will add an object to the given index.
[**add_objects**](SearchApi.md#add_objects) | **POST** /bulkadd/{index_name} | This will add an array of objects to the given index.
[**copy_index_config**](SearchApi.md#copy_index_config) | **POST** /copyIndexConfig | Copy Index configuration from one index to another
[**delete_index**](SearchApi.md#delete_index) | **DELETE** /deleteIndexByApi | Delete Index
[**delete_object**](SearchApi.md#delete_object) | **DELETE** /delete/{index_name} | This will delete the object with given object id
[**generate_event**](SearchApi.md#generate_event) | **POST** /event/{index_name} | This will generate an event.
[**get_all_objects**](SearchApi.md#get_all_objects) | **POST** /getAllObjects | Get All objects stored in index
[**search_query**](SearchApi.md#search_query) | **POST** /search/{index_name} | 


# **add_index**
> object add_index(name, type, api_key)

Add Index By Api

Add Index by Api, provide name and type for creating new index

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
name = 'name_example' # str | name of index to be created
type = 'type_example' # str | type of index, should be Simple_Search or Ecommerce
api_key = 'api_key_example' # str | API_KEY for authentication

try:
    # Add Index By Api
    api_response = api_instance.add_index(name, type, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->add_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of index to be created | 
 **type** | **str**| type of index, should be Simple_Search or Ecommerce | 
 **api_key** | **str**| API_KEY for authentication | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_object**
> object add_object(index_name, api_key, object)

This will add an object to the given index.

It rquire a json object which we want to add.

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index_name = 'index_name_example' # str | name of index
api_key = 'api_key_example' # str | API_KEY for authentication
object = NULL # object | This is the single object to be add in index.

try:
    # This will add an object to the given index.
    api_response = api_instance.add_object(index_name, api_key, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->add_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| name of index | 
 **api_key** | **str**| API_KEY for authentication | 
 **object** | [**object**](object.md)| This is the single object to be add in index. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_objects**
> object add_objects(index_name, api_key, objects_list)

This will add an array of objects to the given index.

It rquire a json array of objects which we want to add.

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index_name = 'index_name_example' # str | name of index
api_key = 'api_key_example' # str | API_KEY for authentication
objects_list = [universal_search_engine.list[object]()] # list[object] | This is the single object to be add in index.

try:
    # This will add an array of objects to the given index.
    api_response = api_instance.add_objects(index_name, api_key, objects_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->add_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| name of index | 
 **api_key** | **str**| API_KEY for authentication | 
 **objects_list** | **list[object]**| This is the single object to be add in index. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_index_config**
> object copy_index_config(api_key, src, dest)

Copy Index configuration from one index to another

Copy Index Configuration, provide src and dest for copying index configuration

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
api_key = 'api_key_example' # str | API_KEY for authentication
src = 'src_example' # str | Source Index
dest = 'dest_example' # str | Target Index

try:
    # Copy Index configuration from one index to another
    api_response = api_instance.copy_index_config(api_key, src, dest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->copy_index_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API_KEY for authentication | 
 **src** | **str**| Source Index | 
 **dest** | **str**| Target Index | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_index**
> object delete_index(index, api_key)

Delete Index

Delete Index, provide name

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index = 'index_example' # str | name of index to be deleted
api_key = 'api_key_example' # str | API_KEY for authentication

try:
    # Delete Index
    api_response = api_instance.delete_index(index, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->delete_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| name of index to be deleted | 
 **api_key** | **str**| API_KEY for authentication | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> object delete_object(index_name, api_key, object_id)

This will delete the object with given object id

this require an objectID of object to be deleted

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index_name = 'index_name_example' # str | name of index
api_key = 'api_key_example' # str | API_KEY for authentication
object_id = 'object_id_example' # str | objectId of the object to be deleted

try:
    # This will delete the object with given object id
    api_response = api_instance.delete_object(index_name, api_key, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->delete_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| name of index | 
 **api_key** | **str**| API_KEY for authentication | 
 **object_id** | **str**| objectId of the object to be deleted | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_event**
> object generate_event(index_name, api_key, type, object)

This will generate an event.

event type should be provided and it shoulb be click.

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index_name = 'index_name_example' # str | name of index
api_key = 'api_key_example' # str | API_KEY for authentication
type = 'type_example' # str | type of the event
object = universal_search_engine.Object1() # Object1 | This is the single object to be add in index.

try:
    # This will generate an event.
    api_response = api_instance.generate_event(index_name, api_key, type, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->generate_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| name of index | 
 **api_key** | **str**| API_KEY for authentication | 
 **type** | **str**| type of the event | 
 **object** | [**Object1**](Object1.md)| This is the single object to be add in index. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_objects**
> object get_all_objects(index, api_key)

Get All objects stored in index

Get All objects stored in index, limit is 1000

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index = 'index_example' # str | 
api_key = 'api_key_example' # str | API_KEY for authentication

try:
    # Get All objects stored in index
    api_response = api_instance.get_all_objects(index, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_all_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**|  | 
 **api_key** | **str**| API_KEY for authentication | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_query**
> object search_query(index_name, query, api_key, size=size, user_token=user_token, search_parameters=search_parameters)



Returns a list of stuff

### Example
```python
from __future__ import print_function
import time
import universal_search_engine
from universal_search_engine.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = universal_search_engine.SearchApi()
index_name = 'index_name_example' # str | name of index
query = 'query_example' # str | Query to be searched
api_key = 'api_key_example' # str | API KEY for authentication
size = 56 # int | maximum number of results to be returned (optional)
user_token = 'user_token_example' # str | userToken for personalization (optional)
search_parameters = universal_search_engine.SearchParameters() # SearchParameters | The user to create. (optional)

try:
    api_response = api_instance.search_query(index_name, query, api_key, size=size, user_token=user_token, search_parameters=search_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| name of index | 
 **query** | **str**| Query to be searched | 
 **api_key** | **str**| API KEY for authentication | 
 **size** | **int**| maximum number of results to be returned | [optional] 
 **user_token** | **str**| userToken for personalization | [optional] 
 **search_parameters** | [**SearchParameters**](SearchParameters.md)| The user to create. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

