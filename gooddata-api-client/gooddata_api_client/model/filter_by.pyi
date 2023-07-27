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


class FilterBy(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies what is used for filtering.
    """


    class MetaOapg:
        required = {
            "labelType",
        }
        
        class properties:
            
            
            class labelType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRIMARY(cls):
                    return cls("PRIMARY")
                
                @schemas.classproperty
                def REQUESTED(cls):
                    return cls("REQUESTED")
            __annotations__ = {
                "labelType": labelType,
            }
    
    labelType: MetaOapg.properties.labelType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labelType"]) -> MetaOapg.properties.labelType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["labelType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labelType"]) -> MetaOapg.properties.labelType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["labelType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        labelType: typing.Union[MetaOapg.properties.labelType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilterBy':
        return super().__new__(
            cls,
            *_args,
            labelType=labelType,
            _configuration=_configuration,
            **kwargs,
        )
