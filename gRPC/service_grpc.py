import grpc
import time
from concurrent import futures
from google.protobuf import empty_pb2
import service_pb2
import service_pb2_grpc

class TestServiceServicer(service_pb2_grpc.TestServiceServicer):
    def NoArgsNoReturn(self, request, context):
        start = time.time();
        print(">>> Server received: NoArgsNoReturn")
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return empty_pb2.Empty()

    def OneLong(self, request, context):
        start = time.time();
        print(f"\n>>> Server received: OneLong({request.value})");
        
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return service_pb2.LongResponse(value=request.value)

    def EightLongs(self, request, context):
        start = time.time();
        print(f"\n>>> Server received: EightLongs({request.v1}, {request.v2}, ..., {request.v8})");
       
        result = sum([
            request.v1, request.v2, request.v3, request.v4,
            request.v5, request.v6, request.v7, request.v8
        ])
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return service_pb2.LongResponse(value=result)

    def OneString(self, request, context):
        start = time.time();
        print(f"\n>>> Server received: OneString({request.value})")
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return service_pb2.StringResponse(value=request.value.upper())

    def ComplexOperation(self, request, context):
        start = time.time();
        print(f"\n>>> Server received: ComplexOperation({request.complex.name}, {request.complex.age})");
        name = request.complex.name[::-1]  # Reverso do nome como exemplo
        age = request.complex.age + 1
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return service_pb2.ComplexResponse(
            complex=service_pb2.ComplexType(name=name, age=age)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TestServiceServicer_to_server(TestServiceServicer(), server)
    # Determina que todos os endereços IP podem ser lidos
    server.add_insecure_port('[::]:50051')
    server.start()
    print("\n\t\t=== Server running on port 50051 ===")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
