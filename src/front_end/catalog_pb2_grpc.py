# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import catalog_pb2 as catalog__pb2


class CatalogServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.query = channel.unary_unary(
                '/CatalogService/query',
                request_serializer=catalog__pb2.QueryRequest.SerializeToString,
                response_deserializer=catalog__pb2.QueryResponse.FromString,
                )
        self.buy = channel.unary_unary(
                '/CatalogService/buy',
                request_serializer=catalog__pb2.BuyRequest.SerializeToString,
                response_deserializer=catalog__pb2.BuyResponse.FromString,
                )


class CatalogServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CatalogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=catalog__pb2.QueryRequest.FromString,
                    response_serializer=catalog__pb2.QueryResponse.SerializeToString,
            ),
            'buy': grpc.unary_unary_rpc_method_handler(
                    servicer.buy,
                    request_deserializer=catalog__pb2.BuyRequest.FromString,
                    response_serializer=catalog__pb2.BuyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CatalogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CatalogService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/CatalogService/query',
            catalog__pb2.QueryRequest.SerializeToString,
            catalog__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/CatalogService/buy',
            catalog__pb2.BuyRequest.SerializeToString,
            catalog__pb2.BuyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
