# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/show/mixture/v1/mixture.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*bilibili/app/show/mixture/v1/mixture.proto\x12\x1c\x62ilibili.app.show.mixture.v1\"2\n\nRcmdReason\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x13\n\x0b\x63orner_mark\x18\x02 \x01(\r\"\xbf\x01\n\nWidgetItem\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\x0c\n\x04view\x18\x02 \x01(\t\x12=\n\x0brcmd_reason\x18\x03 \x01(\x0b\x32(.bilibili.app.show.mixture.v1.RcmdReason\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0b\n\x03uri\x18\x06 \x01(\t\x12\x0c\n\x04goto\x18\x07 \x01(\t\x12\n\n\x02id\x18\x08 \x01(\x03\x12\x11\n\tview_icon\x18\t \x01(\x05\"E\n\x0bWidgetReply\x12\x36\n\x04item\x18\x01 \x03(\x0b\x32(.bilibili.app.show.mixture.v1.WidgetItem\"0\n\tWidgetReq\x12\x12\n\nfrom_spmid\x18\x01 \x01(\t\x12\x0f\n\x07page_no\x18\x02 \x01(\r2g\n\x07Mixture\x12\\\n\x06Widget\x12\'.bilibili.app.show.mixture.v1.WidgetReq\x1a).bilibili.app.show.mixture.v1.WidgetReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.show.mixture.v1.mixture_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_RCMDREASON']._serialized_start=76
  _globals['_RCMDREASON']._serialized_end=126
  _globals['_WIDGETITEM']._serialized_start=129
  _globals['_WIDGETITEM']._serialized_end=320
  _globals['_WIDGETREPLY']._serialized_start=322
  _globals['_WIDGETREPLY']._serialized_end=391
  _globals['_WIDGETREQ']._serialized_start=393
  _globals['_WIDGETREQ']._serialized_end=441
  _globals['_MIXTURE']._serialized_start=443
  _globals['_MIXTURE']._serialized_end=546
# @@protoc_insertion_point(module_scope)