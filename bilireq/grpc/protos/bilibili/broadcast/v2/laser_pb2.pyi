"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
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
class LaserEventResp(google.protobuf.message.Message):
    """服务端下发Laser事件"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASKID_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    taskid: builtins.int
    """任务id"""
    action: builtins.str
    """指令名"""
    params: builtins.str
    """指令参数json字符串"""
    def __init__(
        self,
        *,
        taskid: builtins.int = ...,
        action: builtins.str = ...,
        params: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "params", b"params", "taskid", b"taskid"]) -> None: ...

global___LaserEventResp = LaserEventResp
