# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/interfaces/v1/history.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibili.app.archive.middleware.v1 import preload_pb2 as bilibili_dot_app_dot_archive_dot_middleware_dot_v1_dot_preload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bilibili/app/interfaces/v1/history.proto\x12\x1a\x62ilibili.app.interfaces.v1\x1a\x30\x62ilibili/app/archive/middleware/v1/preload.proto\"\x99\x01\n\x0b\x43\x61rdArticle\x12\x0e\n\x06\x63overs\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x18\n\x10\x64isplayAttention\x18\x04 \x01(\x08\x12\r\n\x05\x62\x61\x64ge\x18\x05 \x01(\t\x12\x36\n\x08relation\x18\x06 \x01(\x0b\x32$.bilibili.app.interfaces.v1.Relation\"Q\n\nCardCheese\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x03\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\x12\x10\n\x08subtitle\x18\x04 \x01(\t\"\xa4\x01\n\x08\x43\x61rdLive\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0b\n\x03tag\x18\x04 \x01(\t\x12\x0e\n\x06ststus\x18\x05 \x01(\x05\x12\x19\n\x11\x64isplay_attention\x18\x06 \x01(\x08\x12\x36\n\x08relation\x18\x07 \x01(\x0b\x32$.bilibili.app.interfaces.v1.Relation\"N\n\x07\x43\x61rdOGV\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x03\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\x12\x10\n\x08subtitle\x18\x04 \x01(\t\"\xbe\x02\n\x07\x43\x61rdUGC\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x03\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0b\n\x03mid\x18\x05 \x01(\x03\x12\x19\n\x11\x64isplay_attention\x18\x06 \x01(\x08\x12\x0b\n\x03\x63id\x18\x07 \x01(\x03\x12\x0c\n\x04page\x18\x08 \x01(\x05\x12\x10\n\x08subtitle\x18\t \x01(\t\x12\x36\n\x08relation\x18\n \x01(\x0b\x32$.bilibili.app.interfaces.v1.Relation\x12\x0c\n\x04\x62vid\x18\x0b \x01(\t\x12\x0e\n\x06videos\x18\x0c \x01(\x03\x12\x12\n\nshort_link\x18\r \x01(\t\x12\x16\n\x0eshare_subtitle\x18\x0e \x01(\t\x12\x0c\n\x04view\x18\x0f \x01(\x03\x12\r\n\x05state\x18\x10 \x01(\x03\"\x1c\n\x08\x43learReq\x12\x10\n\x08\x62usiness\x18\x01 \x01(\t\"$\n\x06\x43ursor\x12\x0b\n\x03max\x18\x01 \x01(\x03\x12\r\n\x05maxTp\x18\x02 \x01(\x05\"\xf1\x03\n\nCursorItem\x12\x37\n\x08\x63\x61rd_ugc\x18\x01 \x01(\x0b\x32#.bilibili.app.interfaces.v1.CardUGCH\x00\x12\x37\n\x08\x63\x61rd_ogv\x18\x02 \x01(\x0b\x32#.bilibili.app.interfaces.v1.CardOGVH\x00\x12?\n\x0c\x63\x61rd_article\x18\x03 \x01(\x0b\x32\'.bilibili.app.interfaces.v1.CardArticleH\x00\x12\x39\n\tcard_live\x18\x04 \x01(\x0b\x32$.bilibili.app.interfaces.v1.CardLiveH\x00\x12=\n\x0b\x63\x61rd_cheese\x18\x05 \x01(\x0b\x32&.bilibili.app.interfaces.v1.CardCheeseH\x00\x12\r\n\x05title\x18\x06 \x01(\t\x12\x0b\n\x03uri\x18\x07 \x01(\t\x12\x0e\n\x06viewAt\x18\x08 \x01(\x03\x12\x0b\n\x03kid\x18\t \x01(\x03\x12\x0b\n\x03oid\x18\n \x01(\x03\x12\x10\n\x08\x62usiness\x18\x0b \x01(\t\x12\n\n\x02tp\x18\x0c \x01(\x05\x12\x32\n\x02\x64t\x18\r \x01(\x0b\x32&.bilibili.app.interfaces.v1.DeviceType\x12\x11\n\thas_share\x18\x0e \x01(\x08\x42\x0b\n\tcard_item\"\xbd\x01\n\x0b\x43ursorReply\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.bilibili.app.interfaces.v1.CursorItem\x12\x32\n\x03tab\x18\x02 \x03(\x0b\x32%.bilibili.app.interfaces.v1.CursorTab\x12\x32\n\x06\x63ursor\x18\x03 \x01(\x0b\x32\".bilibili.app.interfaces.v1.Cursor\x12\x0f\n\x07hasMore\x18\x04 \x01(\x08\"\xdf\x01\n\tCursorReq\x12\x32\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\".bilibili.app.interfaces.v1.Cursor\x12\x10\n\x08\x62usiness\x18\x02 \x01(\t\x12G\n\x0eplayer_preload\x18\x03 \x01(\x0b\x32/.bilibili.app.interfaces.v1.PlayerPreloadParams\x12\x43\n\x0bplayer_args\x18\x04 \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\"J\n\tCursorTab\x12\x10\n\x08\x62usiness\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06router\x18\x03 \x01(\t\x12\r\n\x05\x66ocus\x18\x04 \x01(\x08\"\x9f\x01\n\rCursorV2Reply\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.bilibili.app.interfaces.v1.CursorItem\x12\x32\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\".bilibili.app.interfaces.v1.Cursor\x12\x0f\n\x07hasMore\x18\x03 \x01(\x08\x12\x12\n\nempty_link\x18\x04 \x01(\t\"\xf3\x01\n\x0b\x43ursorV2Req\x12\x32\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\".bilibili.app.interfaces.v1.Cursor\x12\x10\n\x08\x62usiness\x18\x02 \x01(\t\x12G\n\x0eplayer_preload\x18\x03 \x01(\x0b\x32/.bilibili.app.interfaces.v1.PlayerPreloadParams\x12\x43\n\x0bplayer_args\x18\x04 \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\x12\x10\n\x08is_local\x18\x05 \x01(\x08\"B\n\tDeleteReq\x12\x35\n\x08his_info\x18\x01 \x01(\x0b\x32#.bilibili.app.interfaces.v1.HisInfo\"H\n\nDeviceType\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.bilibili.app.interfaces.v1.DT\x12\x0c\n\x04icon\x18\x02 \x01(\t\"(\n\x07HisInfo\x12\x10\n\x08\x62usiness\x18\x01 \x01(\t\x12\x0b\n\x03kid\x18\x02 \x01(\x03\"E\n\x0fHistoryTabReply\x12\x32\n\x03tab\x18\x01 \x03(\x0b\x32%.bilibili.app.interfaces.v1.CursorTab\"m\n\rHistoryTabReq\x12\x10\n\x08\x62usiness\x18\x01 \x01(\t\x12\x39\n\x06source\x18\x02 \x01(\x0e\x32).bilibili.app.interfaces.v1.HistorySource\x12\x0f\n\x07keyword\x18\x03 \x01(\t\"w\n\x12LatestHistoryReply\x12\x35\n\x05items\x18\x01 \x01(\x0b\x32&.bilibili.app.interfaces.v1.CursorItem\x12\r\n\x05scene\x18\x02 \x01(\t\x12\r\n\x05rtime\x18\x03 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x04 \x01(\t\"m\n\x10LatestHistoryReq\x12\x10\n\x08\x62usiness\x18\x01 \x01(\t\x12G\n\x0eplayer_preload\x18\x02 \x01(\x0b\x32/.bilibili.app.interfaces.v1.PlayerPreloadParams\"\t\n\x07NoReply\"!\n\x04Page\x12\n\n\x02pn\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"a\n\x13PlayerPreloadParams\x12\n\n\x02qn\x18\x01 \x01(\x03\x12\r\n\x05\x66nver\x18\x02 \x01(\x03\x12\r\n\x05\x66nval\x18\x03 \x01(\x03\x12\x11\n\tforceHost\x18\x04 \x01(\x03\x12\r\n\x05\x66ourk\x18\x05 \x01(\x03\"B\n\x08Relation\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tis_follow\x18\x02 \x01(\x05\x12\x13\n\x0bis_followed\x18\x03 \x01(\x05\"\x85\x01\n\x0bSearchReply\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.bilibili.app.interfaces.v1.CursorItem\x12\x0f\n\x07hasMore\x18\x02 \x01(\x08\x12.\n\x04page\x18\x03 \x01(\x0b\x32 .bilibili.app.interfaces.v1.Page\":\n\tSearchReq\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\n\n\x02pn\x18\x02 \x01(\x03\x12\x10\n\x08\x62usiness\x18\x03 \x01(\t*S\n\x02\x44T\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05Phone\x10\x01\x12\x07\n\x03Pad\x10\x02\x12\x06\n\x02PC\x10\x03\x12\x06\n\x02TV\x10\x04\x12\x07\n\x03\x43\x61r\x10\x05\x12\x07\n\x03Iot\x10\x06\x12\n\n\x06\x41ndPad\x10\x07*6\n\rHistorySource\x12\x11\n\rhistory_VALUE\x10\x00\x12\x12\n\x0eshopping_VALUE\x10\x01\x32\x9c\x05\n\x07History\x12\x64\n\nHistoryTab\x12).bilibili.app.interfaces.v1.HistoryTabReq\x1a+.bilibili.app.interfaces.v1.HistoryTabReply\x12X\n\x06\x43ursor\x12%.bilibili.app.interfaces.v1.CursorReq\x1a\'.bilibili.app.interfaces.v1.CursorReply\x12^\n\x08\x43ursorV2\x12\'.bilibili.app.interfaces.v1.CursorV2Req\x1a).bilibili.app.interfaces.v1.CursorV2Reply\x12T\n\x06\x44\x65lete\x12%.bilibili.app.interfaces.v1.DeleteReq\x1a#.bilibili.app.interfaces.v1.NoReply\x12X\n\x06Search\x12%.bilibili.app.interfaces.v1.SearchReq\x1a\'.bilibili.app.interfaces.v1.SearchReply\x12R\n\x05\x43lear\x12$.bilibili.app.interfaces.v1.ClearReq\x1a#.bilibili.app.interfaces.v1.NoReply\x12m\n\rLatestHistory\x12,.bilibili.app.interfaces.v1.LatestHistoryReq\x1a..bilibili.app.interfaces.v1.LatestHistoryReplyb\x06proto3')

