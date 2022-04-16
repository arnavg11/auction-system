import socket as sck
import threading as thr
def convertih(ipv4 = sck.gethostbyname(sck.gethostname())):
    return "".join([hex(int(i))[-2:] for i in ipv4.split(".")])
def converthi(ip4_e):
    ip = ""
    for i in range(4):
        if ip4_e[i*2]=="x":
            ip+=hex(int("0"+ip4_e[i*2+1],16))
        else:
            ip+=hex(int(ip4_e[i*2:i*2+2],16))
    return ip
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
t1.join()
