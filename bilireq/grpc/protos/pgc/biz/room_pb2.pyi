"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RoomProto(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROOM_ID_FIELD_NUMBER: builtins.int
    @property
    def room_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """"""
        pass
    def __init__(self,
        *,
        room_id: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["room_id",b"room_id"]) -> None: ...
global___RoomProto = RoomProto
