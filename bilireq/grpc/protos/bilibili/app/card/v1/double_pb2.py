# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/card/v1/double.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibili.app.card.v1 import common_pb2 as bilibili_dot_app_dot_card_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bilibili/app/card/v1/double.proto\x12\x14\x62ilibili.app.card.v1\x1a!bilibili/app/card/v1/common.proto\"\xc3\x01\n\x0b\x44oubleCards\x12<\n\x0esmall_cover_v2\x18\x01 \x01(\x0b\x32\".bilibili.app.card.v1.SmallCoverV2H\x00\x12\x34\n\none_pic_v2\x18\x02 \x01(\x0b\x32\x1e.bilibili.app.card.v1.OnePicV2H\x00\x12\x38\n\x0cthree_pic_v2\x18\x03 \x01(\x0b\x32 .bilibili.app.card.v1.ThreePicV2H\x00\x42\x06\n\x04\x43\x61rd\"\xf6\x04\n\x0cSmallCoverV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x11\n\tcover_gif\x18\x02 \x01(\t\x12\x12\n\ncover_blur\x18\x03 \x01(\x05\x12\x19\n\x11\x63over_left_text_1\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x05 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x06 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x07 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\x08 \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\t \x01(\x05\x12$\n\x1c\x63over_right_background_color\x18\n \x01(\t\x12\x10\n\x08subtitle\x18\x0b \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x0c \x01(\t\x12\x13\n\x0brcmd_reason\x18\r \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x0e \x01(\t\x12,\n\x06\x61vatar\x18\x0f \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12\x15\n\rofficial_icon\x18\x10 \x01(\x05\x12\x10\n\x08\x63\x61n_play\x18\x11 \x01(\x05\x12<\n\x11rcmd_reason_style\x18\x12 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12?\n\x14rcmd_reason_style_v2\x18\x13 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x35\n\x0blike_button\x18\x14 \x01(\x0b\x32 .bilibili.app.card.v1.LikeButton\"\xc3\x02\n\x0cSmallCoverV3\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12,\n\x06\x61vatar\x18\x02 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12\x17\n\x0f\x63over_left_text\x18\x03 \x01(\t\x12\x38\n\x12\x63over_right_button\x18\x04 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Button\x12\x13\n\x0brcmd_reason\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x06 \x01(\t\x12\x15\n\rofficial_icon\x18\x07 \x01(\x05\x12\x10\n\x08\x63\x61n_play\x18\x08 \x01(\x05\x12<\n\x11rcmd_reason_style\x18\t \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"e\n\rMiddleCoverV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\r\n\x05ratio\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x04 \x01(\t\"\xbe\x03\n\x0cLargeCoverV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12,\n\x06\x61vatar\x18\x02 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12\r\n\x05\x62\x61\x64ge\x18\x03 \x01(\t\x12\x38\n\x12\x63over_right_button\x18\x04 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Button\x12\x19\n\x11\x63over_left_text_1\x18\x05 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x06 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x07 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x08 \x01(\x05\x12\x13\n\x0brcmd_reason\x18\t \x01(\t\x12\x15\n\rofficial_icon\x18\n \x01(\x05\x12\x10\n\x08\x63\x61n_play\x18\x0b \x01(\x05\x12<\n\x11rcmd_reason_style\x18\x0c \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x10\n\x08show_top\x18\r \x01(\x05\x12\x13\n\x0bshow_bottom\x18\x0e \x01(\x05\"\xa6\x01\n\x0bThreeItemV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x12\n\ntitle_icon\x18\x02 \x01(\x05\x12\x10\n\x08more_uri\x18\x03 \x01(\t\x12\x11\n\tmore_text\x18\x04 \x01(\t\x12\x34\n\x05items\x18\x05 \x03(\x0b\x32%.bilibili.app.card.v1.ThreeItemV2Item\"\xb7\x01\n\x0fThreeItemV2Item\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x17\n\x0f\x63over_left_icon\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65sc_text_1\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65sc_icon_1\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65sc_text_2\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65sc_icon_2\x18\x06 \x01(\x05\x12\r\n\x05\x62\x61\x64ge\x18\x07 \x01(\t\"\x8e\x01\n\x0cSmallCoverV4\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x13\n\x0b\x63over_badge\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x18\n\x10title_right_text\x18\x04 \x01(\t\x12\x17\n\x0ftitle_right_pic\x18\x05 \x01(\x05\"i\n\tTwoItemV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x32\n\x05items\x18\x02 \x03(\x0b\x32#.bilibili.app.card.v1.TwoItemV2Item\"~\n\rTwoItemV2Item\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\r\n\x05\x62\x61\x64ge\x18\x02 \x01(\t\x12\x19\n\x11\x63over_left_text_1\x18\x03 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x04 \x01(\x05\"\x8c\x01\n\tMultiItem\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x10\n\x08more_uri\x18\x02 \x01(\t\x12\x11\n\tmore_text\x18\x03 \x01(\t\x12\x30\n\x05items\x18\x04 \x03(\x0b\x32!.bilibili.app.card.v1.DoubleCards\"\xdc\x03\n\nThreePicV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x12\n\nleft_cover\x18\x02 \x01(\t\x12\x15\n\rright_cover_1\x18\x03 \x01(\t\x12\x15\n\rright_cover_2\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_text_1\x18\x05 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x06 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x07 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x08 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\t \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\n \x01(\x05\x12$\n\x1c\x63over_right_background_color\x18\x0b \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x0c \x01(\t\x12\x13\n\x0brcmd_reason\x18\r \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x0e \x01(\t\x12,\n\x06\x61vatar\x18\x0f \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12<\n\x11rcmd_reason_style\x18\x10 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\xd4\x02\n\x08OnePicV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x19\n\x11\x63over_left_icon_1\x18\x02 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x03 \x01(\t\x12\x18\n\x10\x63over_right_text\x18\x04 \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\x05 \x01(\x05\x12$\n\x1c\x63over_right_background_color\x18\x06 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x07 \x01(\t\x12\x13\n\x0brcmd_reason\x18\x08 \x01(\t\x12,\n\x06\x61vatar\x18\t \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12<\n\x11rcmd_reason_style\x18\n \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\xab\x03\n\x0cLargeCoverV3\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x11\n\tcover_gif\x18\x02 \x01(\t\x12,\n\x06\x61vatar\x18\x03 \x01(\x0b\x32\x1c.bilibili.app.card.v1.Avatar\x12@\n\x15top_rcmd_reason_style\x18\x04 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x43\n\x18\x62ottom_rcmd_reason_style\x18\x05 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12\x19\n\x11\x63over_left_text_1\x18\x06 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x07 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x08 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\t \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\n \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x0b \x01(\t\x12\x15\n\rofficial_icon\x18\x0c \x01(\x05\"\x8b\x03\n\nThreePicV3\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x12\n\nleft_cover\x18\x02 \x01(\t\x12\x15\n\rright_cover_1\x18\x03 \x01(\t\x12\x15\n\rright_cover_2\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_text_1\x18\x05 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x06 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x07 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x08 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\t \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\n \x01(\x05\x12$\n\x1c\x63over_right_background_color\x18\x0b \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x0c \x01(\t\x12<\n\x11rcmd_reason_style\x18\r \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\x91\x02\n\x08OnePicV3\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x19\n\x11\x63over_left_text_1\x18\x02 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x03 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\x04 \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\x05 \x01(\x05\x12$\n\x1c\x63over_right_background_color\x18\x06 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x07 \x01(\t\x12<\n\x11rcmd_reason_style\x18\x08 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"F\n\x0cSmallCoverV7\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\"\xdb\x03\n\x0cSmallCoverV9\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x19\n\x11\x63over_left_text_1\x18\x02 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x03 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x05 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\x06 \x01(\t\x12\x18\n\x10\x63over_right_icon\x18\x07 \x01(\x05\x12\x10\n\x08\x63\x61n_play\x18\x08 \x01(\x05\x12<\n\x11rcmd_reason_style\x18\t \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12$\n\x02up\x18\n \x01(\x0b\x32\x18.bilibili.app.card.v1.Up\x12\x41\n\x16left_cover_badge_style\x18\x0b \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12H\n\x1dleft_bottom_rcmd_reason_style\x18\x0c \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\xe3\x02\n\x14SmallCoverConvergeV2\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x19\n\x11\x63over_left_text_1\x18\x02 \x01(\t\x12\x19\n\x11\x63over_left_icon_1\x18\x03 \x01(\x05\x12\x19\n\x11\x63over_left_text_2\x18\x04 \x01(\t\x12\x19\n\x11\x63over_left_icon_2\x18\x05 \x01(\x05\x12\x18\n\x10\x63over_right_text\x18\x06 \x01(\t\x12\x1c\n\x14\x63over_right_top_text\x18\x07 \x01(\t\x12<\n\x11rcmd_reason_style\x18\x08 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\x12?\n\x14rcmd_reason_style_v2\x18\t \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyle\"\xc0\x01\n\x13SmallChannelSpecial\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1a.bilibili.app.card.v1.Base\x12\x10\n\x08\x62g_cover\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65sc_1\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65sc_2\x18\x04 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x05 \x01(\t\x12>\n\x13rcmd_reason_style_2\x18\x06 \x01(\x0b\x32!.bilibili.app.card.v1.ReasonStyleb\x06proto3')



