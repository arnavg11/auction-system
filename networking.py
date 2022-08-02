import socket as sck
import threading as thr
import pickle

def getIP():
    temp = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    temp.connect(("8.8.8.8",9000))
    return temp.getsockname()[0]
import tkinter as tk

myip = getIP()


def read(x,comp):
 try:
    while True:
        msg = x.recv(4096).decode().split("-")
        print(msg)
        if msg[0] == "::name":
            u = msg[1]
            comp.pairList[u] = []
            comp.conn[u] = x
            print(420)
            comp.sendall(list(comp.pairList.keys()))
        elif msg[0] == "::cnct":
            p1,p2 = msg[1].split(":")
            if p1 in comp.pairList[p2]:
                print("paired")
                comp.pairList.pop(p1)
                comp.pairList.pop(p2)

                comp.write(f"auth-pair OK-{p2}",p1,True)
                comp.write(f"auth-pair OK-{p1}",p2,True)
            else:
                comp.pairList[p1].append(p2)
        else:
            print(1)
            try:
                print(comp.conn)
                recver = comp.conn[msg[0]]
                comp.write(msg[1],recver)
            except KeyError as e:
                
                print(e)
                comp.write("client not found", x)
 except ConnectionResetError:
     connLeft(x,comp)
def connLeft(x,comp):
     for k in comp.conn:
         if comp.conn[k]==x:
             break
     del comp.conn[k]
     del comp.pairList[k]
     print("client has left: ",k)
     comp.sendall(list(comp.pairList.keys()))

def convertih(ipv4=getIP()):
    return "".join([hex(int(i))[-2:] for i in ipv4.split(".")])


def converthi(ip4_e):
    ip = ""
    for i in range(4):
        if ip4_e[i * 2] == "x":
            ip += str(int("0" + ip4_e[i * 2 + 1], 16))
        else:
            ip += str(int(ip4_e[i * 2 : i * 2 + 2], 16))
        ip += "."
    ip = ip[:-1]
    return ip


t = None


class Server:
    def __init__(self):
        global t
        print(myip)
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.socket.bind((myip, 6789))
        self.conn = {}
        self.pairList = {}
        t = thr.Thread(target=self.startListen)
        t.start()

    def startListen(self):
        self.socket.listen(5)
        while True:
            x = self.socket.accept()[0]
            t = thr.Thread(target=lambda: read(x,self))
            t.start()

    def write(self, msg,c,user=False):
        if user: c = self.conn[c]
        print(type(msg.encode()))
        c.send(msg.encode())
    def sendall(self,msg,start = "players"):
        print(self.conn)
        for i in self.conn:
            self.write(f"{start}-{str(msg)}",self.conn[i])
class Client:
    def __init__(self, username = None):
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.ip = None
        self.user = username
        self.servconn = []
        self.paired = False
        self.opp = None
        self.eventhand = None
    def read(self):
        while True:
                x = self.socket.recv(4096).decode("utf-8").split("-")
                print(x)
                if x[0] == "players":
                    self.servconn = eval(x[1].lstrip("dict_keys"))
                    print(self.servconn)
                elif x[0]=="auth" and x[1]=="pair OK":
                    self.paired = True
                    self.opp = x[2]
                else:self.eventhand(x)#to be imported

    def write(self, msg):
        print(msg.encode())
        self.socket.send(msg.encode())

    def setip(self, ip):
        self.ip = converthi(ip)
        print(self.ip)
        try:
            print(self.user)
            self.socket.connect((self.ip, 6789))
            self.write(f"::name-{self.user}")
            t = thr.Thread(target=self.read)
            t.start()
            return True
        except:
            return False
         
