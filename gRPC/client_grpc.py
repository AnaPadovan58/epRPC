import grpc
import time
from google.protobuf import empty_pb2
import service_pb2
import service_pb2_grpc

def benchmark():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.TestServiceStub(channel)

    # Verifica conexão com o servidor
    try:
        grpc.channel_ready_future(channel).result(timeout=5)
        print("✔ Conectado ao servidor!")
    except grpc.FutureTimeoutError:
        print("❌ Não foi possível conectar ao servidor.")
        return

    print("\n=== gRPC Benchmarks ===")

    # NoArgsNoReturn
    start = time.time()
    stub.NoArgsNoReturn(empty_pb2.Empty())
    print("NoArgsNoReturn:", time.time() - start)

    # OneLong
    req = service_pb2.LongRequest(value=42)
    start = time.time()
    stub.OneLong(req)
    print("OneLong:", time.time() - start)

    # EightLongs
    req = service_pb2.EightLongsRequest(
        v1=1, v2=2, v3=3, v4=4, v5=5, v6=6, v7=7, v8=8
    )
    start = time.time()
    stub.EightLongs(req)
    print("EightLongs:", time.time() - start)

    # OneString
    req = service_pb2.StringRequest(value="Hello world!")
    start = time.time()
    stub.OneString(req)
    print("OneString:", time.time() - start)

    # ComplexOperation
    complex_type = service_pb2.ComplexType(name="Alice", age=30)
    req = service_pb2.ComplexRequest(complex=complex_type)
    start = time.time()
    stub.ComplexOperation(req)
    print("ComplexOperation:", time.time() - start)

if __name__ == "__main__":
    benchmark()