_DOUBLECARDS = DESCRIPTOR.message_types_by_name['DoubleCards']
_SMALLCOVERV2 = DESCRIPTOR.message_types_by_name['SmallCoverV2']
_SMALLCOVERV3 = DESCRIPTOR.message_types_by_name['SmallCoverV3']
_MIDDLECOVERV2 = DESCRIPTOR.message_types_by_name['MiddleCoverV2']
_LARGECOVERV2 = DESCRIPTOR.message_types_by_name['LargeCoverV2']
_THREEITEMV2 = DESCRIPTOR.message_types_by_name['ThreeItemV2']
_THREEITEMV2ITEM = DESCRIPTOR.message_types_by_name['ThreeItemV2Item']
_SMALLCOVERV4 = DESCRIPTOR.message_types_by_name['SmallCoverV4']
_TWOITEMV2 = DESCRIPTOR.message_types_by_name['TwoItemV2']
_TWOITEMV2ITEM = DESCRIPTOR.message_types_by_name['TwoItemV2Item']
_MULTIITEM = DESCRIPTOR.message_types_by_name['MultiItem']
_THREEPICV2 = DESCRIPTOR.message_types_by_name['ThreePicV2']
_ONEPICV2 = DESCRIPTOR.message_types_by_name['OnePicV2']
_LARGECOVERV3 = DESCRIPTOR.message_types_by_name['LargeCoverV3']
_THREEPICV3 = DESCRIPTOR.message_types_by_name['ThreePicV3']
_ONEPICV3 = DESCRIPTOR.message_types_by_name['OnePicV3']
_SMALLCOVERV7 = DESCRIPTOR.message_types_by_name['SmallCoverV7']
_SMALLCOVERV9 = DESCRIPTOR.message_types_by_name['SmallCoverV9']
_SMALLCOVERCONVERGEV2 = DESCRIPTOR.message_types_by_name['SmallCoverConvergeV2']
_SMALLCHANNELSPECIAL = DESCRIPTOR.message_types_by_name['SmallChannelSpecial']
DoubleCards = _reflection.GeneratedProtocolMessageType('DoubleCards', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLECARDS,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.DoubleCards)
  })