_DT = DESCRIPTOR.enum_types_by_name['DT']
DT = enum_type_wrapper.EnumTypeWrapper(_DT)
_HISTORYSOURCE = DESCRIPTOR.enum_types_by_name['HistorySource']
HistorySource = enum_type_wrapper.EnumTypeWrapper(_HISTORYSOURCE)
Unknown = 0
Phone = 1
Pad = 2
PC = 3
TV = 4
Car = 5
Iot = 6
AndPad = 7
history_VALUE = 0
shopping_VALUE = 1


_CARDARTICLE = DESCRIPTOR.message_types_by_name['CardArticle']
_CARDCHEESE = DESCRIPTOR.message_types_by_name['CardCheese']
_CARDLIVE = DESCRIPTOR.message_types_by_name['CardLive']
_CARDOGV = DESCRIPTOR.message_types_by_name['CardOGV']
_CARDUGC = DESCRIPTOR.message_types_by_name['CardUGC']
_CLEARREQ = DESCRIPTOR.message_types_by_name['ClearReq']
_CURSOR = DESCRIPTOR.message_types_by_name['Cursor']
_CURSORITEM = DESCRIPTOR.message_types_by_name['CursorItem']
_CURSORREPLY = DESCRIPTOR.message_types_by_name['CursorReply']
_CURSORREQ = DESCRIPTOR.message_types_by_name['CursorReq']
_CURSORTAB = DESCRIPTOR.message_types_by_name['CursorTab']
_CURSORV2REPLY = DESCRIPTOR.message_types_by_name['CursorV2Reply']
_CURSORV2REQ = DESCRIPTOR.message_types_by_name['CursorV2Req']
_DELETEREQ = DESCRIPTOR.message_types_by_name['DeleteReq']
_DEVICETYPE = DESCRIPTOR.message_types_by_name['DeviceType']
_HISINFO = DESCRIPTOR.message_types_by_name['HisInfo']
_HISTORYTABREPLY = DESCRIPTOR.message_types_by_name['HistoryTabReply']
_HISTORYTABREQ = DESCRIPTOR.message_types_by_name['HistoryTabReq']
_LATESTHISTORYREPLY = DESCRIPTOR.message_types_by_name['LatestHistoryReply']
_LATESTHISTORYREQ = DESCRIPTOR.message_types_by_name['LatestHistoryReq']
_NOREPLY = DESCRIPTOR.message_types_by_name['NoReply']
_PAGE = DESCRIPTOR.message_types_by_name['Page']
_PLAYERPRELOADPARAMS = DESCRIPTOR.message_types_by_name['PlayerPreloadParams']
_RELATION = DESCRIPTOR.message_types_by_name['Relation']
_SEARCHREPLY = DESCRIPTOR.message_types_by_name['SearchReply']
_SEARCHREQ = DESCRIPTOR.message_types_by_name['SearchReq']
CardArticle = _reflection.GeneratedProtocolMessageType('CardArticle', (_message.Message,), {
  'DESCRIPTOR' : _CARDARTICLE,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CardArticle)
  })
