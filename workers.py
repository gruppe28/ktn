'''
KTN-project 2013 / 2014
Python daemon thread class for listening for events on
a socket and notifying a listener of new messages or
if the connection breaks.

A python thread object is started by calling the start()
method on the class. in order to make the thread do any
useful work, you have to override the run() method from
the Thread superclass. NB! DO NOT call the run() method
directly, this will cause the thread to block and suspend the
entire calling process' stack until the run() is finished.
it is the start() method that is responsible for actually
executing the run() method in a new thread.
'''
from threading import Thread
import socket
import time


class ReceiveMessageWorker(Thread):

    def __init__(self, client):
        super(ReceiveMessageWorker, self).__init__()
        self.daemon = True
        self.client = client

    def run(self):
        while True:
            self.client.parse_server_data()
                
           
class SendMessageWorker(Thread):

    def __init__(self, client):
        super(SendMessageWorker, self).__init__()
        self.daemon = True
        self.client = client

    def run(self):
        while True:
            data = self.client.handle_input()
            self.client.send(data)
            time.sleep(0.1)
