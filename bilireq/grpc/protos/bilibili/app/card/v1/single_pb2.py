# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/card/v1/single.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.app.card.v1 import common_pb2 as bilibili_dot_app_dot_card_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bilibili/app/card/v1/single.proto\x12\x14\x62ilibili.app.card.v1\x1a!bilibili/app/card/v1/common.proto\"\xe5\x03\n\x0cSmallCoverV5\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x11\n\tcover_gif\x18\x02 \x01(\t\x12$\n\x02up\x18\x03 \x01(\x0b\x32\x18.bilibili.app.card.v1.Up\x12\x1a\n\x12\x63over_right_text_1\x18\x04 \x01(\t\x12\x14\n\x0cright_desc_1\x18\x05 \x01(\t\x12\x14\n\x0cright_desc_2\x18\x06 \x01(\t\x12<\n\x11rcmd_reason_style\x18\x07 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12?\n\x10hotword_entrance\x18\x08 \x01(\x0b\x32%.bilibili.app.card.v1.HotwordEntrance\x12<\n\x11\x63orner_mark_style\x18\t \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x14\n\x0cright_icon_1\x18\n \x01(\x05\x12\x14\n\x0cright_icon_2\x18\x0b \x01(\x05\x12\x41\n\x16left_corner_mark_style\x18\x0c \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"U\n\x0fHotwordEntrance\x12\x12\n\nhotword_id\x18\x01 \x01(\x03\x12\x10\n\x08hot_text\x18\x02 \x01(\t\x12\x0e\n\x06h5_url\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\"\x9d\x06\n\x0cLargeCoverV1\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x11\n\tcover_gif\x18\x02 \x01(\t\x12,\n\x06\x61vatar\x18\x03 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12\x19\n\x11\x63over_left_text_1\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_text_2\x18\x05 \x01(\t\x12\x19\n\x11\x63over_left_text_3\x18\x06 \x01(\t\x12\x13\n\x0b\x63over_badge\x18\x07 \x01(\t\x12\x17\n\x0ftop_rcmd_reason\x18\x08 \x01(\t\x12\x1a\n\x12\x62ottom_rcmd_reason\x18\t \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\n \x01(\t\x12\x15\n\rofficial_icon\x18\x0b \x01(\x05\x12\x10\n\x08\x63\x61n_play\x18\x0c \x01(\x05\x12@\n\x15top_rcmd_reason_style\x18\r \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x43\n\x18\x62ottom_rcmd_reason_style\x18\x0e \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12?\n\x14rcmd_reason_style_v2\x18\x0f \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x41\n\x16left_cover_badge_style\x18\x10 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x42\n\x17right_cover_badge_style\x18\x11 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x15\n\rcover_badge_2\x18\x12 \x01(\t\x12\x35\n\x0blike_button\x18\x13 \x01(\x0b\x32 .bilibili.app.card.v1.LikeButton\x12\x19\n\x11title_single_line\x18\x14 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\x15 \x01(\t\"\xb0\x01\n\x0eThreeItemAllV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12@\n\x15top_rcmd_reason_style\x18\x02 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x32\n\x04item\x18\x03 \x03(\x0b\x32$.bilibili.app.card.v1.TwoItemHV1Item\"\xd2\x01\n\x0eTwoItemHV1Item\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05\x63over\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\r\n\x05param\x18\x04 \x01(\t\x12(\n\x04\x61rgs\x18\x05 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Args\x12\x0c\n\x04goto\x18\x06 \x01(\t\x12\x19\n\x11\x63over_left_text_1\x18\x07 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x08 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\t \x01(\t\"\xae\x01\n\x0bRcmdOneItem\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12=\n\x12topRcmdReasonStyle\x18\x02 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x36\n\x04item\x18\x03 \x01(\x0b\x32(.bilibili.app.card.v1.SmallCoverRcmdItem\"\xd7\x01\n\x12SmallCoverRcmdItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05\x63over\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\r\n\x05param\x18\x04 \x01(\t\x12\x0c\n\x04goto\x18\x05 \x01(\t\x12\x17\n\x0f\x63overRightText1\x18\x06 \x01(\t\x12\x12\n\nrightDesc1\x18\x07 \x01(\t\x12\x12\n\nrightDesc2\x18\x08 \x01(\t\x12\x10\n\x08\x63overGif\x18\t \x01(\t\x12\x12\n\nrightIcon1\x18\n \x01(\x05\x12\x12\n\nrightIcon2\x18\x0b \x01(\x05\"\xa3\x01\n\x0bThreeItemV1\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x11\n\ttitleIcon\x18\x02 \x01(\x05\x12\x0f\n\x07moreUri\x18\x03 \x01(\t\x12\x10\n\x08moreText\x18\x04 \x01(\t\x12\x34\n\x05items\x18\x05 \x03(\x0b\x32%.bilibili.app.card.v1.ThreeItemV1Item\"\x96\x01\n\x0fThreeItemV1Item\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x15\n\rcoverLeftText\x18\x02 \x01(\t\x12\x15\n\rcoverLeftIcon\x18\x03 \x01(\x05\x12\r\n\x05\x64\x65sc1\x18\x04 \x01(\t\x12\r\n\x05\x64\x65sc2\x18\x05 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x06 \x01(\t\"G\n\x0cHotTopicItem\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05param\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"u\n\x08HotTopic\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x31\n\x05items\x18\x03 \x03(\x0b\x32\".bilibili.app.card.v1.HotTopicItem\"\xfd\x01\n\nDynamicHot\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x16\n\x0etop_left_title\x18\x02 \x01(\t\x12\r\n\x05\x64\x65sc1\x18\x03 \x01(\t\x12\r\n\x05\x64\x65sc2\x18\x04 \x01(\t\x12\x10\n\x08more_uri\x18\x05 \x01(\t\x12\x11\n\tmore_text\x18\x06 \x01(\t\x12\x0e\n\x06\x63overs\x18\x07 \x03(\t\x12\x18\n\x10\x63over_right_text\x18\x08 \x01(\t\x12@\n\x15top_rcmd_reason_style\x18\t \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\x95\x01\n\rMiddleCoverV3\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\r\n\x05\x64\x65sc1\x18\x02 \x01(\t\x12\r\n\x05\x64\x65sc2\x18\x03 \x01(\t\x12<\n\x11\x63over_badge_style\x18\x04 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\xb8\x02\n\x0cLargeCoverV4\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x19\n\x11\x63over_left_text_1\x18\x02 \x01(\t\x12\x19\n\x11\x63over_left_text_2\x18\x03 \x01(\t\x12\x19\n\x11\x63over_left_text_3\x18\x04 \x01(\t\x12\x13\n\x0b\x63over_badge\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61n_play\x18\x06 \x01(\x05\x12$\n\x02up\x18\x07 \x01(\x0b\x32\x18.bilibili.app.card.v1.Up\x12\x12\n\nshort_link\x18\x08 \x01(\t\x12\x16\n\x0eshare_subtitle\x18\t \x01(\t\x12\x13\n\x0bplay_number\x18\n \x01(\t\x12\x0c\n\x04\x62vid\x18\x0b \x01(\t\x12\x11\n\tsub_param\x18\x0c \x01(\t\"q\n\x12PopularTopEntrance\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x31\n\x05items\x18\x02 \x03(\x0b\x32\".bilibili.app.card.v1.EntranceItem\"\xb3\x01\n\x0c\x45ntranceItem\x12\x0c\n\x04goto\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\tmodule_id\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t\x12\x13\n\x0b\x65ntrance_id\x18\x06 \x01(\x03\x12,\n\x06\x62ubble\x18\x07 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Bubble\x12\x15\n\rentrance_type\x18\x08 \x01(\x05\"@\n\x06\x42ubble\x12\x16\n\x0e\x62ubble_content\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\r\n\x05stime\x18\x03 \x01(\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.card.v1.single_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SMALLCOVERV5._serialized_start=95
  _SMALLCOVERV5._serialized_end=580
  _HOTWORDENTRANCE._serialized_start=582
  _HOTWORDENTRANCE._serialized_end=667
  _LARGECOVERV1._serialized_start=670
  _LARGECOVERV1._serialized_end=1467
  _THREEITEMALLV2._serialized_start=1470
  _THREEITEMALLV2._serialized_end=1646
  _TWOITEMHV1ITEM._serialized_start=1649
  _TWOITEMHV1ITEM._serialized_end=1859
  _RCMDONEITEM._serialized_start=1862
  _RCMDONEITEM._serialized_end=2036
  _SMALLCOVERRCMDITEM._serialized_start=2039
  _SMALLCOVERRCMDITEM._serialized_end=2254
  _THREEITEMV1._serialized_start=2257
  _THREEITEMV1._serialized_end=2420
  _THREEITEMV1ITEM._serialized_start=2423
  _THREEITEMV1ITEM._serialized_end=2573
  _HOTTOPICITEM._serialized_start=2575
  _HOTTOPICITEM._serialized_end=2646
  _HOTTOPIC._serialized_start=2648
  _HOTTOPIC._serialized_end=2765
  _DYNAMICHOT._serialized_start=2768
  _DYNAMICHOT._serialized_end=3021
  _MIDDLECOVERV3._serialized_start=3024
  _MIDDLECOVERV3._serialized_end=3173
  _LARGECOVERV4._serialized_start=3176
  _LARGECOVERV4._serialized_end=3488
  _POPULARTOPENTRANCE._serialized_start=3490
  _POPULARTOPENTRANCE._serialized_end=3603
  _ENTRANCEITEM._serialized_start=3606
  _ENTRANCEITEM._serialized_end=3785
  _BUBBLE._serialized_start=3787
  _BUBBLE._serialized_end=3851
# @@protoc_insertion_point(module_scope)
