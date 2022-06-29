import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        while True:
            data = self.rfile.readline().strip()
            if not data:
                break
            print("{} wrote:".format(self.client_address[0]))
            print(data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 12345

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
