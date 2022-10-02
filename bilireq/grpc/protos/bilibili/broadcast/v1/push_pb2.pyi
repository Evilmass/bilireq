"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _LinkType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LinkTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LinkType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LINK_TYPE_UNKNOWN: _LinkType.ValueType  # 0
    """未知"""
    LINK_TYPE_BANGUMI: _LinkType.ValueType  # 1
    """番剧"""
    LINK_TYPE_VIDEO: _LinkType.ValueType  # 2
    """视频"""
    LINK_TYPE_LIVE: _LinkType.ValueType  # 3
    """直播"""

class LinkType(_LinkType, metaclass=_LinkTypeEnumTypeWrapper):
    """"""

LINK_TYPE_UNKNOWN: LinkType.ValueType  # 0
"""未知"""
LINK_TYPE_BANGUMI: LinkType.ValueType  # 1
"""番剧"""
LINK_TYPE_VIDEO: LinkType.ValueType  # 2
"""视频"""
LINK_TYPE_LIVE: LinkType.ValueType  # 3
"""直播"""
global___LinkType = LinkType

class PageBlackList(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___PageBlackList = PageBlackList

class PageView(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___PageView = PageView

class PushMessageResp(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Biz:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _BizEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PushMessageResp._Biz.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        BIZ_UNKNOWN: PushMessageResp._Biz.ValueType  # 0
        """未知"""
        BIZ_VIDEO: PushMessageResp._Biz.ValueType  # 1
        """视频"""
        BIZ_LIVE: PushMessageResp._Biz.ValueType  # 2
        """直播"""
        BIZ_ACTIVITY: PushMessageResp._Biz.ValueType  # 3
        """活动"""

    class Biz(_Biz, metaclass=_BizEnumTypeWrapper):
        """业务类型"""

    BIZ_UNKNOWN: PushMessageResp.Biz.ValueType  # 0
    """未知"""
    BIZ_VIDEO: PushMessageResp.Biz.ValueType  # 1
    """视频"""
    BIZ_LIVE: PushMessageResp.Biz.ValueType  # 2
    """直播"""
    BIZ_ACTIVITY: PushMessageResp.Biz.ValueType  # 3
    """活动"""

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PushMessageResp._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNKNOWN: PushMessageResp._Type.ValueType  # 0
        """未知"""
        TYPE_DEFAULT: PushMessageResp._Type.ValueType  # 1
        """默认"""
        TYPE_HOT: PushMessageResp._Type.ValueType  # 2
        """热门"""
        TYPE_REALTIME: PushMessageResp._Type.ValueType  # 3
        """实时"""
        TYPE_RECOMMEND: PushMessageResp._Type.ValueType  # 4
        """推荐"""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """消息类型"""

    TYPE_UNKNOWN: PushMessageResp.Type.ValueType  # 0
    """未知"""
    TYPE_DEFAULT: PushMessageResp.Type.ValueType  # 1
    """默认"""
    TYPE_HOT: PushMessageResp.Type.ValueType  # 2
    """热门"""
    TYPE_REALTIME: PushMessageResp.Type.ValueType  # 3
    """实时"""
    TYPE_RECOMMEND: PushMessageResp.Type.ValueType  # 4
    """推荐"""

    class _Position:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PositionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PushMessageResp._Position.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        POS_UNKNOWN: PushMessageResp._Position.ValueType  # 0
        """未知"""
        POS_TOP: PushMessageResp._Position.ValueType  # 1
        """顶部"""

    class Position(_Position, metaclass=_PositionEnumTypeWrapper):
        """展示未知"""

    POS_UNKNOWN: PushMessageResp.Position.ValueType  # 0
    """未知"""
    POS_TOP: PushMessageResp.Position.ValueType  # 1
    """顶部"""

    OLD_TASKID_FIELD_NUMBER: builtins.int
    BIZ_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    IMG_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    EXPIRE_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    PAGE_BLACKLIST_FIELD_NUMBER: builtins.int
    PAGE_VIEW_FIELD_NUMBER: builtins.int
    TARGET_RESOURCE_FIELD_NUMBER: builtins.int
    IMAGE_FRAME_FIELD_NUMBER: builtins.int
    IMAGE_MARKER_FIELD_NUMBER: builtins.int
    IMAGE_POSITION_FIELD_NUMBER: builtins.int
    JOB_FIELD_NUMBER: builtins.int
    old_taskid: builtins.int
    """Deprecated: 推送任务id，使用string"""
    biz: global___PushMessageResp.Biz.ValueType
    """业务
    1:是视频 2:是直播 3:是活动
    """
    type: global___PushMessageResp.Type.ValueType
    """类型
    1:是默认 2:是热门 3:是实时 4:是推荐
    """
    title: builtins.str
    """主标题"""
    summary: builtins.str
    """副标题"""
    img: builtins.str
    """图片地址"""
    link: builtins.str
    """跳转地址"""
    position: global___PushMessageResp.Position.ValueType
    """展示位置，1是顶部"""
    duration: builtins.int
    """展示时长（单位：秒），默认3秒"""
    expire: builtins.int
    """失效时间"""
    taskid: builtins.str
    """推送任务id"""
    @property
    def page_blackList(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PageBlackList]:
        """应用内推送黑名单
        UGC:     ugc-video-detail
        PGC:     pgc-video-detail
        一起看:   pgc-video-detail-theater
        直播:     live-room-detail
        Story:    ugc-video-detail-vertical
        播单黑名单 playlist-video-detail
        """
    @property
    def page_view(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PageView]:
        """预留pvid"""
    @property
    def target_resource(self) -> global___TargetResource:
        """跳转资源"""
    image_frame: builtins.int
    """"""
    image_marker: builtins.int
    """"""
    image_position: builtins.int
    """"""
    job: builtins.int
    """"""
    def __init__(
        self,
        *,
        old_taskid: builtins.int = ...,
        biz: global___PushMessageResp.Biz.ValueType = ...,
        type: global___PushMessageResp.Type.ValueType = ...,
        title: builtins.str = ...,
        summary: builtins.str = ...,
        img: builtins.str = ...,
        link: builtins.str = ...,
        position: global___PushMessageResp.Position.ValueType = ...,
        duration: builtins.int = ...,
        expire: builtins.int = ...,
        taskid: builtins.str = ...,
        page_blackList: collections.abc.Iterable[global___PageBlackList] | None = ...,
        page_view: collections.abc.Iterable[global___PageView] | None = ...,
        target_resource: global___TargetResource | None = ...,
        image_frame: builtins.int = ...,
        image_marker: builtins.int = ...,
        image_position: builtins.int = ...,
        job: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["target_resource", b"target_resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["biz", b"biz", "duration", b"duration", "expire", b"expire", "image_frame", b"image_frame", "image_marker", b"image_marker", "image_position", b"image_position", "img", b"img", "job", b"job", "link", b"link", "old_taskid", b"old_taskid", "page_blackList", b"page_blackList", "page_view", b"page_view", "position", b"position", "summary", b"summary", "target_resource", b"target_resource", "taskid", b"taskid", "title", b"title", "type", b"type"]) -> None: ...

global___PushMessageResp = PushMessageResp

class TargetResource(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ResourceEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    Type: global___LinkType.ValueType
    """直播:   roomid
    UGC:   avid
    PGC:   seasonid
    Story: avid
    举个例子
    Type: LINK_TYPE_BANGUMI (番剧)
    Resource: {"seasonid":"123"}

    Type: LINK_TYPE_VIDEO (视频)
    Resource: {"avid":"123"}

    Type: LINK_TYPE_LIVE (直播)
    Resource: {"roomid":"123"}
    """
    @property
    def Resource(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """"""
    def __init__(
        self,
        *,
        Type: global___LinkType.ValueType = ...,
        Resource: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["Resource", b"Resource", "Type", b"Type"]) -> None: ...

global___TargetResource = TargetResource
