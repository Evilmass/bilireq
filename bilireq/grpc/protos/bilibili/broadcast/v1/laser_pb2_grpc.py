# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.broadcast.v1 import laser_pb2 as bilibili_dot_broadcast_dot_v1_dot_laser__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class LaserStub(object):
    """Laser
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WatchLogUploadEvent = channel.unary_stream(
                '/bilibili.broadcast.v1.Laser/WatchLogUploadEvent',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=bilibili_dot_broadcast_dot_v1_dot_laser__pb2.LaserLogUploadResp.FromString,
                )


class LaserServicer(object):
    """Laser
    """

    def WatchLogUploadEvent(self, request, context):
        """监听上报事件
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LaserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WatchLogUploadEvent': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchLogUploadEvent,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=bilibili_dot_broadcast_dot_v1_dot_laser__pb2.LaserLogUploadResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.broadcast.v1.Laser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Laser(object):
    """Laser
    """

    @staticmethod
    def WatchLogUploadEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bilibili.broadcast.v1.Laser/WatchLogUploadEvent',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            bilibili_dot_broadcast_dot_v1_dot_laser__pb2.LaserLogUploadResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
