import capnp
import log_capnp
import socketserver
import struct

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client

        header = self.request.recv(8)
        print(f"header: {header}")
        length = int(header)
        msg = self.request.recv(length)
        print(f"log msg: {msg}")

        # header = self.request.recv(8)
        #
        # length = struct.unpack("ii", header)[1]
        # print(f"length: {length}")
        #
        # data = self.request.recv(8*length)
        #
        # msg = log_capnp.LogMsg.from_bytes(header+data)
        # print(f"log msg: {msg.message}")

        # print("{} wrote:".format(self.client_address[0]))

if __name__ == "__main__":
    HOST, PORT = "localhost", 12345

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
