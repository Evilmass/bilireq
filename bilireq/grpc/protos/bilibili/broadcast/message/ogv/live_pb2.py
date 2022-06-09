# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/broadcast/message/ogv/live.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bilibili/broadcast/message/ogv/live.proto\x12\x1e\x62ilibili.broadcast.message.ogv\"\x10\n\x0eLiveStartEvent\"\x0e\n\x0cLiveEndEvent\"!\n\x0fLiveOnlineEvent\x12\x0e\n\x06online\x18\x01 \x01(\x03\"`\n\x0fLiveUpdateEvent\x12\x1b\n\x13\x61\x66ter_premiere_type\x18\x01 \x01(\x05\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08progress\x18\x04 \x01(\x03\"\x9c\x02\n\x07\x43MDBody\x12?\n\x05start\x18\x01 \x01(\x0b\x32..bilibili.broadcast.message.ogv.LiveStartEventH\x00\x12\x41\n\temergency\x18\x02 \x01(\x0b\x32,.bilibili.broadcast.message.ogv.LiveEndEventH\x00\x12\x41\n\x06online\x18\x03 \x01(\x0b\x32/.bilibili.broadcast.message.ogv.LiveOnlineEventH\x00\x12\x41\n\x06update\x18\x04 \x01(\x0b\x32/.bilibili.broadcast.message.ogv.LiveUpdateEventH\x00\x42\x07\n\x05\x65ventb\x06proto3')



_LIVESTARTEVENT = DESCRIPTOR.message_types_by_name['LiveStartEvent']
_LIVEENDEVENT = DESCRIPTOR.message_types_by_name['LiveEndEvent']
_LIVEONLINEEVENT = DESCRIPTOR.message_types_by_name['LiveOnlineEvent']
_LIVEUPDATEEVENT = DESCRIPTOR.message_types_by_name['LiveUpdateEvent']
_CMDBODY = DESCRIPTOR.message_types_by_name['CMDBody']
LiveStartEvent = _reflection.GeneratedProtocolMessageType('LiveStartEvent', (_message.Message,), {
  'DESCRIPTOR' : _LIVESTARTEVENT,
  '__module__' : 'bilibili.broadcast.message.ogv.live_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ogv.LiveStartEvent)
  })
_sym_db.RegisterMessage(LiveStartEvent)

LiveEndEvent = _reflection.GeneratedProtocolMessageType('LiveEndEvent', (_message.Message,), {
  'DESCRIPTOR' : _LIVEENDEVENT,
  '__module__' : 'bilibili.broadcast.message.ogv.live_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ogv.LiveEndEvent)
  })
_sym_db.RegisterMessage(LiveEndEvent)

LiveOnlineEvent = _reflection.GeneratedProtocolMessageType('LiveOnlineEvent', (_message.Message,), {
  'DESCRIPTOR' : _LIVEONLINEEVENT,
  '__module__' : 'bilibili.broadcast.message.ogv.live_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ogv.LiveOnlineEvent)
  })
_sym_db.RegisterMessage(LiveOnlineEvent)

LiveUpdateEvent = _reflection.GeneratedProtocolMessageType('LiveUpdateEvent', (_message.Message,), {
  'DESCRIPTOR' : _LIVEUPDATEEVENT,
  '__module__' : 'bilibili.broadcast.message.ogv.live_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ogv.LiveUpdateEvent)
  })
_sym_db.RegisterMessage(LiveUpdateEvent)

CMDBody = _reflection.GeneratedProtocolMessageType('CMDBody', (_message.Message,), {
  'DESCRIPTOR' : _CMDBODY,
  '__module__' : 'bilibili.broadcast.message.ogv.live_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ogv.CMDBody)
  })
_sym_db.RegisterMessage(CMDBody)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIVESTARTEVENT._serialized_start=77
  _LIVESTARTEVENT._serialized_end=93
  _LIVEENDEVENT._serialized_start=95
  _LIVEENDEVENT._serialized_end=109
  _LIVEONLINEEVENT._serialized_start=111
  _LIVEONLINEEVENT._serialized_end=144
  _LIVEUPDATEEVENT._serialized_start=146
  _LIVEUPDATEEVENT._serialized_end=242
  _CMDBODY._serialized_start=245
  _CMDBODY._serialized_end=529
# @@protoc_insertion_point(module_scope)
