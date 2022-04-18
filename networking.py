import socket as sck
import threading as thr
def convertih(ipv4 = sck.gethostbyname('localhost')):
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
        self.socket.bind((sck.gethostbyname('localhost'),6000))
    def read(self):
        return self.socket.recvfrom(4096)
    def write(self,msg):
        self.socket.sendto(msg.encode(),(self.ip,6000))
    def setip(self,ip,firstms = False):
        if firstms:self.write(f"JOIN: {convertih()}")
        self.ip = ip
def temp():
    while True:process(x.read())
def process(msg):
    print(1)
    try:
        t2.terminate()
    except:pass
    msgspl = msg.split()
    if msgspl[0]=="JOIN:":
        x.setip(converthi(msgspl[1]))
        x.write(f"JOIN_RES: {convertih()}")
        print("join received")
    elif msgspl[0]=="JOIN_RES:":
        x.setip(converthi(msgspl[1]))
        print("join_RES received")
    
ipReceived = True
print(convertih())
x = Comp()
t1 = thr.Thread(target =temp )
t2 = thr.Thread(target = lambda:x.setip(input("enter ip:\t"),True))
t1.start()
t2.start()
t2.join()
t1.join()
