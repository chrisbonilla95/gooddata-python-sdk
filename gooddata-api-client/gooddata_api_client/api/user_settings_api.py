"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_api_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_api_client.model.json_api_user_setting_in_document import JsonApiUserSettingInDocument
from gooddata_api_client.model.json_api_user_setting_out_document import JsonApiUserSettingOutDocument
from gooddata_api_client.model.json_api_user_setting_out_list import JsonApiUserSettingOutList


class UserSettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_entity_user_settings_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiUserSettingOutDocument,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/users/{userId}/userSettings',
                'operation_id': 'create_entity_user_settings',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'json_api_user_setting_in_document',
                ],
                'required': [
                    'user_id',
                    'json_api_user_setting_in_document',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'json_api_user_setting_in_document':
                        (JsonApiUserSettingInDocument,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                },
                'location_map': {
                    'user_id': 'path',
                    'json_api_user_setting_in_document': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [
                    'application/vnd.gooddata.api+json'
                ]
            },
            api_client=api_client
        )
        self.delete_entity_user_settings_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/api/v1/entities/users/{userId}/userSettings/{id}',
                'operation_id': 'delete_entity_user_settings',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'id',
                    'filter',
                ],
                'required': [
                    'user_id',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'id':
                        (str,),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'id': 'id',
                    'filter': 'filter',
                },
                'location_map': {
                    'user_id': 'path',
                    'id': 'path',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_all_entities_user_settings_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiUserSettingOutList,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/users/{userId}/userSettings',
                'operation_id': 'get_all_entities_user_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'filter',
                    'page',
                    'size',
                    'sort',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'filter':
                        (str,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                    'sort':
                        ([str],),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'filter': 'filter',
                    'page': 'page',
                    'size': 'size',
                    'sort': 'sort',
                },
                'location_map': {
                    'user_id': 'path',
                    'filter': 'query',
                    'page': 'query',
                    'size': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'sort': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_entity_user_settings_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiUserSettingOutDocument,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/users/{userId}/userSettings/{id}',
                'operation_id': 'get_entity_user_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'id',
                    'filter',
                ],
                'required': [
                    'user_id',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'id':
                        (str,),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'id': 'id',
                    'filter': 'filter',
                },
                'location_map': {
                    'user_id': 'path',
                    'id': 'path',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_entity_user_settings_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiUserSettingOutDocument,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/users/{userId}/userSettings/{id}',
                'operation_id': 'update_entity_user_settings',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'id',
                    'json_api_user_setting_in_document',
                    'filter',
                ],
                'required': [
                    'user_id',
                    'id',
                    'json_api_user_setting_in_document',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'id':
                        (str,),
                    'json_api_user_setting_in_document':
                        (JsonApiUserSettingInDocument,),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'id': 'id',
                    'filter': 'filter',
                },
                'location_map': {
                    'user_id': 'path',
                    'id': 'path',
                    'json_api_user_setting_in_document': 'body',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [
                    'application/vnd.gooddata.api+json'
                ]
            },
            api_client=api_client
        )

    def create_entity_user_settings(
        self,
        user_id,
        json_api_user_setting_in_document,
        **kwargs
    ):
        """Post new user settings for the user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entity_user_settings(user_id, json_api_user_setting_in_document, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str):
            json_api_user_setting_in_document (JsonApiUserSettingInDocument):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiUserSettingOutDocument
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['user_id'] = \
            user_id
        kwargs['json_api_user_setting_in_document'] = \
            json_api_user_setting_in_document
        return self.create_entity_user_settings_endpoint.call_with_http_info(**kwargs)

    def delete_entity_user_settings(
        self,
        user_id,
        id,
        **kwargs
    ):
        """Delete a setting for a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_entity_user_settings(user_id, id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str):
            id (str):

        Keyword Args:
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['user_id'] = \
            user_id
        kwargs['id'] = \
            id
        return self.delete_entity_user_settings_endpoint.call_with_http_info(**kwargs)

    def get_all_entities_user_settings(
        self,
        user_id,
        **kwargs
    ):
        """List all settings for a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_entities_user_settings(user_id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str):

        Keyword Args:
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            page (int): Zero-based page index (0..N). [optional] if omitted the server will use the default value of 0
            size (int): The size of the page to be returned. [optional] if omitted the server will use the default value of 20
            sort ([str]): Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiUserSettingOutList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['user_id'] = \
            user_id
        return self.get_all_entities_user_settings_endpoint.call_with_http_info(**kwargs)

    def get_entity_user_settings(
        self,
        user_id,
        id,
        **kwargs
    ):
        """Get a setting for a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entity_user_settings(user_id, id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str):
            id (str):

        Keyword Args:
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiUserSettingOutDocument
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['user_id'] = \
            user_id
        kwargs['id'] = \
            id
        return self.get_entity_user_settings_endpoint.call_with_http_info(**kwargs)

    def update_entity_user_settings(
        self,
        user_id,
        id,
        json_api_user_setting_in_document,
        **kwargs
    ):
        """Put new user settings for the user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_entity_user_settings(user_id, id, json_api_user_setting_in_document, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str):
            id (str):
            json_api_user_setting_in_document (JsonApiUserSettingInDocument):

        Keyword Args:
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiUserSettingOutDocument
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['user_id'] = \
            user_id
        kwargs['id'] = \
            id
        kwargs['json_api_user_setting_in_document'] = \
            json_api_user_setting_in_document
        return self.update_entity_user_settings_endpoint.call_with_http_info(**kwargs)

