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
    x.send(pickle.dumps("Hello"))
    while True:
        print(x.recv(4096))


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
        self.conn = []

        t = thr.Thread(target=self.startListen)
        t.start()

    def startListen(self):
        self.socket.listen(5)
        while True:
            self.conn.append(self.socket.accept())
            print(1)
            t = thr.Thread(target=lambda: read(self.conn[-1][0]))
            t.start()

    def write(self, msg):
        print(self.ip, type(msg.encode()))
        self.socket.send(msg.encode())


x = Server()
print(1)
t.join()