_sym_db.RegisterMessage(DoubleCards)

SmallCoverV2 = _reflection.GeneratedProtocolMessageType('SmallCoverV2', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverV2)
  })
_sym_db.RegisterMessage(SmallCoverV2)

SmallCoverV3 = _reflection.GeneratedProtocolMessageType('SmallCoverV3', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV3,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverV3)
  })
_sym_db.RegisterMessage(SmallCoverV3)

MiddleCoverV2 = _reflection.GeneratedProtocolMessageType('MiddleCoverV2', (_message.Message,), {
  'DESCRIPTOR' : _MIDDLECOVERV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.MiddleCoverV2)
  })
_sym_db.RegisterMessage(MiddleCoverV2)

LargeCoverV2 = _reflection.GeneratedProtocolMessageType('LargeCoverV2', (_message.Message,), {
  'DESCRIPTOR' : _LARGECOVERV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.LargeCoverV2)
  })
_sym_db.RegisterMessage(LargeCoverV2)

ThreeItemV2 = _reflection.GeneratedProtocolMessageType('ThreeItemV2', (_message.Message,), {
  'DESCRIPTOR' : _THREEITEMV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreeItemV2)
  })
_sym_db.RegisterMessage(ThreeItemV2)

ThreeItemV2Item = _reflection.GeneratedProtocolMessageType('ThreeItemV2Item', (_message.Message,), {
  'DESCRIPTOR' : _THREEITEMV2ITEM,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreeItemV2Item)
  })
_sym_db.RegisterMessage(ThreeItemV2Item)

SmallCoverV4 = _reflection.GeneratedProtocolMessageType('SmallCoverV4', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV4,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverV4)
  })
_sym_db.RegisterMessage(SmallCoverV4)

TwoItemV2 = _reflection.GeneratedProtocolMessageType('TwoItemV2', (_message.Message,), {
  'DESCRIPTOR' : _TWOITEMV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.TwoItemV2)
  })
_sym_db.RegisterMessage(TwoItemV2)

TwoItemV2Item = _reflection.GeneratedProtocolMessageType('TwoItemV2Item', (_message.Message,), {
  'DESCRIPTOR' : _TWOITEMV2ITEM,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.TwoItemV2Item)
  })
_sym_db.RegisterMessage(TwoItemV2Item)

