import socket as sck
class Server:
    def __init__(self,ip):
        self.socket = sck.socket()
        self.socket.bind(ip,6000)
        self.socket.listen()
        self.socket.accept()
    def read(self):
        return self.socket.read()
    def write(self):
        self.socket.w
