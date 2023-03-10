# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import order_pb2 as order__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.buy = channel.unary_unary(
                '/OrderService/buy',
                request_serializer=order__pb2.OrderInfo.SerializeToString,
                response_deserializer=order__pb2.OrderNumber.FromString,
                )
        self.query = channel.unary_unary(
                '/OrderService/query',
                request_serializer=order__pb2.OrderNumber.SerializeToString,
                response_deserializer=order__pb2.OrderInfo.FromString,
                )
        self.ping = channel.unary_unary(
                '/OrderService/ping',
                request_serializer=order__pb2.Empty.SerializeToString,
                response_deserializer=order__pb2.Empty.FromString,
                )
        self.updateReplica = channel.unary_unary(
                '/OrderService/updateReplica',
                request_serializer=order__pb2.OrderInfo.SerializeToString,
                response_deserializer=order__pb2.OrderNumber.FromString,
                )
        self.recovery = channel.unary_unary(
                '/OrderService/recovery',
                request_serializer=order__pb2.OrderNumber.SerializeToString,
                response_deserializer=order__pb2.RecoveryInfo.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def buy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateReplica(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recovery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'buy': grpc.unary_unary_rpc_method_handler(
                    servicer.buy,
                    request_deserializer=order__pb2.OrderInfo.FromString,
                    response_serializer=order__pb2.OrderNumber.SerializeToString,
            ),
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=order__pb2.OrderNumber.FromString,
                    response_serializer=order__pb2.OrderInfo.SerializeToString,
            ),
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=order__pb2.Empty.FromString,
                    response_serializer=order__pb2.Empty.SerializeToString,
            ),
            'updateReplica': grpc.unary_unary_rpc_method_handler(
                    servicer.updateReplica,
                    request_deserializer=order__pb2.OrderInfo.FromString,
                    response_serializer=order__pb2.OrderNumber.SerializeToString,
            ),
            'recovery': grpc.unary_unary_rpc_method_handler(
                    servicer.recovery,
                    request_deserializer=order__pb2.OrderNumber.FromString,
                    response_serializer=order__pb2.RecoveryInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def buy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/buy',
            order__pb2.OrderInfo.SerializeToString,
            order__pb2.OrderNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/query',
            order__pb2.OrderNumber.SerializeToString,
            order__pb2.OrderInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/ping',
            order__pb2.Empty.SerializeToString,
            order__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateReplica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/updateReplica',
            order__pb2.OrderInfo.SerializeToString,
            order__pb2.OrderNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recovery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/recovery',
            order__pb2.OrderNumber.SerializeToString,
            order__pb2.RecoveryInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
