"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FeedModeValue(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value:
        """"""
    def __init__(
        self,
        *,
        value: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

global___FeedModeValue = FeedModeValue

@typing_extensions.final
class PegasusAutoPlay(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SINGLE_FIELD_NUMBER: builtins.int
    DOUBLE_FIELD_NUMBER: builtins.int
    SINGLE_AFFECTED_BY_SERVER_SIDE_FIELD_NUMBER: builtins.int
    DOUBLE_AFFECTED_BY_SERVER_SIDE_FIELD_NUMBER: builtins.int
    @property
    def single(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value:
        """"""
    @property
    def double(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value:
        """"""
    @property
    def single_affected_by_server_side(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """"""
    @property
    def double_affected_by_server_side(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """"""
    def __init__(
        self,
        *,
        single: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value | None = ...,
        double: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value | None = ...,
        single_affected_by_server_side: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
        double_affected_by_server_side: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["double", b"double", "double_affected_by_server_side", b"double_affected_by_server_side", "single", b"single", "single_affected_by_server_side", b"single_affected_by_server_side"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["double", b"double", "double_affected_by_server_side", b"double_affected_by_server_side", "single", b"single", "single_affected_by_server_side", b"single_affected_by_server_side"]) -> None: ...

global___PegasusAutoPlay = PegasusAutoPlay

@typing_extensions.final
class PegasusColumnValue(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    AFFECTED_BY_SERVER_SIDE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value:
        """"""
    @property
    def affected_by_server_side(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """"""
    def __init__(
        self,
        *,
        value: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value | None = ...,
        affected_by_server_side: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["affected_by_server_side", b"affected_by_server_side", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["affected_by_server_side", b"affected_by_server_side", "value", b"value"]) -> None: ...

global___PegasusColumnValue = PegasusColumnValue

@typing_extensions.final
class PegasusDeviceConfig(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLUMN_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    AUTO_PLAY_FIELD_NUMBER: builtins.int
    @property
    def column(self) -> global___PegasusColumnValue:
        """"""
    @property
    def mode(self) -> global___FeedModeValue:
        """"""
    @property
    def auto_play(self) -> global___PegasusAutoPlay:
        """"""
    def __init__(
        self,
        *,
        column: global___PegasusColumnValue | None = ...,
        mode: global___FeedModeValue | None = ...,
        auto_play: global___PegasusAutoPlay | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["auto_play", b"auto_play", "column", b"column", "mode", b"mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_play", b"auto_play", "column", b"column", "mode", b"mode"]) -> None: ...

global___PegasusDeviceConfig = PegasusDeviceConfig