"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PrivacyConfigState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PrivacyConfigStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrivacyConfigState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    close: _PrivacyConfigState.ValueType  # 0
    """关闭"""
    open: _PrivacyConfigState.ValueType  # 1
    """打开"""

class PrivacyConfigState(_PrivacyConfigState, metaclass=_PrivacyConfigStateEnumTypeWrapper):
    """隐私开关状态"""

close: PrivacyConfigState.ValueType  # 0
"""关闭"""
open: PrivacyConfigState.ValueType  # 1
"""打开"""
global___PrivacyConfigState = PrivacyConfigState

class _PrivacyConfigType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PrivacyConfigTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrivacyConfigType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    none: _PrivacyConfigType.ValueType  # 0
    """"""
    dynamic_city: _PrivacyConfigType.ValueType  # 1
    """动态同城"""

class PrivacyConfigType(_PrivacyConfigType, metaclass=_PrivacyConfigTypeEnumTypeWrapper):
    """隐私开关类型"""

none: PrivacyConfigType.ValueType  # 0
""""""
dynamic_city: PrivacyConfigType.ValueType  # 1
"""动态同城"""
global___PrivacyConfigType = PrivacyConfigType

@typing_extensions.final
class NoArgRequest(google.protobuf.message.Message):
    """空请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NoArgRequest = NoArgRequest

@typing_extensions.final
class NoReply(google.protobuf.message.Message):
    """空响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NoReply = NoReply

@typing_extensions.final
class PrivacyConfigItem(google.protobuf.message.Message):
    """隐私设置"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVACY_CONFIG_TYPE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    SUB_TITLE_FIELD_NUMBER: builtins.int
    SUB_TITLE_URI_FIELD_NUMBER: builtins.int
    privacy_config_type: global___PrivacyConfigType.ValueType
    """隐私开关类型"""
    title: builtins.str
    """"""
    state: global___PrivacyConfigState.ValueType
    """隐私开关状态"""
    sub_title: builtins.str
    """"""
    sub_title_uri: builtins.str
    """"""
    def __init__(
        self,
        *,
        privacy_config_type: global___PrivacyConfigType.ValueType = ...,
        title: builtins.str = ...,
        state: global___PrivacyConfigState.ValueType = ...,
        sub_title: builtins.str = ...,
        sub_title_uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["privacy_config_type", b"privacy_config_type", "state", b"state", "sub_title", b"sub_title", "sub_title_uri", b"sub_title_uri", "title", b"title"]) -> None: ...

global___PrivacyConfigItem = PrivacyConfigItem

@typing_extensions.final
class PrivacyConfigReply(google.protobuf.message.Message):
    """获取隐私设置-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVACY_CONFIG_ITEM_FIELD_NUMBER: builtins.int
    @property
    def privacy_config_item(self) -> global___PrivacyConfigItem:
        """隐私设置"""
    def __init__(
        self,
        *,
        privacy_config_item: global___PrivacyConfigItem | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["privacy_config_item", b"privacy_config_item"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["privacy_config_item", b"privacy_config_item"]) -> None: ...

global___PrivacyConfigReply = PrivacyConfigReply

@typing_extensions.final
class SetPrivacyConfigRequest(google.protobuf.message.Message):
    """修改隐私设置-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVACY_CONFIG_TYPE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    privacy_config_type: global___PrivacyConfigType.ValueType
    """隐私开关类型"""
    state: global___PrivacyConfigState.ValueType
    """隐私开关状态"""
    def __init__(
        self,
        *,
        privacy_config_type: global___PrivacyConfigType.ValueType = ...,
        state: global___PrivacyConfigState.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["privacy_config_type", b"privacy_config_type", "state", b"state"]) -> None: ...

global___SetPrivacyConfigRequest = SetPrivacyConfigRequest