MultiItem = _reflection.GeneratedProtocolMessageType('MultiItem', (_message.Message,), {
  'DESCRIPTOR' : _MULTIITEM,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.MultiItem)
  })
_sym_db.RegisterMessage(MultiItem)

ThreePicV2 = _reflection.GeneratedProtocolMessageType('ThreePicV2', (_message.Message,), {
  'DESCRIPTOR' : _THREEPICV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePicV2)
  })
_sym_db.RegisterMessage(ThreePicV2)

OnePicV2 = _reflection.GeneratedProtocolMessageType('OnePicV2', (_message.Message,), {
  'DESCRIPTOR' : _ONEPICV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.OnePicV2)
  })
_sym_db.RegisterMessage(OnePicV2)

LargeCoverV3 = _reflection.GeneratedProtocolMessageType('LargeCoverV3', (_message.Message,), {
  'DESCRIPTOR' : _LARGECOVERV3,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.LargeCoverV3)
  })
_sym_db.RegisterMessage(LargeCoverV3)

ThreePicV3 = _reflection.GeneratedProtocolMessageType('ThreePicV3', (_message.Message,), {
  'DESCRIPTOR' : _THREEPICV3,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.ThreePicV3)
  })
_sym_db.RegisterMessage(ThreePicV3)

OnePicV3 = _reflection.GeneratedProtocolMessageType('OnePicV3', (_message.Message,), {
  'DESCRIPTOR' : _ONEPICV3,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.OnePicV3)
  })
_sym_db.RegisterMessage(OnePicV3)

SmallCoverV7 = _reflection.GeneratedProtocolMessageType('SmallCoverV7', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV7,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverV7)
  })
_sym_db.RegisterMessage(SmallCoverV7)

SmallCoverV9 = _reflection.GeneratedProtocolMessageType('SmallCoverV9', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERV9,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverV9)
  })
_sym_db.RegisterMessage(SmallCoverV9)

SmallCoverConvergeV2 = _reflection.GeneratedProtocolMessageType('SmallCoverConvergeV2', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCOVERCONVERGEV2,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallCoverConvergeV2)
  })
_sym_db.RegisterMessage(SmallCoverConvergeV2)

SmallChannelSpecial = _reflection.GeneratedProtocolMessageType('SmallChannelSpecial', (_message.Message,), {
  'DESCRIPTOR' : _SMALLCHANNELSPECIAL,
  '__module__' : 'bilibili.app.card.v1.double_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.SmallChannelSpecial)
  })
_sym_db.RegisterMessage(SmallChannelSpecial)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOUBLECARDS._serialized_start=95
  _DOUBLECARDS._serialized_end=290
  _SMALLCOVERV2._serialized_start=293
  _SMALLCOVERV2._serialized_end=923
  _SMALLCOVERV3._serialized_start=926
  _SMALLCOVERV3._serialized_end=1249
  _MIDDLECOVERV2._serialized_start=1251
  _MIDDLECOVERV2._serialized_end=1352
  _LARGECOVERV2._serialized_start=1355
  _LARGECOVERV2._serialized_end=1801
  _THREEITEMV2._serialized_start=1804
  _THREEITEMV2._serialized_end=1970
  _THREEITEMV2ITEM._serialized_start=1973
  _THREEITEMV2ITEM._serialized_end=2156
  _SMALLCOVERV4._serialized_start=2159
  _SMALLCOVERV4._serialized_end=2301
  _TWOITEMV2._serialized_start=2303
  _TWOITEMV2._serialized_end=2408
  _TWOITEMV2ITEM._serialized_start=2410
  _TWOITEMV2ITEM._serialized_end=2536
  _MULTIITEM._serialized_start=2539
  _MULTIITEM._serialized_end=2679
  _THREEPICV2._serialized_start=2682
  _THREEPICV2._serialized_end=3158
  _ONEPICV2._serialized_start=3161
  _ONEPICV2._serialized_end=3501
  _LARGECOVERV3._serialized_start=3504
  _LARGECOVERV3._serialized_end=3931
  _THREEPICV3._serialized_start=3934
  _THREEPICV3._serialized_end=4329
  _ONEPICV3._serialized_start=4332
  _ONEPICV3._serialized_end=4605
  _SMALLCOVERV7._serialized_start=4607
  _SMALLCOVERV7._serialized_end=4677
  _SMALLCOVERV9._serialized_start=4680
  _SMALLCOVERV9._serialized_end=5155
  _SMALLCOVERCONVERGEV2._serialized_start=5158
  _SMALLCOVERCONVERGEV2._serialized_end=5513
  _SMALLCHANNELSPECIAL._serialized_start=5516
  _SMALLCHANNELSPECIAL._serialized_end=5708
# @@protoc_insertion_point(module_scope)
