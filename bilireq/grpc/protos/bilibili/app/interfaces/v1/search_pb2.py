# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/interfaces/v1/search.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'bilibili/app/interfaces/v1/search.proto\x12\x1a\x62ilibili.app.interfaces.v1\"R\n\x14SuggestionResult3Req\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x11\n\thighlight\x18\x02 \x01(\x05\x12\x16\n\x0eteenagers_mode\x18\x03 \x01(\x05\"o\n\x16SuggestionResult3Reply\x12\x0f\n\x07trackid\x18\x01 \x01(\t\x12\x34\n\x04list\x18\x02 \x03(\x0b\x32&.bilibili.app.interfaces.v1.ResultItem\x12\x0e\n\x06\x65xpStr\x18\x03 \x01(\t\"\xa1\x04\n\nResultItem\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07keyword\x18\x03 \x01(\t\x12\x10\n\x08position\x18\x04 \x01(\x05\x12\r\n\x05\x63over\x18\x05 \x01(\t\x12\x12\n\ncover_size\x18\x06 \x01(\x01\x12\x10\n\x08sug_type\x18\x07 \x01(\t\x12\x11\n\tterm_type\x18\x08 \x01(\x05\x12\x0c\n\x04goto\x18\t \x01(\t\x12\x0b\n\x03uri\x18\n \x01(\t\x12\x43\n\x0fofficial_verify\x18\x0b \x01(\x0b\x32*.bilibili.app.interfaces.v1.OfficialVerify\x12\r\n\x05param\x18\x0c \x01(\t\x12\x0b\n\x03mid\x18\r \x01(\x03\x12\x0c\n\x04\x66\x61ns\x18\x0e \x01(\x05\x12\r\n\x05level\x18\x0f \x01(\x05\x12\x10\n\x08\x61rchives\x18\x10 \x01(\x05\x12\r\n\x05ptime\x18\x11 \x01(\x03\x12\x18\n\x10season_type_name\x18\x12 \x01(\t\x12\x0c\n\x04\x61rea\x18\x13 \x01(\t\x12\r\n\x05style\x18\x14 \x01(\t\x12\r\n\x05label\x18\x15 \x01(\t\x12\x0e\n\x06rating\x18\x16 \x01(\x01\x12\x0c\n\x04vote\x18\x17 \x01(\x05\x12\x37\n\x06\x62\x61\x64ges\x18\x18 \x03(\x0b\x32\'.bilibili.app.interfaces.v1.ReasonStyle\x12\x0e\n\x06styles\x18\x19 \x01(\t\x12\x11\n\tmodule_id\x18\x1a \x01(\x03\x12\x11\n\tlive_link\x18\x1b \x01(\t\",\n\x0eOfficialVerify\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\"\xb7\x01\n\x0bReasonStyle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x18\n\x10text_color_night\x18\x03 \x01(\t\x12\x10\n\x08\x62g_color\x18\x04 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x05 \x01(\t\x12\x14\n\x0c\x62order_color\x18\x06 \x01(\t\x12\x1a\n\x12\x62order_color_night\x18\x07 \x01(\t\x12\x10\n\x08\x62g_style\x18\x08 \x01(\x05\x32z\n\x06Search\x12p\n\x08Suggest3\x12\x30.bilibili.app.interfaces.v1.SuggestionResult3Req\x1a\x32.bilibili.app.interfaces.v1.SuggestionResult3Replyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.interfaces.v1.search_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUGGESTIONRESULT3REQ._serialized_start=71
  _SUGGESTIONRESULT3REQ._serialized_end=153
  _SUGGESTIONRESULT3REPLY._serialized_start=155
  _SUGGESTIONRESULT3REPLY._serialized_end=266
  _RESULTITEM._serialized_start=269
  _RESULTITEM._serialized_end=814
  _OFFICIALVERIFY._serialized_start=816
  _OFFICIALVERIFY._serialized_end=860
  _REASONSTYLE._serialized_start=863
  _REASONSTYLE._serialized_end=1046
  _SEARCH._serialized_start=1048
  _SEARCH._serialized_end=1170
# @@protoc_insertion_point(module_scope)
