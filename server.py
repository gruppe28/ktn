''' KTN-project 2013 / 2014 Very simple server implementation that
should serve as a basis for implementing the chat server '''

import SocketServer
import json

'''
The RequestHandler class for our server.

It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
'''

class ClientHandler(SocketServer.BaseRequestHandler):

    username = ''
    
    def handle(self):
        # Get a reference to the socket object
        self.connection = self.request
        # Get the remote ip adress of the socket
        self.ip = self.client_address[0]
        # Get the remote port number of the socket
        self.port = self.client_address[1]
        print 'Client connected @' + self.ip + ':' + str(self.port)
        # Wait for data from the client
        data = json.loads(self.connection.recv(1024).strip())
        # Check if the data exists
        # (recv could have returned due to a disconnect)
        if data:
            print data
            # Return the string in uppercase
            self.connection.sendall(json.dumps(data))
        else:
            print 'Client disconnected!'

    def createMessageArray(messagetext, username):
        '''
        message[3] = [ TID , username, messagetext ]
        return message
        '''
        pass

    def validateClient(username):
        if username.find(
        
'''
This will make all Request handlers being called in its own thread.
Very important, otherwise only one client will be served at a time
'''


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 9999
    backlog = [{}]
    users = []

    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
