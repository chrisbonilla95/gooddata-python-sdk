# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class JsonApiUserDataFilterIn(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    JSON:API representation of userDataFilter entity.
    """


    class MetaOapg:
        required = {
            "attributes",
            "id",
            "type",
        }
        
        class properties:
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "maql",
                    }
                    
                    class properties:
                        areRelationsValid = schemas.BoolSchema
                        
                        
                        class description(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class maql(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class tags(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'tags':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        
                        
                        class title(
                            schemas.StrSchema
                        ):
                            pass
                        __annotations__ = {
                            "areRelationsValid": areRelationsValid,
                            "description": description,
                            "maql": maql,
                            "tags": tags,
                            "title": title,
                        }
                
                maql: MetaOapg.properties.maql
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["areRelationsValid"]) -> MetaOapg.properties.areRelationsValid: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["maql"]) -> MetaOapg.properties.maql: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["areRelationsValid", "description", "maql", "tags", "title", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["areRelationsValid"]) -> typing.Union[MetaOapg.properties.areRelationsValid, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["maql"]) -> MetaOapg.properties.maql: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["areRelationsValid", "description", "maql", "tags", "title", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    maql: typing.Union[MetaOapg.properties.maql, str, ],
                    areRelationsValid: typing.Union[MetaOapg.properties.areRelationsValid, bool, schemas.Unset] = schemas.unset,
                    description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                    tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
                    title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        maql=maql,
                        areRelationsValid=areRelationsValid,
                        description=description,
                        tags=tags,
                        title=title,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USER_DATA_FILTER(cls):
                    return cls("userDataFilter")
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class user(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                
                                    @staticmethod
                                    def data() -> typing.Type['JsonApiUserToOneLinkage']:
                                        return JsonApiUserToOneLinkage
                                    __annotations__ = {
                                        "data": data,
                                    }
                            
                            data: 'JsonApiUserToOneLinkage'
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserToOneLinkage': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserToOneLinkage': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                data: 'JsonApiUserToOneLinkage',
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'user':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class userGroup(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                
                                    @staticmethod
                                    def data() -> typing.Type['JsonApiUserGroupToOneLinkage']:
                                        return JsonApiUserGroupToOneLinkage
                                    __annotations__ = {
                                        "data": data,
                                    }
                            
                            data: 'JsonApiUserGroupToOneLinkage'
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserGroupToOneLinkage': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserGroupToOneLinkage': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                data: 'JsonApiUserGroupToOneLinkage',
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'userGroup':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "user": user,
                            "userGroup": userGroup,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["userGroup"]) -> MetaOapg.properties.userGroup: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "userGroup", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["userGroup"]) -> typing.Union[MetaOapg.properties.userGroup, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "userGroup", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    user: typing.Union[MetaOapg.properties.user, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    userGroup: typing.Union[MetaOapg.properties.userGroup, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *_args,
                        user=user,
                        userGroup=userGroup,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "attributes": attributes,
                "id": id,
                "type": type,
                "relationships": relationships,
            }
    
    attributes: MetaOapg.properties.attributes
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiUserDataFilterIn':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            id=id,
            type=type,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.json_api_user_group_to_one_linkage import JsonApiUserGroupToOneLinkage
from gooddata_api_client.model.json_api_user_to_one_linkage import JsonApiUserToOneLinkage