_sym_db.RegisterMessage(CardArticle)

CardCheese = _reflection.GeneratedProtocolMessageType('CardCheese', (_message.Message,), {
  'DESCRIPTOR' : _CARDCHEESE,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CardCheese)
  })
_sym_db.RegisterMessage(CardCheese)

CardLive = _reflection.GeneratedProtocolMessageType('CardLive', (_message.Message,), {
  'DESCRIPTOR' : _CARDLIVE,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CardLive)
  })
_sym_db.RegisterMessage(CardLive)

CardOGV = _reflection.GeneratedProtocolMessageType('CardOGV', (_message.Message,), {
  'DESCRIPTOR' : _CARDOGV,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CardOGV)
  })
_sym_db.RegisterMessage(CardOGV)

CardUGC = _reflection.GeneratedProtocolMessageType('CardUGC', (_message.Message,), {
  'DESCRIPTOR' : _CARDUGC,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CardUGC)
  })
_sym_db.RegisterMessage(CardUGC)

ClearReq = _reflection.GeneratedProtocolMessageType('ClearReq', (_message.Message,), {
  'DESCRIPTOR' : _CLEARREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.ClearReq)
  })
_sym_db.RegisterMessage(ClearReq)

Cursor = _reflection.GeneratedProtocolMessageType('Cursor', (_message.Message,), {
  'DESCRIPTOR' : _CURSOR,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.Cursor)
  })
