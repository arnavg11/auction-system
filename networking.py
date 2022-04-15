import socket as sck
class Server:
    def __init__(self):
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
        self.socket.bind((sck.gethostbyname(sck.gethostname()),6000))
    def read(self):
        return self.socket.recvfrom(4096)
    def write(self,msg):
        self.socket.sendto(msg.encode(),6000)
c = Server()
print(sck.gethostbyname(sck.gethostname()))
while True : print(c.read())
