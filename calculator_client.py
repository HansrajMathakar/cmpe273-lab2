from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.AdditionStub(channel)
        response = stub.PerformAddition(calculator_pb2.AddRequest(nbr1=4, nbr2=5))
    print(response.message)


if __name__ == '__main__':
    run()