_sym_db.RegisterMessage(Cursor)

CursorItem = _reflection.GeneratedProtocolMessageType('CursorItem', (_message.Message,), {
  'DESCRIPTOR' : _CURSORITEM,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorItem)
  })
_sym_db.RegisterMessage(CursorItem)

CursorReply = _reflection.GeneratedProtocolMessageType('CursorReply', (_message.Message,), {
  'DESCRIPTOR' : _CURSORREPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorReply)
  })
_sym_db.RegisterMessage(CursorReply)

CursorReq = _reflection.GeneratedProtocolMessageType('CursorReq', (_message.Message,), {
  'DESCRIPTOR' : _CURSORREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorReq)
  })
_sym_db.RegisterMessage(CursorReq)

CursorTab = _reflection.GeneratedProtocolMessageType('CursorTab', (_message.Message,), {
  'DESCRIPTOR' : _CURSORTAB,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorTab)
  })
_sym_db.RegisterMessage(CursorTab)

CursorV2Reply = _reflection.GeneratedProtocolMessageType('CursorV2Reply', (_message.Message,), {
  'DESCRIPTOR' : _CURSORV2REPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorV2Reply)
  })
_sym_db.RegisterMessage(CursorV2Reply)

CursorV2Req = _reflection.GeneratedProtocolMessageType('CursorV2Req', (_message.Message,), {
  'DESCRIPTOR' : _CURSORV2REQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.CursorV2Req)
  })
_sym_db.RegisterMessage(CursorV2Req)

DeleteReq = _reflection.GeneratedProtocolMessageType('DeleteReq', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.DeleteReq)
  })
_sym_db.RegisterMessage(DeleteReq)

DeviceType = _reflection.GeneratedProtocolMessageType('DeviceType', (_message.Message,), {
  'DESCRIPTOR' : _DEVICETYPE,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.DeviceType)
  })
_sym_db.RegisterMessage(DeviceType)

HisInfo = _reflection.GeneratedProtocolMessageType('HisInfo', (_message.Message,), {
  'DESCRIPTOR' : _HISINFO,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.HisInfo)
  })
_sym_db.RegisterMessage(HisInfo)

HistoryTabReply = _reflection.GeneratedProtocolMessageType('HistoryTabReply', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTABREPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.HistoryTabReply)
  })
_sym_db.RegisterMessage(HistoryTabReply)

HistoryTabReq = _reflection.GeneratedProtocolMessageType('HistoryTabReq', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTABREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.HistoryTabReq)
  })
_sym_db.RegisterMessage(HistoryTabReq)

LatestHistoryReply = _reflection.GeneratedProtocolMessageType('LatestHistoryReply', (_message.Message,), {
  'DESCRIPTOR' : _LATESTHISTORYREPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.LatestHistoryReply)
  })
