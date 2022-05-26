import socket as sck
import threading as thr
import pickle

"""
temp = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
temp.connect(("8.8.8.8",9000))
myip = temp.getsockname()[0]"""
import tkinter as tk

myip = "localhost"


def read(x):
    while True:
        msg = str(x.recv(4096))
        print(msg)
        if msg[0:4] == "name" and "-"in msg:
            for i in range(len(serv.connBuffer)):
                if serv.connBuffer[i][0]==x:
                    serv.conn[msg.split("-")[1]] = serv.connBuffer.pop(i)
                    print(420)
            serv.write("init_ack",x)
        else:
            msg = msg.split(":")
            recver = serv.findClient(msg[0])
            if recver!=None:
                serv.write(msg[1],recver)
            else:
                serv.write("client not found", x)
        

def convertih(ipv4=myip):
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
    def findClient(self,ip):
        for i in self.conn:
            if i[1][0] == ip:
                return i

serv = Server()
print(1)
t.join()
