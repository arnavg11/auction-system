import socket as sck
import threading as thr
def convertih(ipv4 = sck.gethostbyname(sck.gethostname())):
    return "".join([hex(int(i))[-2:] for i in ipv4.split(".")])
class Comp:
    def __init__(self):
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
        self.socket.bind((sck.gethostbyname(sck.gethostname()),6000))
    def read(self):
        return self.socket.recvfrom(4096)
    def write(self,msg):
        self.socket.sendto(msg.encode(),(self.ip,6000))
    def setip(self,ip):
        self.ip = ip
def temp():
    while True:print(x.read())
print(convertih())
x = Comp()
t1 = thr.Thread(target =temp )
t1.start()
print("main")