_sym_db.RegisterMessage(LatestHistoryReply)

LatestHistoryReq = _reflection.GeneratedProtocolMessageType('LatestHistoryReq', (_message.Message,), {
  'DESCRIPTOR' : _LATESTHISTORYREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.LatestHistoryReq)
  })
_sym_db.RegisterMessage(LatestHistoryReq)

NoReply = _reflection.GeneratedProtocolMessageType('NoReply', (_message.Message,), {
  'DESCRIPTOR' : _NOREPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.NoReply)
  })
_sym_db.RegisterMessage(NoReply)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {
  'DESCRIPTOR' : _PAGE,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.Page)
  })
_sym_db.RegisterMessage(Page)

PlayerPreloadParams = _reflection.GeneratedProtocolMessageType('PlayerPreloadParams', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERPRELOADPARAMS,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.PlayerPreloadParams)
  })
_sym_db.RegisterMessage(PlayerPreloadParams)

Relation = _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), {
  'DESCRIPTOR' : _RELATION,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.Relation)
  })
_sym_db.RegisterMessage(Relation)

SearchReply = _reflection.GeneratedProtocolMessageType('SearchReply', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREPLY,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.SearchReply)
  })
_sym_db.RegisterMessage(SearchReply)

SearchReq = _reflection.GeneratedProtocolMessageType('SearchReq', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQ,
  '__module__' : 'bilibili.app.interfaces.v1.history_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.interfaces.v1.SearchReq)
  })
_sym_db.RegisterMessage(SearchReq)

_HISTORY = DESCRIPTOR.services_by_name['History']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DT._serialized_start=3406
  _DT._serialized_end=3489
  _HISTORYSOURCE._serialized_start=3491
  _HISTORYSOURCE._serialized_end=3545
  _CARDARTICLE._serialized_start=123
  _CARDARTICLE._serialized_end=276
  _CARDCHEESE._serialized_start=278
  _CARDCHEESE._serialized_end=359
  _CARDLIVE._serialized_start=362
  _CARDLIVE._serialized_end=526
  _CARDOGV._serialized_start=528
  _CARDOGV._serialized_end=606
  _CARDUGC._serialized_start=609
  _CARDUGC._serialized_end=927
  _CLEARREQ._serialized_start=929
  _CLEARREQ._serialized_end=957
  _CURSOR._serialized_start=959
  _CURSOR._serialized_end=995
  _CURSORITEM._serialized_start=998
  _CURSORITEM._serialized_end=1495
  _CURSORREPLY._serialized_start=1498
  _CURSORREPLY._serialized_end=1687
  _CURSORREQ._serialized_start=1690
  _CURSORREQ._serialized_end=1913
  _CURSORTAB._serialized_start=1915
  _CURSORTAB._serialized_end=1989
  _CURSORV2REPLY._serialized_start=1992
  _CURSORV2REPLY._serialized_end=2151
  _CURSORV2REQ._serialized_start=2154
  _CURSORV2REQ._serialized_end=2397
  _DELETEREQ._serialized_start=2399
  _DELETEREQ._serialized_end=2465
  _DEVICETYPE._serialized_start=2467
  _DEVICETYPE._serialized_end=2539
  _HISINFO._serialized_start=2541
  _HISINFO._serialized_end=2581
  _HISTORYTABREPLY._serialized_start=2583
  _HISTORYTABREPLY._serialized_end=2652
  _HISTORYTABREQ._serialized_start=2654
  _HISTORYTABREQ._serialized_end=2763
  _LATESTHISTORYREPLY._serialized_start=2765
  _LATESTHISTORYREPLY._serialized_end=2884
  _LATESTHISTORYREQ._serialized_start=2886
  _LATESTHISTORYREQ._serialized_end=2995
  _NOREPLY._serialized_start=2997
  _NOREPLY._serialized_end=3006
  _PAGE._serialized_start=3008
  _PAGE._serialized_end=3041
  _PLAYERPRELOADPARAMS._serialized_start=3043
  _PLAYERPRELOADPARAMS._serialized_end=3140
  _RELATION._serialized_start=3142
  _RELATION._serialized_end=3208
  _SEARCHREPLY._serialized_start=3211
  _SEARCHREPLY._serialized_end=3344
  _SEARCHREQ._serialized_start=3346
  _SEARCHREQ._serialized_end=3404
  _HISTORY._serialized_start=3548
  _HISTORY._serialized_end=4216
# @@protoc_insertion_point(module_scope)
