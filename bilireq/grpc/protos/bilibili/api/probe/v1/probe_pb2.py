# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/api/probe/v1/probe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bilibili/api/probe/v1/probe.proto\x12\x15\x62ilibili.api.probe.v1\"\x0b\n\tCodeReply\"\x17\n\x07\x43odeReq\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\"J\n\x14\x44ynamicMessageUpdate\x12\x32\n\x04\x62ody\x18\x01 \x01(\x0b\x32$.bilibili.api.probe.v1.SimpleMessage\"\xd8\x03\n\x08\x45mbedded\x12\x10\n\x08\x62ool_val\x18\x01 \x01(\x08\x12\x11\n\tint32_val\x18\x02 \x01(\x05\x12\x11\n\tint64_val\x18\x03 \x01(\x03\x12\x11\n\tfloat_val\x18\x04 \x01(\x02\x12\x12\n\ndouble_val\x18\x05 \x01(\x01\x12\x12\n\nstring_val\x18\x06 \x01(\t\x12\x1a\n\x12repeated_int32_val\x18\x08 \x03(\x05\x12\x1b\n\x13repeated_string_val\x18\x0c \x03(\t\x12I\n\x0emap_string_val\x18\r \x03(\x0b\x32\x31.bilibili.api.probe.v1.Embedded.MapStringValEntry\x12G\n\rmap_error_val\x18\x0e \x03(\x0b\x32\x30.bilibili.api.probe.v1.Embedded.MapErrorValEntry\x1a\x33\n\x11MapStringValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aW\n\x10MapErrorValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.bilibili.api.probe.v1.ErrorMessage:\x02\x38\x01\"=\n\x0c\x45rrorMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"0\n\nProbeReply\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"&\n\x08ProbeReq\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\r\n\x05\x62uvid\x18\x02 \x01(\t\"H\n\x10ProbeStreamReply\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"/\n\x0eProbeStreamReq\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x10\n\x08sequence\x18\x02 \x01(\x03\"#\n\rProbeSubReply\x12\x12\n\nmessage_id\x18\x01 \x01(\x03\"\x1c\n\x0bProbeSubReq\x12\r\n\x05\x62uvid\x18\x01 \x01(\x03\"w\n\rSimpleMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03num\x18\x02 \x01(\x03\x12\x0c\n\x04lang\x18\x03 \x01(\t\x12\x0c\n\x04\x63\x61te\x18\x04 \x01(\x05\x12\x31\n\x08\x65mbedded\x18\x05 \x01(\x0b\x32\x1f.bilibili.api.probe.v1.Embedded*\\\n\x08\x43\x61tegory\x12\x18\n\x14\x43\x41TEGORY_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43\x41TEGORY_ONE\x10\x01\x12\x10\n\x0c\x43\x41TEGORY_TWO\x10\x02\x12\x12\n\x0e\x43\x41TEGORY_THREE\x10\x03*A\n\x0b\x45rrorReason\x12\x15\n\x11PROBE_UNSPECIFIED\x10\x00\x12\x1b\n\x17PROBE_CATEGORY_NOTFOUND\x10\x01\x32\xd7\x02\n\x05Probe\x12L\n\x08TestCode\x12\x1e.bilibili.api.probe.v1.CodeReq\x1a .bilibili.api.probe.v1.CodeReply\x12M\n\x07TestReq\x12\x1f.bilibili.api.probe.v1.ProbeReq\x1a!.bilibili.api.probe.v1.ProbeReply\x12\\\n\nTestStream\x12%.bilibili.api.probe.v1.ProbeStreamReq\x1a\'.bilibili.api.probe.v1.ProbeStreamReply\x12S\n\x07TestSub\x12\".bilibili.api.probe.v1.ProbeSubReq\x1a$.bilibili.api.probe.v1.ProbeSubReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.api.probe.v1.probe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMBEDDED_MAPSTRINGVALENTRY._options = None
  _EMBEDDED_MAPSTRINGVALENTRY._serialized_options = b'8\001'
  _EMBEDDED_MAPERRORVALENTRY._options = None
  _EMBEDDED_MAPERRORVALENTRY._serialized_options = b'8\001'
  _CATEGORY._serialized_start=1113
  _CATEGORY._serialized_end=1205
  _ERRORREASON._serialized_start=1207
  _ERRORREASON._serialized_end=1272
  _CODEREPLY._serialized_start=60
  _CODEREPLY._serialized_end=71
  _CODEREQ._serialized_start=73
  _CODEREQ._serialized_end=96
  _DYNAMICMESSAGEUPDATE._serialized_start=98
  _DYNAMICMESSAGEUPDATE._serialized_end=172
  _EMBEDDED._serialized_start=175
  _EMBEDDED._serialized_end=647
  _EMBEDDED_MAPSTRINGVALENTRY._serialized_start=507
  _EMBEDDED_MAPSTRINGVALENTRY._serialized_end=558
  _EMBEDDED_MAPERRORVALENTRY._serialized_start=560
  _EMBEDDED_MAPERRORVALENTRY._serialized_end=647
  _ERRORMESSAGE._serialized_start=649
  _ERRORMESSAGE._serialized_end=710
  _PROBEREPLY._serialized_start=712
  _PROBEREPLY._serialized_end=760
  _PROBEREQ._serialized_start=762
  _PROBEREQ._serialized_end=800
  _PROBESTREAMREPLY._serialized_start=802
  _PROBESTREAMREPLY._serialized_end=874
  _PROBESTREAMREQ._serialized_start=876
  _PROBESTREAMREQ._serialized_end=923
  _PROBESUBREPLY._serialized_start=925
  _PROBESUBREPLY._serialized_end=960
  _PROBESUBREQ._serialized_start=962
  _PROBESUBREQ._serialized_end=990
  _SIMPLEMESSAGE._serialized_start=992
  _SIMPLEMESSAGE._serialized_end=1111
  _PROBE._serialized_start=1275
  _PROBE._serialized_end=1618
# @@protoc_insertion_point(module_scope)
