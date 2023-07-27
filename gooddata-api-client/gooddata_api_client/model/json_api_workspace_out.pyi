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


class JsonApiWorkspaceOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    JSON:API representation of workspace entity.
    """


    class MetaOapg:
        required = {
            "id",
            "type",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WORKSPACE(cls):
                    return cls("workspace")
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class description(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class earlyAccess(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class name(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class prefix(
                            schemas.StrSchema
                        ):
                            pass
                        __annotations__ = {
                            "description": description,
                            "earlyAccess": earlyAccess,
                            "name": name,
                            "prefix": prefix,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["earlyAccess"]) -> MetaOapg.properties.earlyAccess: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> MetaOapg.properties.prefix: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "earlyAccess", "name", "prefix", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["earlyAccess"]) -> typing.Union[MetaOapg.properties.earlyAccess, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union[MetaOapg.properties.prefix, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "earlyAccess", "name", "prefix", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                    earlyAccess: typing.Union[MetaOapg.properties.earlyAccess, str, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    prefix: typing.Union[MetaOapg.properties.prefix, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        description=description,
                        earlyAccess=earlyAccess,
                        name=name,
                        prefix=prefix,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class meta(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class config(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "approximateCountAvailable",
                                    "showAllValuesOnDatesAvailable",
                                    "dataSamplingAvailable",
                                }
                                
                                class properties:
                                    approximateCountAvailable = schemas.BoolSchema
                                    dataSamplingAvailable = schemas.BoolSchema
                                    showAllValuesOnDatesAvailable = schemas.BoolSchema
                                    __annotations__ = {
                                        "approximateCountAvailable": approximateCountAvailable,
                                        "dataSamplingAvailable": dataSamplingAvailable,
                                        "showAllValuesOnDatesAvailable": showAllValuesOnDatesAvailable,
                                    }
                            
                            approximateCountAvailable: MetaOapg.properties.approximateCountAvailable
                            showAllValuesOnDatesAvailable: MetaOapg.properties.showAllValuesOnDatesAvailable
                            dataSamplingAvailable: MetaOapg.properties.dataSamplingAvailable
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["approximateCountAvailable"]) -> MetaOapg.properties.approximateCountAvailable: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["dataSamplingAvailable"]) -> MetaOapg.properties.dataSamplingAvailable: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["showAllValuesOnDatesAvailable"]) -> MetaOapg.properties.showAllValuesOnDatesAvailable: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["approximateCountAvailable", "dataSamplingAvailable", "showAllValuesOnDatesAvailable", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["approximateCountAvailable"]) -> MetaOapg.properties.approximateCountAvailable: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["dataSamplingAvailable"]) -> MetaOapg.properties.dataSamplingAvailable: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["showAllValuesOnDatesAvailable"]) -> MetaOapg.properties.showAllValuesOnDatesAvailable: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["approximateCountAvailable", "dataSamplingAvailable", "showAllValuesOnDatesAvailable", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                approximateCountAvailable: typing.Union[MetaOapg.properties.approximateCountAvailable, bool, ],
                                showAllValuesOnDatesAvailable: typing.Union[MetaOapg.properties.showAllValuesOnDatesAvailable, bool, ],
                                dataSamplingAvailable: typing.Union[MetaOapg.properties.dataSamplingAvailable, bool, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'config':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    approximateCountAvailable=approximateCountAvailable,
                                    showAllValuesOnDatesAvailable=showAllValuesOnDatesAvailable,
                                    dataSamplingAvailable=dataSamplingAvailable,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class permissions(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                    
                                    @schemas.classproperty
                                    def MANAGE(cls):
                                        return cls("MANAGE")
                                    
                                    @schemas.classproperty
                                    def ANALYZE(cls):
                                        return cls("ANALYZE")
                                    
                                    @schemas.classproperty
                                    def EXPORT(cls):
                                        return cls("EXPORT")
                                    
                                    @schemas.classproperty
                                    def EXPORT_TABULAR(cls):
                                        return cls("EXPORT_TABULAR")
                                    
                                    @schemas.classproperty
                                    def EXPORT_PDF(cls):
                                        return cls("EXPORT_PDF")
                                    
                                    @schemas.classproperty
                                    def VIEW(cls):
                                        return cls("VIEW")
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'permissions':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "config": config,
                            "permissions": permissions,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["config", "permissions", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config", "permissions", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    permissions: typing.Union[MetaOapg.properties.permissions, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'meta':
                    return super().__new__(
                        cls,
                        *_args,
                        config=config,
                        permissions=permissions,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class parent(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                
                                    @staticmethod
                                    def data() -> typing.Type['JsonApiWorkspaceToOneLinkage']:
                                        return JsonApiWorkspaceToOneLinkage
                                    __annotations__ = {
                                        "data": data,
                                    }
                            
                            data: 'JsonApiWorkspaceToOneLinkage'
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'JsonApiWorkspaceToOneLinkage': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'JsonApiWorkspaceToOneLinkage': ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                data: 'JsonApiWorkspaceToOneLinkage',
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'parent':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "parent": parent,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *_args,
                        parent=parent,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "type": type,
                "attributes": attributes,
                "meta": meta,
                "relationships": relationships,
            }
    
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "attributes", "meta", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union[MetaOapg.properties.meta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "attributes", "meta", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        meta: typing.Union[MetaOapg.properties.meta, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiWorkspaceOut':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            attributes=attributes,
            meta=meta,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.json_api_workspace_to_one_linkage import JsonApiWorkspaceToOneLinkage
