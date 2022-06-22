import socket as sck
import threading as thr
import pickle

def getIP():
    temp = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    temp.connect(("8.8.8.8",9000))
    return temp.getsockname()[0]
import tkinter as tk

myip = "localhost"


def read(x):
 try:
    while True:
        msg = x.recv(4096).decode()
        print(msg)
        if msg[0:4] == "name" and "-"in msg:
            for i in range(len(serv.connBuffer)):
                if serv.connBuffer[i][0]==x:
                    serv.conn[msg.split("-")[1]] = serv.connBuffer.pop(i)
                    print(420)
            serv.write("init_ack",x)
        else:
            msg = msg.split(":")
            try:
                recver = serv.conn[msg[0]]
                serv.write(msg[1],recver)
            except KeyError:
                serv.write("client not found", x)
 except ConnectionResetError:
     connLeft(x)
def connLeft(x):
     for user,conn in serv.conn.items():
         if conn[0]==x:
             del serv.conn[user]
             print("client has left: ",user)
             for user,client in serv.conn.items():
                 serv.write("left:"+user,client)
             break

def convertih(ipv4=getIP()):
    return "".join([hex(int(i))[-2:] for i in ipv4.split(".")])


def converthi(ip4_e):
    ip = ""
    for i in range(4):
        if ip4_e[i * 2] == "x":
            ip += str(int("0" + ip4_e[i * 2 + 1], 16))[:-2]
        else:
            ip += str(int(ip4_e[i * 2 : i * 2 + 2], 16))
        ip += "."
    ip = ip[:-1]
    return ip


t = None


class Server:
    def __init__(self):
        global t
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.socket.bind((myip, 6789))
        self.connBuffer = []
        self.conn = {}

        t = thr.Thread(target=self.startListen)
        t.start()

    def startListen(self):
        self.socket.listen(5)
        while True:
            self.connBuffer.append(self.socket.accept())
            print(self.connBuffer[-1])
            t = thr.Thread(target=lambda: read(self.connBuffer[-1][0]))
            t.start()

    def write(self, msg,c):
        print(type(msg.encode()))
        c.send(msg.encode())
class Client:
    def __init__(self, username = None):
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.ip = None
        self.user = username
    def read(self):
        while True:
            print(self.socket.recv(4096))

    def write(self, msg):
        print(msg.encode())
        self.socket.send(msg.encode())

    def setip(self, ip):
        self.ip = ip
        try:
            print(self.user)
            self.socket.connect((ip, 6789))
            self.write(f"name-{self.user}")
            t = thr.Thread(target=self.read)
            t.start()
            return True
        except:
            return False
