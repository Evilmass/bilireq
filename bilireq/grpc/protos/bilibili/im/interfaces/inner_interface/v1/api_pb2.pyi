"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BanUser(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    uid: builtins.int
    """用户mid"""
    limit: builtins.int
    """封禁业务"""
    time: builtins.int
    """封禁时间"""
    mode: builtins.int
    """模式
    1:add 2:remove
    """
    def __init__(
        self,
        *,
        uid: builtins.int = ...,
        limit: builtins.int = ...,
        time: builtins.int = ...,
        mode: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["limit", b"limit", "mode", b"mode", "time", b"time", "uid", b"uid"]) -> None: ...

global___BanUser = BanUser

@typing_extensions.final
class ReqOpBlacklist(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BAN_USERS_FIELD_NUMBER: builtins.int
    @property
    def ban_users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BanUser]:
        """需要封禁/解封的用户信息"""
    def __init__(
        self,
        *,
        ban_users: collections.abc.Iterable[global___BanUser] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ban_users", b"ban_users"]) -> None: ...

global___ReqOpBlacklist = ReqOpBlacklist

@typing_extensions.final
class RspOpBlacklist(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILED_USERS_FIELD_NUMBER: builtins.int
    @property
    def failed_users(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """"""
    def __init__(
        self,
        *,
        failed_users: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failed_users", b"failed_users"]) -> None: ...

global___RspOpBlacklist = RspOpBlacklist
