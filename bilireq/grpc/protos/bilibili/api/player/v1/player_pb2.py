# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/api/player/v1/player.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#bilibili/api/player/v1/player.proto\x12\x16\x62ilibili.api.player.v1\"\x1c\n\x0eHeartbeatReply\x12\n\n\x02ts\x18\x01 \x01(\x03\"\xb8\x04\n\x0cHeartbeatReq\x12\x13\n\x0bserver_time\x18\x01 \x01(\x03\x12\x0f\n\x07session\x18\x02 \x01(\t\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0b\n\x03\x61id\x18\x04 \x01(\x03\x12\x0b\n\x03\x63id\x18\x05 \x01(\x03\x12\x0b\n\x03sid\x18\x06 \x01(\t\x12\x0c\n\x04\x65pid\x18\x07 \x01(\x03\x12\x0c\n\x04type\x18\x08 \x01(\t\x12\x10\n\x08sub_type\x18\t \x01(\x05\x12\x0f\n\x07quality\x18\n \x01(\x05\x12\x12\n\ntotal_time\x18\x0b \x01(\x03\x12\x13\n\x0bpaused_time\x18\x0c \x01(\x03\x12\x13\n\x0bplayed_time\x18\r \x01(\x03\x12\x16\n\x0evideo_duration\x18\x0e \x01(\x03\x12\x11\n\tplay_type\x18\x0f \x01(\t\x12\x14\n\x0cnetwork_type\x18\x10 \x01(\x05\x12\x1f\n\x17last_play_progress_time\x18\x11 \x01(\x03\x12\x1e\n\x16max_play_progress_time\x18\x12 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x13 \x01(\x05\x12\x12\n\nfrom_spmid\x18\x14 \x01(\t\x12\r\n\x05spmid\x18\x15 \x01(\t\x12\x13\n\x0b\x65pid_status\x18\x16 \x01(\t\x12\x13\n\x0bplay_status\x18\x17 \x01(\t\x12\x13\n\x0buser_status\x18\x18 \x01(\t\x12\x1a\n\x12\x61\x63tual_played_time\x18\x19 \x01(\x03\x12\x11\n\tauto_play\x18\x1a \x01(\x05\x12\x16\n\x0elist_play_time\x18\x1b \x01(\x03\x12\x18\n\x10\x64\x65tail_play_time\x18\x1c \x01(\x03\x32\x63\n\tHeartbeat\x12V\n\x06Mobile\x12$.bilibili.api.player.v1.HeartbeatReq\x1a&.bilibili.api.player.v1.HeartbeatReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.api.player.v1.player_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEARTBEATREPLY._serialized_start=63
  _HEARTBEATREPLY._serialized_end=91
  _HEARTBEATREQ._serialized_start=94
  _HEARTBEATREQ._serialized_end=662
  _HEARTBEAT._serialized_start=664
  _HEARTBEAT._serialized_end=763
# @@protoc_insertion_point(module_scope)
