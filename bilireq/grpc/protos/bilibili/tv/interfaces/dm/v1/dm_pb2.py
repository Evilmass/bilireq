# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/tv/interfaces/dm/v1/dm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/tv/interfaces/dm/v1/dm.proto\x12\x1c\x62ilibili.tv.interfaces.dm.v1\"\xc2\x01\n\x0c\x43ommandDmOtt\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\x05\x12\x10\n\x08progress\x18\x08 \x01(\x05\x12\r\n\x05\x63time\x18\t \x01(\t\x12\r\n\x05mtime\x18\n \x01(\t\x12\r\n\x05\x65xtra\x18\x0b \x01(\t\x12\x0e\n\x06id_str\x18\x0c \x01(\t\"Y\n\x12\x43ommandDmsOttReply\x12\x43\n\x0f\x63ommand_dms_ott\x18\x01 \x03(\x0b\x32*.bilibili.tv.interfaces.dm.v1.CommandDmOtt\"9\n\x10\x43ommandDmsOttReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\"L\n\rDanmakuAIFlag\x12;\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32).bilibili.tv.interfaces.dm.v1.DanmakuFlag\"\xd6\x01\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08progress\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x10\n\x08\x66ontsize\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\x0f\n\x07midHash\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\r\n\x05idStr\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"\xcc\x04\n\x18\x44\x61nmuDefaultPlayerConfig\x12)\n!player_danmaku_use_default_config\x18\x01 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12$\n\x1cinline_player_danmaku_switch\x18\x10 \x01(\x08\x12)\n!player_danmaku_senior_mode_switch\x18\x11 \x01(\x05\"\xd3\x05\n\x11\x44\x61nmuPlayerConfig\x12\x1d\n\x15player_danmaku_switch\x18\x01 \x01(\x08\x12\"\n\x1aplayer_danmaku_switch_save\x18\x02 \x01(\x08\x12)\n!player_danmaku_use_default_config\x18\x03 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12&\n\x1eplayer_danmaku_enableblocklist\x18\x10 \x01(\x08\x12$\n\x1cinline_player_danmaku_switch\x18\x11 \x01(\x08\x12$\n\x1cinline_player_danmaku_config\x18\x12 \x01(\x05\x12&\n\x1eplayer_danmaku_ios_switch_save\x18\x13 \x01(\x05\"K\n\x18\x44\x61nmuPlayerDynamicConfig\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\"\xa5\x02\n\x15\x44\x61nmuPlayerViewConfig\x12]\n\x1d\x64\x61nmuku_default_player_config\x18\x01 \x01(\x0b\x32\x36.bilibili.tv.interfaces.dm.v1.DanmuDefaultPlayerConfig\x12N\n\x15\x64\x61nmuku_player_config\x18\x02 \x01(\x0b\x32/.bilibili.tv.interfaces.dm.v1.DanmuPlayerConfig\x12]\n\x1d\x64\x61nmuku_player_dynamic_config\x18\x03 \x03(\x0b\x32\x36.bilibili.tv.interfaces.dm.v1.DanmuPlayerDynamicConfig\"\x99\x01\n\x10\x44mSegMobileReply\x12\x38\n\x05\x65lems\x18\x01 \x03(\x0b\x32).bilibili.tv.interfaces.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12<\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32+.bilibili.tv.interfaces.dm.v1.DanmakuAIFlag\"u\n\x0e\x44mSegMobileReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\x12\x16\n\x0eteenagers_mode\x18\x05 \x01(\x05\x12\x0c\n\x04\x66rom\x18\x06 \x01(\x03\"\xc1\x03\n\x0b\x44mViewReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x35\n\x04mask\x18\x02 \x01(\x0b\x32\'.bilibili.tv.interfaces.dm.v1.VideoMask\x12=\n\x08subtitle\x18\x03 \x01(\x0b\x32+.bilibili.tv.interfaces.dm.v1.VideoSubtitle\x12\x13\n\x0bspecial_dms\x18\x04 \x03(\t\x12@\n\x07\x61i_flag\x18\x05 \x01(\x0b\x32/.bilibili.tv.interfaces.dm.v1.DanmakuFlagConfig\x12J\n\rplayer_config\x18\x06 \x01(\x0b\x32\x33.bilibili.tv.interfaces.dm.v1.DanmuPlayerViewConfig\x12\x16\n\x0esend_box_style\x18\x07 \x01(\x05\x12\r\n\x05\x61llow\x18\x08 \x01(\x08\x12\x11\n\tcheck_box\x18\t \x01(\t\x12\x1a\n\x12\x63heck_box_show_msg\x18\n \x01(\t\x12\x18\n\x10text_placeholder\x18\x0b \x01(\t\x12\x19\n\x11input_placeholder\x18\x0c \x01(\t\"f\n\tDmViewReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x14\n\x0cis_hard_boot\x18\x05 \x01(\x05\x12\x0c\n\x04\x66rom\x18\x06 \x01(\x03\"\x96\x01\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\t\x12\x0b\n\x03lan\x18\x03 \x01(\t\x12\x0f\n\x07lan_doc\x18\x04 \x01(\t\x12\x14\n\x0csubtitle_url\x18\x05 \x01(\t\x12\x36\n\x06\x61uthor\x18\x06 \x01(\x0b\x32&.bilibili.tv.interfaces.dm.v1.UserInfo\"\\\n\x08UserInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0c\n\x04rank\x18\x06 \x01(\x05\"S\n\tVideoMask\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04plat\x18\x02 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08mask_url\x18\x05 \x01(\t\"k\n\rVideoSubtitle\x12\x0b\n\x03lan\x18\x01 \x01(\t\x12\x0e\n\x06lanDoc\x18\x02 \x01(\t\x12=\n\tsubtitles\x18\x03 \x03(\x0b\x32*.bilibili.tv.interfaces.dm.v1.SubtitleItemb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.tv.interfaces.dm.v1.dm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMANDDMOTT._serialized_start=72
  _COMMANDDMOTT._serialized_end=266
  _COMMANDDMSOTTREPLY._serialized_start=268
  _COMMANDDMSOTTREPLY._serialized_end=357
  _COMMANDDMSOTTREQ._serialized_start=359
  _COMMANDDMSOTTREQ._serialized_end=416
  _DANMAKUAIFLAG._serialized_start=418
  _DANMAKUAIFLAG._serialized_end=494
  _DANMAKUELEM._serialized_start=497
  _DANMAKUELEM._serialized_end=711
  _DANMAKUFLAG._serialized_start=713
  _DANMAKUFLAG._serialized_end=754
  _DANMAKUFLAGCONFIG._serialized_start=756
  _DANMAKUFLAGCONFIG._serialized_end=831
  _DANMUDEFAULTPLAYERCONFIG._serialized_start=834
  _DANMUDEFAULTPLAYERCONFIG._serialized_end=1422
  _DANMUPLAYERCONFIG._serialized_start=1425
  _DANMUPLAYERCONFIG._serialized_end=2148
  _DANMUPLAYERDYNAMICCONFIG._serialized_start=2150
  _DANMUPLAYERDYNAMICCONFIG._serialized_end=2225
  _DANMUPLAYERVIEWCONFIG._serialized_start=2228
  _DANMUPLAYERVIEWCONFIG._serialized_end=2521
  _DMSEGMOBILEREPLY._serialized_start=2524
  _DMSEGMOBILEREPLY._serialized_end=2677
  _DMSEGMOBILEREQ._serialized_start=2679
  _DMSEGMOBILEREQ._serialized_end=2796
  _DMVIEWREPLY._serialized_start=2799
  _DMVIEWREPLY._serialized_end=3248
  _DMVIEWREQ._serialized_start=3250
  _DMVIEWREQ._serialized_end=3352
  _SUBTITLEITEM._serialized_start=3355
  _SUBTITLEITEM._serialized_end=3505
  _USERINFO._serialized_start=3507
  _USERINFO._serialized_end=3599
  _VIDEOMASK._serialized_start=3601
  _VIDEOMASK._serialized_end=3684
  _VIDEOSUBTITLE._serialized_start=3686
  _VIDEOSUBTITLE._serialized_end=3793
# @@protoc_insertion_point(module_scope)
