# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/show/gateway/v1/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.broadcast.message.main import native_pb2 as bilibili_dot_broadcast_dot_message_dot_main_dot_native__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*bilibili/app/show/gateway/v1/service.proto\x12\x1c\x62ilibili.app.show.gateway.v1\x1a,bilibili/broadcast/message/main/native.proto\"0\n\x11GetActProgressReq\x12\x0e\n\x06pageID\x18\x01 \x01(\x03\x12\x0b\n\x03mid\x18\x02 \x01(\x03\"V\n\x13GetActProgressReply\x12?\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x30.bilibili.broadcast.message.main.NativePageEvent2\x7f\n\x07\x41ppShow\x12t\n\x0eGetActProgress\x12/.bilibili.app.show.gateway.v1.GetActProgressReq\x1a\x31.bilibili.app.show.gateway.v1.GetActProgressReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.show.gateway.v1.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETACTPROGRESSREQ._serialized_start=122
  _GETACTPROGRESSREQ._serialized_end=170
  _GETACTPROGRESSREPLY._serialized_start=172
  _GETACTPROGRESSREPLY._serialized_end=258
  _APPSHOW._serialized_start=260
  _APPSHOW._serialized_end=387
# @@protoc_insertion_point(module_scope)
