# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/pgc/gateway/player/v3/playurl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.playershared import playershared_pb2 as bilibili_dot_playershared_dot_playershared__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,bilibili/pgc/gateway/player/v3/playurl.proto\x12\x1e\x62ilibili.pgc.gateway.player.v3\x1a(bilibili/playershared/playershared.proto\x1a\x19google/protobuf/any.proto\"\x81\x02\n\x0bPlayViewReq\x12,\n\x03vod\x18\x01 \x01(\x0b\x32\x1f.bilibili.playershared.VideoVod\x12\r\n\x05spmid\x18\x02 \x01(\t\x12\x12\n\nfrom_spmid\x18\x03 \x01(\t\x12\x16\n\x0eteenagers_mode\x18\x04 \x01(\x05\x12T\n\rextra_content\x18\x05 \x03(\x0b\x32=.bilibili.pgc.gateway.player.v3.PlayViewReq.ExtraContentEntry\x1a\x33\n\x11\x45xtraContentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc0\x02\n\rPlayViewReply\x12\x30\n\x08vod_info\x18\x01 \x01(\x0b\x32\x1e.bilibili.playershared.VodInfo\x12\x39\n\rplay_arc_conf\x18\x02 \x01(\x0b\x32\".bilibili.playershared.PlayArcConf\x12(\n\nsupplement\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x08play_arc\x18\x04 \x01(\x0b\x32\x1e.bilibili.playershared.PlayArc\x12\x39\n\rqn_trial_info\x18\x05 \x01(\x0b\x32\".bilibili.playershared.QnTrialInfo\x12+\n\x05\x65vent\x18\x06 \x01(\x0b\x32\x1c.bilibili.playershared.Eventb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.pgc.gateway.player.v3.playurl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYVIEWREQ_EXTRACONTENTENTRY._options = None
  _PLAYVIEWREQ_EXTRACONTENTENTRY._serialized_options = b'8\001'
  _PLAYVIEWREQ._serialized_start=150
  _PLAYVIEWREQ._serialized_end=407
  _PLAYVIEWREQ_EXTRACONTENTENTRY._serialized_start=356
  _PLAYVIEWREQ_EXTRACONTENTENTRY._serialized_end=407
  _PLAYVIEWREPLY._serialized_start=410
  _PLAYVIEWREPLY._serialized_end=730
# @@protoc_insertion_point(module_scope)
