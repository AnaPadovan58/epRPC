from thrift import Thrift
import time
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer  
from myservice import TestService
from myservice.ttypes import *

class TestServiceHandler:
    def NoArgsNoReturn(self):
        start = time.time();
        print(">>> Server received: NoArgsNoReturn")
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return None

    def OneLong(self, request):
        start = time.time();
        print(f"\n>>> Server received: OneLong({request.value})")
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return LongResponse(value=request.value)

    def EightLongs(self, request):
        start = time.time();
        print(f"\n>>> Server received: EightLongs({request.v1}, ..., {request.v8})")
        total = sum([request.v1, request.v2, request.v3, request.v4, request.v5, request.v6, request.v7, request.v8])
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return LongResponse(value=total)

    def OneString(self, request):
        start = time.time();
        print(f"\n>>> Server received: OneString({request.value})")
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return StringResponse(value=request.value.upper())

    def ComplexOperation(self, request):
        start = time.time();
        print(f"\n>>> Server received: ComplexOperation({request.complex.name}, {request.complex.age})")
        new_name = request.complex.name[::-1]
        new_age = request.complex.age + 1
        print(f"\n\tTempo de execução no servidor: ", (time.time() - start), " seconds");
        return ComplexResponse(complex=ComplexType(name=new_name, age=new_age))

def start_thrift_server():
    handler = TestServiceHandler()
    processor = TestService.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=50052)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("\n\t\t=== Thrift server running on port 50052 ===")
    server.serve()

if __name__ == '__main__':
    start_thrift_server()
