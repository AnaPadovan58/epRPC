import grpc
from concurrent import futures
from google.protobuf import empty_pb2
import service_pb2
import service_pb2_grpc

class TestServiceServicer(service_pb2_grpc.TestServiceServicer):
    def NoArgsNoReturn(self, request, context):
        print(">>> Server received: NoArgsNoReturn")
        return empty_pb2.Empty()

    def OneLong(self, request, context):
        print(f">>> Server received: OneLong({request.value})")
        return service_pb2.LongResponse(value=request.value)

    def EightLongs(self, request, context):
        print(f">>> Server received: EightLongs({request.v1}, {request.v2}, ..., {request.v8})")
        result = sum([
            request.v1, request.v2, request.v3, request.v4,
            request.v5, request.v6, request.v7, request.v8
        ])
        return service_pb2.LongResponse(value=result)

    def OneString(self, request, context):
        print(f">>> Server received: OneString({request.value})")
        return service_pb2.StringResponse(value=request.value.upper())

    def ComplexOperation(self, request, context):
        print(f">>> Server received: ComplexOperation({request.complex.name}, {request.complex.age})")
        name = request.complex.name[::-1]  # Reverso do nome como exemplo
        age = request.complex.age + 1
        return service_pb2.ComplexResponse(
            complex=service_pb2.ComplexType(name=name, age=age)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TestServiceServicer_to_server(TestServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("=== Server running on port 50051 ===")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
