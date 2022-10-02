"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.card.v1.single_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Card(google.protobuf.message.Message):
    """卡片信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SMALL_COVER_V5_FIELD_NUMBER: builtins.int
    LARGE_COVER_V1_FIELD_NUMBER: builtins.int
    THREE_ITEM_ALL_V2_FIELD_NUMBER: builtins.int
    THREE_ITEM_V1_FIELD_NUMBER: builtins.int
    HOT_TOPIC_FIELD_NUMBER: builtins.int
    THREE_ITEM_H_V5_FIELD_NUMBER: builtins.int
    MIDDLE_COVER_V3_FIELD_NUMBER: builtins.int
    LARGE_COVER_V4_FIELD_NUMBER: builtins.int
    POPULAR_TOP_ENTRANCE_FIELD_NUMBER: builtins.int
    RCMD_ONE_ITEM_FIELD_NUMBER: builtins.int
    @property
    def small_cover_v5(self) -> bilibili.app.card.v1.single_pb2.SmallCoverV5:
        """小封面条目"""
    @property
    def large_cover_v1(self) -> bilibili.app.card.v1.single_pb2.LargeCoverV1:
        """"""
    @property
    def three_item_all_v2(self) -> bilibili.app.card.v1.single_pb2.ThreeItemAllV2:
        """"""
    @property
    def three_item_v1(self) -> bilibili.app.card.v1.single_pb2.ThreeItemV1:
        """"""
    @property
    def hot_topic(self) -> bilibili.app.card.v1.single_pb2.HotTopic:
        """"""
    @property
    def three_item_h_v5(self) -> bilibili.app.card.v1.single_pb2.DynamicHot:
        """"""
    @property
    def middle_cover_v3(self) -> bilibili.app.card.v1.single_pb2.MiddleCoverV3:
        """"""
    @property
    def large_cover_v4(self) -> bilibili.app.card.v1.single_pb2.LargeCoverV4:
        """"""
    @property
    def popular_top_entrance(self) -> bilibili.app.card.v1.single_pb2.PopularTopEntrance:
        """热门列表顶部按钮"""
    @property
    def rcmd_one_item(self) -> bilibili.app.card.v1.single_pb2.RcmdOneItem:
        """"""
    def __init__(
        self,
        *,
        small_cover_v5: bilibili.app.card.v1.single_pb2.SmallCoverV5 | None = ...,
        large_cover_v1: bilibili.app.card.v1.single_pb2.LargeCoverV1 | None = ...,
        three_item_all_v2: bilibili.app.card.v1.single_pb2.ThreeItemAllV2 | None = ...,
        three_item_v1: bilibili.app.card.v1.single_pb2.ThreeItemV1 | None = ...,
        hot_topic: bilibili.app.card.v1.single_pb2.HotTopic | None = ...,
        three_item_h_v5: bilibili.app.card.v1.single_pb2.DynamicHot | None = ...,
        middle_cover_v3: bilibili.app.card.v1.single_pb2.MiddleCoverV3 | None = ...,
        large_cover_v4: bilibili.app.card.v1.single_pb2.LargeCoverV4 | None = ...,
        popular_top_entrance: bilibili.app.card.v1.single_pb2.PopularTopEntrance | None = ...,
        rcmd_one_item: bilibili.app.card.v1.single_pb2.RcmdOneItem | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hot_topic", b"hot_topic", "item", b"item", "large_cover_v1", b"large_cover_v1", "large_cover_v4", b"large_cover_v4", "middle_cover_v3", b"middle_cover_v3", "popular_top_entrance", b"popular_top_entrance", "rcmd_one_item", b"rcmd_one_item", "small_cover_v5", b"small_cover_v5", "three_item_all_v2", b"three_item_all_v2", "three_item_h_v5", b"three_item_h_v5", "three_item_v1", b"three_item_v1"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hot_topic", b"hot_topic", "item", b"item", "large_cover_v1", b"large_cover_v1", "large_cover_v4", b"large_cover_v4", "middle_cover_v3", b"middle_cover_v3", "popular_top_entrance", b"popular_top_entrance", "rcmd_one_item", b"rcmd_one_item", "small_cover_v5", b"small_cover_v5", "three_item_all_v2", b"three_item_all_v2", "three_item_h_v5", b"three_item_h_v5", "three_item_v1", b"three_item_v1"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["item", b"item"]) -> typing_extensions.Literal["small_cover_v5", "large_cover_v1", "three_item_all_v2", "three_item_v1", "hot_topic", "three_item_h_v5", "middle_cover_v3", "large_cover_v4", "popular_top_entrance", "rcmd_one_item"] | None: ...

global___Card = Card
