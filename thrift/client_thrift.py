import time
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from myservice import TestService
from myservice.ttypes import *

def benchmark():
    transport = TSocket.TSocket('localhost', 50052)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = TestService.Client(protocol)

    transport.open()
    print("\n=== Thrift Benchmarks ===")

    # NoArgsNoReturn
    start = time.time()
    client.NoArgsNoReturn()
    print("NoArgsNoReturn:", time.time() - start)

    # OneLong
    req = LongRequest(value=42)
    start = time.time()
    client.OneLong(req)
    print("OneLong:", time.time() - start)

    # EightLongs
    req = EightLongsRequest(
        v1=1, v2=2, v3=3, v4=4, v5=5, v6=6, v7=7, v8=8
    )
    start = time.time()
    client.EightLongs(req)
    print("EightLongs:", time.time() - start)

    # OneString
    req = StringRequest(value="Hello world!")
    start = time.time()
    client.OneString(req)
    print("OneString:", time.time() - start)

    # ComplexOperation
    complex_data = ComplexType(name="Alice", age=30)
    req = ComplexRequest(complex=complex_data)
    start = time.time()
    client.ComplexOperation(req)
    print("ComplexOperation:", time.time() - start)

    transport.close()

if __name__ == "__main__":
    benchmark()
