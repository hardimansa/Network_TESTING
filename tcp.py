import socketserver
import re

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.read().decode('utf-8')
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.output = re.findall(r"\bthan\b", self.data)
        print(self.output)
        



if __name__ == "__main__":
    HOST, PORT = "localhost", 12345
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

